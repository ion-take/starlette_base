

from typing import Any, Union

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from starlette.requests import Request
from starlette.responses import Response, RedirectResponse
from starlette import status 
from starlette_admin.auth import AdminConfig, AdminUser, AuthProvider
from starlette_admin.exceptions import FormValidationError, LoginFailed

from src.database.serializer import UserSchema 
from src.database.model import User
from src.flash import messages




class UserProvider(AuthProvider):
    """
    This is only for demo purpose, it's not a better
    way to save and validate user credentials
    """

    async def login(
        self, email: str, password: str,
        remember_me: bool,
        request: Request,response: Response,
        ) -> Response:
        
        # if request.user.is_authenticated and request.user.role.is_admin:
            
        #     user = await self.login_admin_user(request, email=email, pwd=password)
        #     if user : 
        #         request.session.update({"user": user})
        #         return response
        #     raise LoginFailed("Invalid email or password")
        
        # await messages(request, category="danger", msg="You Must be a Authorized user", icon="fa-solid fa-circle-exclamation fa-beat")
        
        return await send_to_home(request)
        

    async def is_authenticated(self, request) -> bool:
        user = request.session.get("user", None) 
        """
        Save current `user` object in the request state. Can be used later
        to restrict access to connected user.
        """
        
        # if user:
        #     request.state.user = user
        #     return user["role"]["is_admin"]

        return True


    def get_admin_config(self, request: Request) -> AdminConfig:
        user = {}
        # # user = request.state.user   Retrieve current user
        # # # Update app title according to current_user
        custom_app_title = "Hello, " + user.get('name', '') + "!"
        # # # Update logo url according to current_user
        custom_logo_url = None
        # # if user['company'].get("logo_url", None):
        # #     custom_logo_url = request.url_for("admin:api:file", storage="avatar", file_id=user['company']["logo_url"])
        return AdminConfig(
            app_title=custom_app_title,
            logo_url=custom_logo_url,
        )


    def get_admin_user(self, request: Request) -> AdminUser:
        # user = request.state.user  # Retrieve current user
        user = {}
        photo_url = None
        # if user.get("avatar", None) is not None:
        #     photo_url = request.url_for("admin:api:file", storage="avatar", file_id=user["avatar"])
        return AdminUser(username=user.get("name", None), photo_url=photo_url)


    async def logout(self, request: Request, response: Response) -> Response:
        request.session.pop('user')
        return await send_to_home(request)


    async def login_admin_user(self, request:Request, email:str, pwd:str)-> Union[User, bool]:
        """
        Implement the user login system here

        return UserSchema instance
        """
        return False




