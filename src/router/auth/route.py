from typing import List
from http import HTTPMethod


from starlette.routing import Route
from starlette.requests import Request 
from starlette.responses import Response
from starlette_login.decorator import login_required
from starlette_wtf import csrf_protect

from src.form.forms import LoginForm

from .login_helper import login_helper
from .logout_helper import  logout_helper





@csrf_protect
async def login(request: Request)-> Response:
    form = await LoginForm.from_formdata(request)
    response = await login_helper(request, form) 
    return response



@login_required
async def logout(request: Request)-> Response:
    response = await logout_helper(request)
    return response



routes: List[Route] = [
    Route('/login', endpoint=login, methods=[HTTPMethod.GET, HTTPMethod.POST], name='login'),
    Route('/logout', endpoint=logout, methods=[HTTPMethod.GET], name='logout'),
]