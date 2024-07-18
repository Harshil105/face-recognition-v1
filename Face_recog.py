from io import BytesIO
import numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, status
import face_recognition
from PIL import Image
import os
from Antispoofing.test import test
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import date, time
from datetime import datetime

app = FastAPI()

# registration
models.Base.metadata.create_all(bind=engine)


class LogInBase(BaseModel):
    name: str
    date: date
    login: time


class LogOutBase(BaseModel):
    name: str
    date: date
    logout: time


class UserBase(BaseModel):
    name: str
    email: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/register/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    return {"message": "User created successfully"}


async def update_login_table(username: str, db: Session):
    login_time = datetime.now().time()
    todays_date = datetime.now().date()
    login_instance = models.LogIn(name=username, date=todays_date, login=login_time)
    db.add(login_instance)
    db.commit()


async def update_logout_table(username: str, db: Session):
    logout_time = datetime.now().time()
    todays_date = datetime.now().date()
    logout_instance = models.LogOut(name=username, date=todays_date, logout=logout_time)
    db.add(logout_instance)
    db.commit()


# face recognition
user_images_folder = "/path/photos" #put the path to the folder
face_database = {}


def load_face_database():
    for filename in os.listdir(user_images_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            username = os.path.splitext(filename)[0]
            image_path = os.path.join(user_images_folder, filename)
            face_image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(face_image)[0]
            face_database[username] = face_encoding


load_face_database()


def recognize_face(unknown_face_encoding):
    for username, known_face_encoding in face_database.items():
        if face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)[0]:
            return username
    return None


# apis

@app.post("/login")
async def recognize_person_login(image: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        image_data = await image.read()
        img = Image.open(BytesIO(image_data))
        unknown_face_encoding = face_recognition.face_encodings(np.array(img))[0]
        recognized_person = recognize_face(unknown_face_encoding)

        if recognized_person:
            await update_login_table(recognized_person, db)
            return {"message": "Login successful", "username": recognized_person}
        else:
            return {"message": "Face not recognized"}

    except Exception as e:
        raise HTTPException(detail=str(e), status_code=500)


@app.post("/logout")
async def recognize_person_logout(image: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        image_data = await image.read()
        img = Image.open(BytesIO(image_data))
        unknown_face_encoding = face_recognition.face_encodings(np.array(img))[0]
        recognized_person = recognize_face(unknown_face_encoding)

        if recognized_person:
            await update_logout_table(recognized_person, db)
            return {"message": "Logout successful", "username": recognized_person}
        else:
            return {"message": "Face not recognized"}

    except Exception as e:
        raise HTTPException(detail=str(e), status_code=500)

# antispoofing

# @app.post("/antispoofing")
# async def spoof(image: UploadFile = File(...)):
#     try:
#         image_data = await image.read()
#         img = Image.open((BytesIO(image_data)))
#         new_img = img.resize((480,640))
#         label = test(image_name = new_img,
#                    model_dir = "C:/Users/harsh/fastapi/Silent-Face-Anti-Spoofing-master/resources/anti_spoof_models",
#                    device_id = 0
#                    )
#         if label == 1:
#             return {"message": "Real"}
#         else:
#             return {"message": "Fake"}
#     except Exception as e:
#         raise HTTPException(detail=str(e), status_code=501)
#     db.add(db_user)
#     db.commit()
