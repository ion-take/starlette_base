

from starlette.requests import Request 
from starlette.responses import Response 
from starlette.routing import Route 

from . import landin_helper



async def landin(request: Request)-> Response:
    response = await landin_helper.main(request)
    return response




routes = [
    Route('/', endpoint=landin, name='landin'),
    
]