from fastapi import FastAPI
from src.api.routes.task_routes import router as task_router
from src.database.connection import Base, engine

# create_all() - Create all tables defined in the metadata if they do not already exist
# checks whether the tables exist.
# If not → creates them
# If yes → does nothing
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(task_router)
