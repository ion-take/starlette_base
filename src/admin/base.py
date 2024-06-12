from typing import Optional, Sequence, Union, Any, Dict

from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from starlette.middleware import Middleware
from starlette.requests import Request

from starlette_admin.auth import BaseAuthProvider
from starlette_admin.contrib.sqla.middleware import DBSessionMiddleware
from starlette_admin.i18n import I18nConfig
from starlette_admin.i18n import lazy_gettext as _
from starlette_admin.views import CustomView
from starlette_admin.contrib.sqla import Admin
from starlette_admin.contrib.sqla import ModelView

from src.database.connection import async_engine






class AdminApp(Admin):
    def __init__(
        self,
        title: str = _("Admin"),
        base_url: str = "/admin",
        route_name: str = "admin",
        logo_url: Optional[str] = None,
        login_logo_url: Optional[str] = None,
        templates_dir: str = "templates",
        statics_dir: Optional[str] = None,
        index_view: Optional[CustomView] = None,
        auth_provider: Optional[BaseAuthProvider] = None,
        middlewares: Optional[Sequence[Middleware]] = None,
        debug: bool = False,
        i18n_config: Optional[I18nConfig] = None,
        favicon_url: Optional[str] = None,
    ) -> None:
        super().__init__(
            engine=async_engine,
            title=title,
            base_url=base_url,
            route_name=route_name,
            logo_url=logo_url,
            login_logo_url=login_logo_url,
            templates_dir=templates_dir,
            statics_dir=statics_dir,
            index_view=index_view,
            auth_provider=auth_provider,
            middlewares=middlewares,
            debug=debug,
            i18n_config=i18n_config,
            favicon_url=favicon_url,
        )




class BaseModelView(ModelView):
    
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        try:
            data = await self._arrange_data(request, data)
            await self.validate(request, data)
            session: Union[Session, AsyncSession] = request.state.session
            obj = await self._populate_obj(request, self.model(), data)
            session.add(obj)
            await self.before_create(request, data, obj)
            if isinstance(session, AsyncSession):
                await session.commit()
                # await session.refresh(obj)
            else:
                await anyio.to_thread.run_sync(session.commit)  # type: ignore[arg-type]
                await anyio.to_thread.run_sync(session.refresh, obj)  # type: ignore[arg-type]
            await self.after_create(request, obj)
            return obj
        except Exception as e:
            return self.handle_exception(e)

    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        try:
            data = await self._arrange_data(request, data, True)
            await self.validate(request, data)
            session: Union[Session, AsyncSession] = request.state.session
            obj = await self.find_by_pk(request, pk)
            await self._populate_obj(request, obj, data, True)
            session.add(obj)
            await self.before_edit(request, data, obj)
            if isinstance(session, AsyncSession):
                await session.commit()
                # await session.refresh(obj)
            else:
                await anyio.to_thread.run_sync(session.commit)  # type: ignore[arg-type]
                await anyio.to_thread.run_sync(session.refresh, obj)  # type: ignore[arg-type]
            await self.after_edit(request, obj)
            return obj
        except Exception as e:
            self.handle_exception(e)