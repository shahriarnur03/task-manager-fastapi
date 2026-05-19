from src.database.connection import Base
from sqlalchemy import Column, Integer, String, Boolean

# here create a database table
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)