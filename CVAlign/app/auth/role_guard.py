from fastapi import Depends, HTTPException, status
from app.auth.users import current_active_user
from app.models.user import RoleEnum, User

def require_role(role: RoleEnum):
    def checker(user: User = Depends(current_active_user)):
        if user.role != role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        return user
    return checker
