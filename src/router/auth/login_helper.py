from http import HTTPMethod
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select 


from starlette.requests import Request 
from starlette.responses import Response, RedirectResponse
from starlette import status
from starlette_login.utils import login_user
from starlette_wtf import StarletteForm


from src.database.model import User

from src.exception.exc_exception import LoginFaild
from src.flash import messages
from src.settings import Template



# login helpers 

async def login_helper(request:Request, form:StarletteForm )-> Response:
    if request.method == HTTPMethod.POST and (await form.validate_on_submit()):
        
        try:
            user = await authenticate_user(request.state.session, form.email.data)
            return RedirectResponse(url = request.url_for('welcome:say-hello'), status_code=status.HTTP_303_SEE_OTHER)
        
        except LoginFaild as error:
            return Template.TemplateResponse(request, name='auth/index.html', context={'error': error, 'form': form},status_code=status.HTTP_401_UNAUTHORIZED)   
    
    return Template.TemplateResponse(request, name='auth/index.html', context={'form': form}, status_code=status.HTTP_200_OK)





async def authenticate_user(session, name:str):
    user = None
    if user:
        return user 
    raise LoginFaild(msg=f'no user with name {name}')


