<<<<<<< HEAD
# Task Management API (Flask + JWT + RBAC)

> 🎓 MCA Final Year Project  
> A secure and scalable Task Management API with Role-Based Access Control and JWT Authentication.

---

## Project Overview

This project is a backend system designed to simulate real-world task management used in organizations.

It focuses on:
- Secure authentication
- Role-based authorization
- Controlled task workflow
- Clean and modular backend architecture

---

## Project Structure
task_manager_API/
│
├── app.py # Main application entry point
├── config.py # Configuration (DB, JWT)
├── models.py # Database models (User, Task)
│
├── routes/
│ ├── auth.py # Register & Login APIs
│ └── tasks.py # Task CRUD APIs
│
├── instance/
│ └── tasks.db # SQLite database
│
├── venv/ # Virtual environment
└── README.md

---

##  Technologies Used

- Python (Flask)
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite
- Flasgger (Swagger UI)

---

##  Authentication System

- JWT (JSON Web Token) based authentication
- Password hashing for security
- Token required for protected routes

Example:
Authorization: Bearer <your-token>

---

##  Role-Based Access Control (RBAC)

| Role  | Permissions |
|-------|------------|
| Admin | Full access (create, update, delete any task) |
| User  | Can manage only their own tasks |

---

##  Task Workflow
pending → in-progress → completed

- Users must follow this sequence
- Admin can override status

---

##  API Endpoints

###  Auth

| Method | Endpoint   | Description |
|--------|-----------|------------|
| POST   | /register | Register user |
| POST   | /login    | Login & get JWT |

---

###  Tasks

| Method | Endpoint        | Description |
|--------|----------------|------------|
| POST   | /tasks         | Create task |
| GET    | /tasks         | Get tasks |
| PUT    | /tasks/{id}    | Update task |
| DELETE | /tasks/{id}    | Delete task |

---

##  Validation Rules

- Title: 3–100 characters
- Description: Max 200 characters
- Status: pending / in-progress / completed
- Password: Must contain uppercase + number

---

##  Database Design

###  User Table
- id
- username
- password (hashed)
- role

###  Task Table
- id
- title
- description
- status
- user_id (Foreign Key)

---

##  Relationship

One User → Many Tasks

---

##  Swagger Documentation
http://127.0.0.1:5000/apidocs/

---

##  Testing

- Swagger UI
- Role-based testing:
  - Admin → full control
  - User → restricted access
  - Unauthorized access → 403 error

---

##  Screenshots Included

- Registration
- Login (JWT Token)
- Create Task
- Get Tasks
- Update Task
- Unauthorized Access (403)
- Delete Task
- Database View

---

##  Important Notes

- Strong JWT secret key required
- Do not use debug mode in production
- Input validation ensures data integrity

---

##  Conclusion

This project demonstrates:

- REST API development
- Authentication & Authorization
- Database design
- Secure coding practices
- Real-world backend logic

---

##  Author

**Aswinsahu**  
MCA Final Year Student

---

##  Acknowledgment

I sincerely thank my faculty and HOD for their guidance and support.

---

##  Final Statement

This project represents a complete backend system with security, validation, and real-world architecture.
=======
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
>>>>>>> db5435423e611bbacc207e1192c71317df88fd27
