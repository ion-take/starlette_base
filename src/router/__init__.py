from typing import List, Union 
from starlette.routing import Route, Mount


RoutingTable: List[Union[Route, Mount]] = []



