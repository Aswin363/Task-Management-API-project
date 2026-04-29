from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from datetime import datetime

db = SQLAlchemy()


# ---------------- USER MODEL ----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # unique username for login
    username = db.Column(db.String(50), unique=True, nullable=False)

    # email for identification (industry standard)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # hashed password (never store plain text)
    password = db.Column(db.String(255), nullable=False)

    # role-based access control (admin/user)
    role = db.Column(db.String(20), default="user", nullable=False)

    # relationship → one user can have multiple tasks
    tasks = db.relationship('Task', backref='user', lazy=True)


# ---------------- ROLE PROTECTION ----------------
# Prevents role modification after creation (security control)
@event.listens_for(User, "before_update")
def prevent_role_change(mapper, connection, target):
    state = db.inspect(target)

    if state.attrs.role.history.has_changes():
        raise ValueError("Role cannot be changed once set")


# ---------------- TASK MODEL ----------------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # task title (required)
    title = db.Column(db.String(100), nullable=False)

    # optional description
    description = db.Column(db.String(200))

    # task status (controlled values: pending, in_progress, completed)
    status = db.Column(db.String(20), default="pending")

    # foreign key → each task belongs to a user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # ---------------- NEW FIELDS ----------------

    # record creation timestamp
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # auto update timestamp on modification
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # soft delete flag (instead of permanent deletion)
    is_deleted = db.Column(db.Boolean, default=False)