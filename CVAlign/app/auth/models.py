import uuid
from sqlalchemy import Column, String, Enum as SqlEnum
from sqlalchemy.dialects.postgresql import UUID
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from app.database import Base
import enum

class RoleEnum(str, enum.Enum):
    recruiter = "recruiter"
    manager = "manager"
    admin = "admin"


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role = Column(SqlEnum(RoleEnum), default=RoleEnum.recruiter)
