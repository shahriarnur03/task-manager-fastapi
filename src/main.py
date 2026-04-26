from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI(title= "Task manager API")

# Fake database
tasks = [
  {
    "title": "Task 1",
    "completed": False,
    "id": 1
  },
  {
    "title": "Task 2",
    "completed": False,
    "id": 2
  },
  {
    "title": "Task 3",
    "completed": False,
    "id": 3
  },
  {
    "title": "Task 4",
    "completed": False,
    "id": 4
  },
  {
    "title": "Task 5",
    "completed": False,
    "id": 5
  },
  {
    "title": "Task 6",
    "completed": False,
    "id": 6
  },
  {
    "title": "Task 7",
    "completed": False,
    "id": 7
  },
  {
    "title": "Task 8",
    "completed": False,
    "id": 8
  },
  {
    "title": "Task 9",
    "completed": False,
    "id": 9
  },
  {
    "title": "Task 10",
    "completed": False,
    "id": 10
  }
]

class Task(BaseModel):
    title: str
    completed: bool = False

@app.post("/tasks")
def create_task(task: Task):
    task_dict = task.dict()
    task_dict["id"] = len(tasks) +1
    tasks.append(task_dict)
    return task_dict

@app.get("/tasks")
def get_task():
    return tasks

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return{"error": "Task is not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, update_task: Task):
    for task in tasks:
        if task_id == task["id"]:
            task["title"] = update_task.title
            task["completed"] = update_task.completed
            return task
    return {"error": "Task is not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"error": "Task is not found"}

