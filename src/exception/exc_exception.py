from typing import Dict
from starlette.requests import Request 


class ErrorException(Exception):
    """
    ErrorException display simple messages 
    to let users know an error has occured
    params:
        msg: massage to display 
        icon: awsome-fan icon
    """
    def __init__(self, msg:str=None, icon:str="fa-solid fa-circle-exclamation"):
        super().__init__(msg)
        self.msg = msg 
        self.icon = icon
    


class ActionException(Exception):
    """
    ActionException display simple messages 
    to let users know an action-error has occured
    params:
        name: name of the action or event
        msg: message to give insides of what the warning is about
        icon: awsome-fan icon 
    """
    def __init__(self, name:str, msg:str, icon:str="fa-solid fa-circle-exclamation"):
        super().__init__(msg)
        self.name = name
        self.msg = msg
        self.icon = icon




class WarningException(Exception):
    """
    WarningsException is the father of all wanngs 
    params: 
        title: header of the warning cart
        text: message to inform a user about the waring
        icon: awsome-fan  icon  
    
    """
    def __init__(self, title:str, text:str, icon:str="fa-solid fa-circle-exclamation"):
        super().__init__(text)
        self.title = title
        self.text = text
        self.icon = icon

    def __call__(request:Request)->None:
        request.state.session["_warnings"] = {"title": self.title, "text":self.text, "icon": self.icon}


    def get_warnings(self, request:Request):
        return request.session.pop("_warnings") if "_messages" in request.session else []





class LoginFaild(ErrorException):pass


