

from typing import List
from http import HTTPMethod

from starlette.requests import Request 
from starlette.responses import Response 
from starlette.routing import Route

from .storage_helper import _serve_file




async def storage(request: Request)-> Response:
    """
    store meda file like [ img, video ]
    """
    response = _serve_file(request)
    return response




routes: List[Route] = [
    Route('/media/{storage}/{file_id}', endpoint=storage, methods=[HTTPMethod.GET], name='file.api')
]

