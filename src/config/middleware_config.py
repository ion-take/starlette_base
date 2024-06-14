




from sqlalchemy import select 
from sqlalchemy.orm import selectinload

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_login.backends import SessionAuthBackend
from starlette_login.login_manager import LoginManager
from starlette_login.middleware import AuthenticationMiddleware
from starlette_wtf import CSRFProtectMiddleware


from src.database.connection import async_session
from src.database.user_loader import user_loader
from src.settings import Env    
from src.flash import messages



login_manager = LoginManager(redirect_to='/auth/login', secret_key=str(Env.LOGIN_SECRET_KEY))
login_manager.set_user_loader(user_loader)



class DBSessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp ) -> None:
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        async with (async_session(Env.DB_ADMINISTRATION_NAME)).begin() as session:
            request.state.session = session
            return await call_next(request)



class UrlAnalizerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
            super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """ here goes the logics """
        
        return await call_next(request)







AppMiddleWare = [
    Middleware(SessionMiddleware, secret_key=Env.SESSION_SECRET_KEY),
    Middleware(CSRFProtectMiddleware, csrf_secret=Env.CSRF_SECTET_KEY),
    Middleware(
        AuthenticationMiddleware,
        backend=SessionAuthBackend(login_manager),
        login_manager=login_manager,
        allow_websocket=False,
    ),
    Middleware(DBSessionMiddleware),
]


# add translatetor middelwares 
AppMiddleWareI18n = AppMiddleWare.extend([])