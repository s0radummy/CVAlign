import uuid
import enum
from typing import Optional

from sqlalchemy import String, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from fastapi_users import schemas

from app.database import Base

class RoleEnum(str, enum.Enum):
    recruiter = "recruiter"
    manager = "manager"
    admin = "admin"

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    role: Mapped[RoleEnum] = mapped_column(SqlEnum(RoleEnum), default=RoleEnum.recruiter)

class UserRead(schemas.BaseUser[uuid.UUID]):
    role: RoleEnum


class UserCreate(schemas.BaseUserCreate):
    role: RoleEnum


class UserUpdate(schemas.BaseUserUpdate):
    role: Optional[RoleEnum]
