from typing import List
import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm
from services import create_database
import services as _services
from schemas import UserCreate
 

app = _fastapi.FastAPI()

create_database()

@app.post("/api/users")
async def create_user(user: UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    my_db = await _services.get_user_by_email(user.email, db)
    if my_db:
        raise _fastapi.HTTPException(status_code = 400, detail = 'email already in use')
    return await _services.create_user(user, db)
