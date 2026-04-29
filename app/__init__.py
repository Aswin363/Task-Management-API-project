from dotenv import load_dotenv
load_dotenv()   # Load environment variables

from flask import Flask
from config import Config
from app.models import db
from flask_jwt_extended import JWTManager
from flask_restx import Api
from app.extensions import limiter
from datetime import timedelta
import logging


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ---------------- JWT CONFIG ----------------
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

    # ---------------- LOGGING ----------------
    logging.basicConfig(level=logging.INFO)

    # ---------------- INIT EXTENSIONS ----------------
    db.init_app(app)
    limiter.init_app(app)
    JWTManager(app)

    # ---------------- SWAGGER CONFIG ----------------
    authorizations = {
        "Bearer": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Bearer <JWT Token>"
        }
    }

    api = Api(
        app,
        title="Task Management API",
        version="1.0",
        description="Production-ready Task Management System",
        doc="/docs",
        authorizations=authorizations,
        security="Bearer"
    )

    # ---------------- REGISTER ROUTES ----------------
    from app.routes.auth import auth_ns
    from app.routes.tasks import task_ns

    api.add_namespace(auth_ns)
    api.add_namespace(task_ns)

    return app