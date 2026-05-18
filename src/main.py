from fastapi import FastAPI
from src.api.routes.task_routes import router as task_router
from src.database.connection import engine
from src.database.models import Task

Task.metadata.create_al(bind=engine)

app = FastAPI()

app.include_router(task_router)
