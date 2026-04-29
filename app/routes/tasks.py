from flask import request
from flask_restx import Namespace, Resource, fields
from app.models import db, Task, User
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
import logging

# Namespace
task_ns = Namespace("tasks", description="Task APIs", path="/api/tasks")

# ---------------- MODELS ----------------
task_model = task_ns.model("TaskRequest", {
    "title": fields.String(required=True),
    "description": fields.String,
    "assigned_to": fields.Integer
})

assign_model = task_ns.model("AssignTask", {
    "user_id": fields.Integer(required=True)
})

update_model = task_ns.model("UpdateTask", {
    "title": fields.String,
    "description": fields.String,
    "status": fields.String
})

ALLOWED_STATUS = ["pending", "in_progress", "completed"]

STATUS_FLOW = {
    "pending": ["in_progress"],
    "in_progress": ["completed"],
    "completed": []
}

#............. GET + CREATE................
@task_ns.route('')
class TaskList(Resource):

    @jwt_required()
    @task_ns.doc(params={
        "page": "Page number (default=1)",
        "limit": "Items per page (default=5, max=50)",
        "title": "Search by title",
        "status": "Filter by status",
        "sort": "Sort by field (id/title/status)",
        "order": "asc or desc"
    })
    def get(self):
        try:
            user_id = int(get_jwt_identity())
            role = get_jwt().get("role", "user")

            page = request.args.get("page", 1, type=int)
            limit = min(request.args.get("limit", 5, type=int), 50)

            title = request.args.get("title")
            status = request.args.get("status")
            sort = request.args.get("sort", "id")
            order = request.args.get("order", "asc")

            query = Task.query.filter_by(is_deleted=False)

            # RBAC
            if role != "admin":
                query = query.filter_by(user_id=user_id)

            #  Filtering
            if title:
                query = query.filter(Task.title.ilike(f"%{title}%"))

            if status:
                query = query.filter(Task.status == status)

            #  Sorting
            if sort == "title":
                column = Task.title
            elif sort == "status":
                column = Task.status
            else:
                column = Task.id

            if order == "desc":
                column = column.desc()

            query = query.order_by(column)

            # Pagination
            tasks = query.paginate(page=page, per_page=limit, error_out=False)

            return {
                "success": True,
                "total": tasks.total,
                "page": page,
                "limit": limit,
                "pages": tasks.pages,
                "has_next": tasks.has_next,
                "has_prev": tasks.has_prev,
                "data": [
                    {
                        "id": t.id,
                        "title": t.title,
                        "description": t.description,
                        "status": t.status,
                        "user_id": t.user_id
                    } for t in tasks.items
                ]
            }, 200

        except Exception:
            logging.exception("GET ERROR")
            return {"message": "Internal error"}, 500


    @task_ns.expect(task_model, validate=True)
    @jwt_required()
    def post(self):
        try:
            data = request.json or {}
            role = get_jwt().get("role")

            if role != "admin":
                return {"message": "Only admin can create tasks"}, 403

            title = data.get("title", "").strip()
            description = data.get("description", "").strip()

            if not title or len(title) < 3:
                return {"message": "Invalid title"}, 400

            if description and len(description) > 200:
                return {"message": "Description too long"}, 400

            assigned_to = data.get("assigned_to")

            if not assigned_to:
                return {"message": "assigned_to (user_id) required"}, 400

            user = db.session.get(User, int(assigned_to))
            if not user:
                return {"message": "User not found"}, 404

            task = Task(
                title=title,
                description=description,
                status="pending",
                user_id=assigned_to
            )

            db.session.add(task)
            db.session.commit()

            return {"message": "Task assigned successfully", "task_id": task.id}, 201

        except Exception:
            db.session.rollback()
            logging.exception("CREATE ERROR")
            return {"message": "Internal error"}, 500


# ...................SINGLE TASK..................
@task_ns.route('/<int:task_id>')
class TaskResource(Resource):

    @jwt_required()
    def get(self, task_id):
        user_id = int(get_jwt_identity())
        role = get_jwt().get("role")

        task = Task.query.filter_by(id=task_id, is_deleted=False).first_or_404()

        if role != "admin" and task.user_id != user_id:
            return {"message": "Not allowed"}, 403

        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "user_id": task.user_id
        }


    # ..................... UPDATE ......................
    @task_ns.expect(update_model, validate=True)
    @jwt_required()
    def put(self, task_id):
        try:
            data = request.json or {}

            if not data:
                return {"message": "Request body required"}, 400

            user_id = int(get_jwt_identity())
            role = get_jwt().get("role")

            task = Task.query.filter_by(id=task_id, is_deleted=False).first_or_404()

            if role != "admin" and task.user_id != user_id:
                return {"message": "Not allowed"}, 403

            # ADMIN → full control
            if role == "admin":
                if "title" in data:
                    task.title = data["title"]

                if "description" in data:
                    task.description = data["description"]

                if "status" in data:
                    if data["status"] not in ALLOWED_STATUS:
                        return {"message": "Invalid status"}, 400
                    task.status = data["status"]

            # USER → controlled status
            else:
                new_status = data.get("status")

                if not new_status:
                    return {"message": "Status required"}, 400

                allowed_next = STATUS_FLOW.get(task.status, [])

                if new_status not in allowed_next:
                    return {
                        "message": f"Invalid transition from {task.status} to {new_status}"
                    }, 400

                task.status = new_status

            db.session.commit()
            return {"message": "Task updated"}, 200

        except Exception as e:
            db.session.rollback()
            logging.error(f"UPDATE ERROR: {str(e)}")
            return {"message": "Internal error"}, 500


    # ..................... DELETE ........................
    @jwt_required()
    def delete(self, task_id):
        try:
            role = get_jwt().get("role")

            if role != "admin":
                return {"message": "Admin only"}, 403

            task = Task.query.filter_by(id=task_id, is_deleted=False).first_or_404()

            task.is_deleted = True
            db.session.commit()

            return {"message": "Task deleted"}, 200

        except Exception:
            db.session.rollback()
            logging.exception("DELETE ERROR")
            return {"message": "Internal error"}, 500


# .....................ASSIGN ....................
@task_ns.route('/<int:task_id>/assign')
class AssignTask(Resource):

    @task_ns.expect(assign_model, validate=True)
    @jwt_required()
    def patch(self, task_id):
        try:
            role = get_jwt().get("role")

            if role != "admin":
                return {"message": "Admin only"}, 403

            data = request.json or {}
            user_id = data.get("user_id")

            if not user_id:
                return {"message": "user_id required"}, 400

            user = db.session.get(User, user_id)
            if not user:
                return {"message": "User not found"}, 404

            task = Task.query.filter_by(id=task_id, is_deleted=False).first_or_404()

            if task.user_id == user_id:
                return {"message": "Task already assigned"}, 200

            task.user_id = user_id
            db.session.commit()

            return {"message": "Task reassigned successfully"}, 200

        except Exception as e:
            db.session.rollback()
            logging.error(f"ASSIGN ERROR: {str(e)}")
            return {"message": "Internal error"}, 500