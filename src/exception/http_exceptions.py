
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

from src.settings import Template 


async def ExceptionResponse(request:Request, exc:HTTPException)->Response:
    if isinstance(exc, HTTPException):
        return Template.TemplateResponse(request, name='error/error.html', context={'exc': exc}, status_code=exc.status_code)
    return Template.TemplateResponse(request, name='error/error.html', context={'exc': exc}, status_code=500)
    

async def not_found(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def bad_request(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def unauthorized(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def forbidden(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def method_not_allowed(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def not_acceptable(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def  Proxy_Authentication_Required(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def  Request_Timeout(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Conflict(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Gone(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Length_Required(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Precondition_Failed(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Payload_Too_Large(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def URI_Too_Long(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Unsupported_Media_Type(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Range_Not_Satisfiable(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Expectation_Failed(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def teapot(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Misdirected_Request(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Unprocessable_Content(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Locked(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Failed_Dependency(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Too_Early(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Upgrade_Required(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Precondition_Required(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Too_Many_Requests(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def Request_Header_Fields_Too_Large(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    
async def Unavailable_For_Legal_Reasons(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)
    

async def server_error(request: Request, exc: HTTPException)->Response:
        return await ExceptionResponse(request, exc)
    

async def Not_Implemented(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)


async def Bad_Gateway(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)


async def Service_Unavailable(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)


async def Gateway_Timeout(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)


async def HTTP_Version_Not_Supported(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)


async def Variant_Also_Negotiates(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)


async def Insufficient_Storage(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)


async def Loop_Detected(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)


async def Not_Extended(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)


async def Network_Authentication_Required(request: Request, exc: HTTPException)->Response:
    return await ExceptionResponse(request, exc)




exception_handlers = {
    400: bad_request,
    403: forbidden,
    404: not_found,
    405: method_not_allowed,
    406: not_acceptable,
    407: Proxy_Authentication_Required,
    408: Request_Timeout,
    409: Conflict,
    410: Gone,
    411: Length_Required, 
    412: Precondition_Failed,
    413: Payload_Too_Large,
    414: URI_Too_Long,
    415: Unsupported_Media_Type,
    416: Range_Not_Satisfiable,
    417: Expectation_Failed,
    418: teapot,
    421: Misdirected_Request,
    422: Unprocessable_Content,
    423: Locked,
    424: Failed_Dependency,
    425: Too_Early,
    426: Upgrade_Required,
    428: Precondition_Required,
    429: Too_Many_Requests,
    431: Request_Header_Fields_Too_Large,
    451: Unavailable_For_Legal_Reasons,
    500: server_error,
    501: Not_Implemented,
    502: Bad_Gateway,
    503: Service_Unavailable,
    504: Gateway_Timeout,
    505: HTTP_Version_Not_Supported,
    506: Variant_Also_Negotiates,
    507: Insufficient_Storage,
    508: Loop_Detected,
    510: Not_Extended,
    511: Network_Authentication_Required,

}
