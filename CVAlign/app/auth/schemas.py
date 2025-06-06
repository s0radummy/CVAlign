from fastapi_users import schemas
from app.auth.models import RoleEnum
import uuid
from typing import Optional

class UserRead(schemas.BaseUser[uuid.UUID]):
    role: RoleEnum

class UserCreate(schemas.BaseUserCreate):
    role: RoleEnum

class UserUpdate(schemas.BaseUserUpdate):
    role: Optional[RoleEnum] = None
