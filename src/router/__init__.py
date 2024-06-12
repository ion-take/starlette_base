from typing import List, Union 
from starlette.routing import Route, Mount

from src.settings import Static

from .landin.route import routes as landin_routes
from .storage.route import routes as storage_routes
from .auth.route import routes as auth_routes




RoutingTable: List[Union[Route, Mount]] = [
    Mount('/static', app=Static, name='static'),
    Mount('/auth', routes=auth_routes, name='auth'),
    Mount('/storage', routes=storage_routes, name='storage'),
    Mount('/dash', routes=landin_routes, name='landin'),
]


