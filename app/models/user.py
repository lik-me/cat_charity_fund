from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from pydantic import Extra

# from app.core.db import Base
from app.core.db import BaseUser

class User(SQLAlchemyBaseUserTable[int], BaseUser):
# class User(SQLAlchemyBaseUserTable[int], Base):
    pass
