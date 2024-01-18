import sqlalchemy.orm as _orm
import passlib.hash as _hash
from schemas import UserCreate
from database import engine, Base, SessionLocal
import models as _models
import logging  # Import the logging module
import schemas as _schemas
import jwt as _jwt
import fastapi.security as _security
import fastapi as _fastapi
# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG

oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/api/token")

JWT_SECRET = "myjwtsecret"

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


async def authenticate_user(email: str, password: str, db: _orm.Session):
    try:
        user = await get_user_by_email(db=db, email=email)

        if not user:
            return False

        if not user.verify_password(password):
            return False

        return user
    except  Exception as e:
        logging.error('Error while authenticarting user: %s', str(e))
        raise e


async def create_token(user: _models.User):
    try:
        user_obj = _schemas.User.from_orm(user)

        token = _jwt.encode(user_obj.model_dump(), JWT_SECRET)

        return dict(access_token=token, token_type="bearer")
    except  Exception as e:
        logging.error('Error while authenticarting user: %s', str(e))
        raise e
    

async def get_current_user(
    db: _orm.Session = _fastapi.Depends(get_db),
    token: str = _fastapi.Depends(oauth2schema),
):
    try:
        payload = _jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = db.query(_models.User).get(payload["id"])
    except:
        raise _fastapi.HTTPException(
            status_code=401, detail="Invalid Email or Password"
        )

    return _schemas.User.from_orm(user)
