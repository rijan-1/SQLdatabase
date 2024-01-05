import sqlalchemy.orm as _orm
import passlib.hash as _hash
from schemas import UserCreate
from database import engine, Base, SessionLocal
import models as _models
import logging  # Import the logging module

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG

def create_database():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        logging.error("Error creating database: %s", str(e))  # Log the error
        raise e  # Re-raise the exception

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_user_by_email(email: str, db: _orm.Session):
    try:
        return  db.query(_models.User).filter(_models.User.email == email).first()
    except Exception as e:
        logging.error("Error fetching user by email: %s", str(e))  # Log the error
        raise e  # Re-raise the exception

async def create_user(user: UserCreate, db: _orm.Session):
    try:
        user_obj = _models.User(
            email=user.email, hashed_password=_hash.bcrypt.hash(user.hashed_password)
        )
        db.add(user_obj)
        db.commit()
        db.refresh(user_obj)
        return user_obj
    except Exception as e:
        logging.error("Error creating user: %s", str(e))  # Log the error
        raise e  # Re-raise the exception

