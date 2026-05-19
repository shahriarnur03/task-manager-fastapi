from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://:shahriar@localhost/task_manager"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False, # auto save. False means we need to call db.commit() to save changes. True means changes will be saved automatically after each operation. if we set 2 data. 1st one correct and 2nd one incorrect. if autocommit is True, 1st one will be saved but 2nd one will not be saved. if autocommit is False, both of them will not be saved.
    autoflush=False,
    bind=engine # bind the engine to the session. This means that the session will use the engine to connect to the database. 
)

Base = declarative_base() # This is the base class for all our models. We will inherit from this class to create our models. It will also create the tables in the database.