
from starlette.applications import Starlette 

from src.exception.http_exceptions import exception_handlers
from src.config.middleware_config import AppMiddleWare, login_manager
from src.database.storage import configure_storage
from src.router import RoutingTable


def create_app():
    """ 
    create a Starlette app instance 
    """
    app: Starlette = Starlette(
        routes=RoutingTable,
        debug=True,
        middleware= AppMiddleWare,
        exception_handlers = exception_handlers,
        on_startup=[configure_storage],
    )

    app.state.login_manager = login_manager
    return app