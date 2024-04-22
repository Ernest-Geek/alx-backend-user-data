#!/usr/bin/env python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class User(Base):
    """
    User model representing a user in the database.

    Attributes:
        id (int): The integer primary key for the user.
        email (str): The email address of the user. Non-nullable.
        hashed_password (str): The hashed password of the user. Non-nullable.
        session_id (str, optional): The session ID of the user.
        reset_token (str, optional): The reset token of the user.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
