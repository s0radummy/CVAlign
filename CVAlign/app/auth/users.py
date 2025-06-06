from fastapi_users import FastAPIUsers
from app.auth.models import User
from app.auth.schemas import UserRead, UserCreate, UserUpdate
from app.auth.manager import get_user_manager, auth_backend
import uuid

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)
