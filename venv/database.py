import sqlalchemy as _sql
from sqlalchemy.orm import sessionmaker
import sqlalchemy.ext.declarative as _declarative

DATABASE_URL = 'sqlite:///./mydatabase.db'

engine = _sql.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker( autoflush = True,bind=engine)

Base = _declarative.declarative_base()
