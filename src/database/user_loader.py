
from starlette.requests import Request

from .model import User
from .connection import async_session
from src.settings import Env



async def user_loader(request: Request, user_id: int)->User:
    async with (async_session(Env.DB_ADMINISTRATION_NAME)).begin() as session:
        user = await session.get(User, user_id)
        return user 