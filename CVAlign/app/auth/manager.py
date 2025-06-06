from fastapi import Depends
from fastapi_users.manager import BaseUserManager, UUIDIDMixin
from app.auth.models import User
from app.database import SessionLocal
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
import uuid
import os

SECRET = os.getenv("SECRET")

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    user_db_model = User

    async def on_after_register(self, user: User, request=None):
        print(f"User {user.id} has registered.")

async def get_user_db():
    db = SessionLocal()
    yield SQLAlchemyUserDatabase(User, db)
async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
