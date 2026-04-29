from flask import request
from flask_restx import Namespace, Resource, fields
from app.models import db, User
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
import re
import os
import logging
from dotenv import load_dotenv
from app.extensions import limiter

# Load environment config
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(BASE_DIR, '.env'))

ADMIN_SECRET = os.getenv("ADMIN_SECRET")

# Namespace
auth_ns = Namespace('Auth', description="Authentication APIs")

# -------- Models --------
register_model = auth_ns.model("RegisterRequest", {
    "username": fields.String(required=True),
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "admin_key": fields.String(required=False),
})

login_model = auth_ns.model("LoginRequest", {
    "username": fields.String(required=True),
    "password": fields.String(required=True),
})

# -------- Register --------
@auth_ns.route('/register')
class Register(Resource):

    @auth_ns.expect(register_model)
    def post(self):
        data = request.json

        if not data.get("username") or not data.get("email") or not data.get("password"):
            return {"success": False, "message": "All fields required"}, 400

        username = data["username"].strip().lower()
        email = data["email"].strip().lower()
        password = data["password"]
        admin_key = data.get("admin_key")

        if len(username) < 3:
            return {"success": False, "message": "Username too short"}, 400

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return {"success": False, "message": "Invalid email"}, 400

        if not re.search(r"[A-Z]", password) or not re.search(r"[0-9]", password):
            return {"success": False, "message": "Weak password"}, 400

        if User.query.filter_by(username=username).first():
            return {"success": False, "message": "Username exists"}, 400

        if User.query.filter_by(email=email).first():
            return {"success": False, "message": "Email exists"}, 400

        if admin_key and ADMIN_SECRET and admin_key.strip() == ADMIN_SECRET.strip():
            role = "admin"
        else:
            role = "user"

        try:
            user = User(
                username=username,
                email=email,
                password=generate_password_hash(password),
                role=role
            )
            db.session.add(user)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            logging.error(f"Register Error: {str(e)}")
            return {"success": False, "message": "Internal server error"}, 500

        return {"success": True, "message": "User registered", "role": role}, 201


# -------- Login --------
@auth_ns.route('/login')
class Login(Resource):

    @limiter.limit("5 per minute")
    @auth_ns.expect(login_model)
    def post(self):
        data = request.json

        if not data.get("username") or not data.get("password"):
            return {"success": False, "message": "All fields required"}, 400

        username = data["username"].strip().lower()
        password = data["password"]

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            logging.warning(f"Failed login attempt: {username}")
            return {"success": False, "message": "Invalid credentials"}, 401

        token = create_access_token(
            identity=str(user.id),
            additional_claims={"role": user.role}
        )

        return {
            "success": True,
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
        }, 200