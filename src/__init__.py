
from starlette.applications import Starlette 

from starception import install_error_handler

from src.exception.http_exceptions import exception_handlers
from src.config.middleware_config import AppMiddleWare, login_manager, AppMiddleWareI18n
from src.database.storage import configure_storage
from src.router import RoutingTable
from src.admin import app as admin_app





def create_app():
    """ 
    create a Starlette app instance 
    """
    install_error_handler(editor='vscode')
    app: Starlette = Starlette(
        routes=RoutingTable,
        debug=True,
        middleware= AppMiddleWare,
        # exception_handlers = exception_handlers,
        on_startup=[configure_storage],
    )

    admin_app.create_admin(app)
    app.state.login_manager = login_manager
    return app