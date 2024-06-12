
from starlette.applications import Starlette
from starlette_admin.views import Link
from starlette_admin.i18n import lazy_gettext as _

from .base import AdminApp
from .form import admin_modelviews
from .auth import UserProvider

from src.settings import get_resouces_location
from src.config.middleware_config import AppMiddleWare


def create_admin(app: Starlette):
    """
    This func Initialize a admin-app instance
    """
    admin = AdminApp(
        title = _("Admin"),
        base_url = "/admin",
        route_name = "admin",
        logo_url = None,
        login_logo_url = None,
        templates_dir = get_resouces_location('src/views/admin'),
        auth_provider=UserProvider(),
        debug=True,
        middlewares=AppMiddleWare,
    )
    admin.add_view(Link(label="Home Page", icon="fa fa-home", url="/admin"))

    admin_modelviews(admin)
    admin.mount_to(app)



