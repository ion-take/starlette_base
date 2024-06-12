"""
    Flashes are messages pass to the template
    to display some message
    example:

        flash.async_messages(request, 'danger', 'this is a flash', 'warning')
        await flash.messages(request, 'danger', 'this is a flash', 'warning')
"""

from starlette.requests import Request
from starlette.templating import Jinja2Templates





def sync_messages(request:Request, category:str, msg:str, icon:str)->None:

    """ 
    Set a sync notificaton  on the request so the template displays it 
        params:
            request: current server request object
            category: category name used for css/boostrap
            msg: message to display on the screem 
    """
    if "_messages" not in request.session:
        request.session.update({"_messages":[]})
    request.session['_messages'].append({"category":category, "msg":msg, "icon":icon})
    
    


async def messages(request:Request, category:str, msg:str, icon:str)->None:
    """ 
    Set an async notificaton  on the request so the template displays it  
        params:
            request: current server request object
            category: category name used for css/boostrap
            msg: message to display on the screem 
    """

    if "_messages" not in request.session:
        request.session.update({"_messages":[]})
    request.session['_messages'].append({"category":category, "msg":msg, "icon":icon})
    


def get_masseges(request:Request):
    """ 
    Delete and GeT all notification from _messages 
    """
    return request.session.pop("_messages") if "_messages" in request.session else []







def set_template_flash_messages(temmplate: Jinja2Templates):
    """
    Add functionality to the template so it can be used 
    
    """
    template.env.globals['get_messages'] = get_masseges