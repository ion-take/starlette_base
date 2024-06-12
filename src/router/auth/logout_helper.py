from http import HTTPMethod

from typing import Any

from sqlalchemy import select 

from starlette.routing import Route
from starlette.requests import Request 
from starlette.responses import Response, RedirectResponse
from starlette import status

from starlette_login.utils import login_user, logout_user

from src.database.model import User




#  logout helpers 
async def logout_helper(request:Request)->Response:


    await logout_user(request)
    url = request.url_for('landin:landin')
    request.session.clear()
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

