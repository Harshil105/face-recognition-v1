# face-recognition-v1
Features 
1. Facial Recognition-based Authentication
2. Anti-Spoofing Detection
3. Automatic Login and Logout Tracking
4. User Registration and Login

Tech-Stack
1. Python FastAPI for Backend
2. SQL for Database
3. Facial Recognition Library
4. Anti-Spoofing Detection Models

# Setting up
 Backend

 Setting up Face recogniton library -
 
 1. Install cmake library using pip
    ```
    pip install cmake
    ```
 3. Download whl file for dlib according to your python version from this link https://github.com/z-mahmud22/Dlib_Windows_Python3.x
 4. For eg: if ur python version 3.10 then u will download " dlib-19.22.99-cp310-cp310-win_amd64.whl " this file
 5. using pip install the file from the path of the location it stored in after downloading
    ```
    pip install "/path/dlib-19.22.99-cp310-cp310-win_amd64.whl"
    ```
 7. Install the face recognition library using pip.
    ```
    pip install face-recognition
    ```
 9. Face recognition library is ready to import
 10. visit https://pypi.org/project/face-recognition/ for more information

Setting up Anti Spoofing model -
1. Visit " https://github.com/minivision-ai/Silent-Face-Anti-Spoofing/tree/master " and downwload the zip file of the github repository
2. Download whl file for dlib according to your python version from this link https://github.com/z-mahmud22/Dlib_Windows_Python3.x
3. Install all the dependencies from a separate requirements.txt file specially for antispoofing and the dlib file for antispoofing model and make sure in the terminal you are in the folder you downloaded from the github repository.
4. Test the model by typing this in the terminal
   ```
   python test.py --image_name your_image_name
   ```
5. Anti-Spoofing Model is ready to use

# Starting Backend Project 
1. Install fastapi and uvicorn
```
pip install fastapi uvicorn[standard]
```
2. For running the fastapi app
```
uvicorn main:app --reload
```
