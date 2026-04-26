from fastapi import APIRouter
from src.schemas.task import Task, TaskCreate
from src.services import task_service

router = APIRouter()

@router.post("/tasks", response_model = Task)
def create_task(task: TaskCreate):
    return task_service.create_task(task)

@router.get("/tasks")
def get_tasks():
    return task_service.get_task()

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = task_service.get_task_by_id(task_id)
    if not task:
        return {"error": "Task is not found"}
    return task

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    updated = task_service.update_task(task_id, task)
    if not updated:
        return {"error": "Task not found"}
    return updated

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task_service.delete_task(task_id)
    return {"message": "deleted"}