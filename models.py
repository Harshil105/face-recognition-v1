from sqlalchemy import Boolean, Column, Integer, String, Time, Date
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    email = Column(String(50))

class LogIn(Base):
    __tablename__ = 'logIN'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    date = Column(Date)
    login = Column(Time)

class LogOut(Base):
    __tablename__ = 'logOUT'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    date = Column(Date)
    logout = Column(Time)