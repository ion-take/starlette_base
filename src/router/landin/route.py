

from starlette.requests import Request 
from starlette.responses import Response 


from . import landin_helper




async def landin(request: Request)-> Response:
    response = await landin_helper.main(request)
    return response