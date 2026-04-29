from functools import wraps
from flask_jwt_extended import get_jwt_identity
from app.models import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            user_id = int(get_jwt_identity())
            user = User.query.get(user_id)

            if not user or user.role != 'admin':
                return {"success": False, "message": "Admin only"}, 403

            return fn(*args, **kwargs)
        except Exception as e:
            return {"success": False, "message": str(e)}, 500

    return wrapper