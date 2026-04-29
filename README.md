# 🚀 Task Management API (Flask + JWT + RBAC)

> 🎓 MCA Final Year Project  
> A secure and scalable Task Management API with Role-Based Access Control and JWT Authentication.

---

## 🧠 Project Overview

This project is a backend system designed to simulate real-world task management used in organizations.

It focuses on:
- Secure authentication
- Role-based authorization
- Controlled task workflow
- Clean and modular backend architecture

---

## 🏗️ Project Structure
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

## ⚙️ Technologies Used

- Python (Flask)
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite
- Flasgger (Swagger UI)

---

## 🔐 Authentication System

- JWT (JSON Web Token) based authentication
- Password hashing for security
- Token required for protected routes

Example:
Authorization: Bearer <your-token>

---

## 👥 Role-Based Access Control (RBAC)

| Role  | Permissions |
|-------|------------|
| Admin | Full access (create, update, delete any task) |
| User  | Can manage only their own tasks |

---

## 📋 Task Workflow
pending → in-progress → completed

- Users must follow this sequence
- Admin can override status

---

## 📌 API Endpoints

### 🔐 Auth

| Method | Endpoint   | Description |
|--------|-----------|------------|
| POST   | /register | Register user |
| POST   | /login    | Login & get JWT |

---

### 📋 Tasks

| Method | Endpoint        | Description |
|--------|----------------|------------|
| POST   | /tasks         | Create task |
| GET    | /tasks         | Get tasks |
| PUT    | /tasks/{id}    | Update task |
| DELETE | /tasks/{id}    | Delete task |

---

## 🧪 Validation Rules

- Title: 3–100 characters
- Description: Max 200 characters
- Status: pending / in-progress / completed
- Password: Must contain uppercase + number

---

## 🗄️ Database Design

### 👤 User Table
- id
- username
- password (hashed)
- role

### 📋 Task Table
- id
- title
- description
- status
- user_id (Foreign Key)

---

## 🔗 Relationship

One User → Many Tasks

---

## 🌐 Swagger Documentation
http://127.0.0.1:5000/apidocs/

---

## 🧪 Testing

- Swagger UI
- Role-based testing:
  - Admin → full control
  - User → restricted access
  - Unauthorized access → 403 error

---

## 📸 Screenshots Included

- Registration
- Login (JWT Token)
- Create Task
- Get Tasks
- Update Task
- Unauthorized Access (403)
- Delete Task
- Database View

---

## ⚠️ Important Notes

- Strong JWT secret key required
- Do not use debug mode in production
- Input validation ensures data integrity

---

## 🎯 Conclusion

This project demonstrates:

- REST API development
- Authentication & Authorization
- Database design
- Secure coding practices
- Real-world backend logic

---

## 👨‍💻 Author

**Aswinsahu**  
MCA Final Year Student

---

## 🙏 Acknowledgment

I sincerely thank my faculty and HOD for their guidance and support.

---

## ⭐ Final Statement

This project represents a complete backend system with security, validation, and real-world architecture.
