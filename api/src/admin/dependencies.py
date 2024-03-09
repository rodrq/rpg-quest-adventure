from src.character.models import Character
from fastapi import Depends, HTTPException, status
from src.character.schemas import UserRoleEnum
from src.character.dependencies import get_current_character

def get_current_admin_user(current_user: Character = Depends(get_current_character)):
    if current_user.role != UserRoleEnum.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access to this resource",
        )
    return current_user