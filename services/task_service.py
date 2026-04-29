from app.models import Task, db

def create_task(data, user_id):
    assigned_to = data.get("assigned_to", user_id)

    task = Task(
        title=data["title"],
        description=data.get("description"),
        user_id=assigned_to
    )

    db.session.add(task)
    db.session.commit()
    return task