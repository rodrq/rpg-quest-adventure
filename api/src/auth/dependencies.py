from src.auth.schemas import UserForm
from src.auth import service
from src.auth.exceptions import UsernameTaken



async def valid_username_create(user: UserForm):
    if await service.get_user_by_username(user.username):
        raise UsernameTaken
    return user

