

from starlette.requests import Request
from starlette.responses import Response
from starlette import status



from src.settings import Template



async def main(request: Request)->Response:
    return Template.TemplateResponse(request, name='landin/index.html', context={}, status_code=status.HTTP_200_OK)



