import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "tasks.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")