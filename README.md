Task Management API

Project Overview

This project is a production-like REST API built using Flask. It allows users to manage tasks with authentication, role-based access, and a structured task workflow.

The system is designed to simulate real-world backend behavior where admin and normal users have different responsibilities.

Admin can create, assign, update, and monitor tasks.
User can view and update only their assigned tasks.

---

Features

Authentication
User registration
User login using JWT
Secure password hashing

Task Management
Create task
Get tasks with pagination and filtering
Update task
Delete task

Role-Based Access
Admin has full control
User can access only their own tasks

Task Assignment
Admin can assign tasks to any user
User cannot assign tasks

Task Status Workflow
pending to in_progress to completed
Invalid transitions are restricted

Advanced Features
Pagination using page and limit
Filtering using title search
Proper HTTP status codes
Structured JSON responses

---

Tech Stack

Backend: Flask
Database: SQLite
ORM: SQLAlchemy
Authentication: Flask-JWT-Extended
API Documentation: Swagger (Flasgger)

---

Project Structure

task_manager_api/

app.py
config.py
models.py
requirements.txt

routes/
auth.py
tasks.py

tests/
screenshots/
README.md

---

Installation and Setup

Clone the repository

git clone your-repo-link

Go to project folder

cd task_manager_api

Create virtual environment

python -m venv venv
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the server

python app.py

---

API Endpoints

Authentication

POST /register
Register a new user

POST /login
Login and get JWT token

Tasks

GET /tasks
Get tasks with pagination and filtering

POST /tasks
Create a new task

PUT /tasks/<id>
Update task

DELETE /tasks/<id>
Delete task

---

Authorization

Use JWT token in header

Authorization: Bearer your_token

---

Test Cases

Register success
Register duplicate
Login success
Login invalid
Task creation authorized

---

Screenshots

Authentication flows
Task CRUD operations
Role-based access
Status updates
Error handling

---

Key Concepts Used

REST API design
JWT authentication
Role-based authorization
Input validation
Error handling
Database transactions
Secure password hashing

---

Production-Level Features

Role-based access control
Task assignment system
Status workflow control
Secure authentication
Clean API design

---

Future Improvements

Refresh tokens
Email notifications
Task deadlines
Frontend integration

---

Conclusion

This project demonstrates practical backend development skills with focus on security, clean architecture, and real-world API design.
