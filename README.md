# 🚀 Task Management API

**Production-Grade Backend System using Flask**

---

## 📌 Overview

The Task Management API is a production-ready backend system developed using Flask, designed with modern software engineering principles such as modular architecture, secure authentication, and scalable API design.

This system enables efficient task management with strict role-based access control, ensuring that users can perform only authorized operations. The application simulates real-world enterprise backend systems with strong emphasis on security, maintainability, and performance optimization.

---

## 🎯 Objectives

* Design a scalable RESTful API using Flask
* Implement secure authentication using JWT
* Enforce Role-Based Access Control (RBAC)
* Maintain clean and modular architecture
* Support pagination, filtering, and sorting
* Ensure robust validation and error handling
* Implement unit testing for reliability

---

## ⚙️ Core Features

### 🔐 Authentication & Security

* Secure user registration and login
* JWT-based authentication with role claims
* Password hashing using Werkzeug
* Rate limiting (Brute-force protection)
* Input validation and error handling

---

### 📋 Task Management

* Full CRUD operations for tasks
* Task assignment to users
* Soft delete mechanism
* Task status tracking (pending → in_progress → completed)
* Ownership validation for secure access

---

### 🛡️ Role-Based Access Control (RBAC)

**Admin Permissions:**

* Create and assign tasks
* View all tasks
* Update and delete tasks

**User Permissions:**

* View assigned tasks
* Update only task status
* Restricted access to other users' data

---

### 🌐 API Capabilities

* RESTful API design
* JSON-based request-response handling
* Swagger documentation (Flask-RESTX)
* Pagination, filtering, and sorting
* Standard HTTP status codes

---

### 🧪 Testing

* Unit testing using pytest
* Covers authentication and task APIs
* Handles edge cases and validation scenarios

---

## 🧰 Technology Stack

* **Language:** Python 3
* **Framework:** Flask
* **ORM:** SQLAlchemy
* **Authentication:** Flask-JWT-Extended
* **Rate Limiting:** Flask-Limiter
* **API Docs:** Flask-RESTX (Swagger)
* **Database:** SQLite
* **Testing:** pytest

---

## 🏗️ Project Architecture

The system follows a modular layered architecture:

* **Routes Layer:** API endpoints
* **Business Logic Layer:** Core application rules
* **Data Layer:** Database interactions
* **Security Layer:** JWT authentication & RBAC

This architecture ensures scalability, maintainability, and separation of concerns.

---

## 🗄️ Database Design

### User

* Stores authentication details and roles
* Supports RBAC

### Task

* Stores task information
* Includes status tracking and soft delete
* Linked to User via foreign key

---

## 🔗 API Endpoints

### Authentication

* `POST /auth/register`
* `POST /auth/login`

### Tasks

* `GET /api/tasks`
* `POST /api/tasks`
* `GET /api/tasks/{id}`
* `PUT /api/tasks/{id}`
* `DELETE /api/tasks/{id}`
* `PATCH /api/tasks/{id}/assign`

---

## 🔄 Authentication Flow

1. User registers
2. User logs in
3. JWT token is generated
4. Token is sent in Authorization header
5. Protected APIs validate token before execution

---

## 🚀 Running the Project


### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create `.env` file:

```
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
ADMIN_SECRET=your-admin-key
```

---

### 5. Run Application

```bash
python app.py
```

---

### 6. Access Swagger UI

```
http://127.0.0.1:5000/docs
```

---

## 📁 Project Structure

```
Task-Management-API-project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── extensions.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── tasks.py
│   ├── services/
│   ├── utils/
│
├── instance/
│   └── tasks.db
│
├── tests/
├── config.py
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
```

---

## 🔒 Security Considerations

* Passwords stored as hashed values
* JWT ensures secure API communication
* RBAC restricts unauthorized access
* Rate limiting prevents brute-force attacks

---

## 🔮 Future Enhancements

* PostgreSQL integration
* Docker deployment
* Microservices architecture
* Frontend integration
* Notification system

---

## 📌 Conclusion

This project demonstrates the implementation of a production-grade backend system with strong emphasis on security, modular design, and scalability. It reflects real-world API development practices and is suitable for extension into enterprise-level applications.

---
