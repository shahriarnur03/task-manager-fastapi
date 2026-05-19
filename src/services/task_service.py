from src.database.models import Task


def create_task(db, task_data):
    task = Task(
        title=task_data.title,
        completed=task_data.isCompleted,
    )

    
    
    db.add(task) # Prepare insert query
    db.commit() # Actually save to DB. Without commit → nothing save
    db.refresh(task) # Reload object from DB
    
    return task


def get_task(db):
    return db.query(Task).all()


def get_task_by_id(task_id: int, db):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(task_id: int, update_data, db):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    task.title = update_data.title
    task.completed = update_data.isCompleted
    db.commit()
    db.refresh(task)
    return task


def delete_task(task_id: int, db):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True