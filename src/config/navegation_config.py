

from typing import Union

from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.datastructures import URL 

from .base import  BaseLink, DropDown

class HomeLink(BaseLink):
    def __init__(self):
        super().__init__(lable='Home', icon="fa-solid fa-home")

    def url(self, request:Request)->Union[URL, str]:
        return request.url_for('landin:landin')
    

class LoginLink(BaseLink):
    def __init__(self):
        super().__init__(lable="Login", icon="fa fa-lock")
    
    def url(self, request: Request)-> Union[URL, str]:
        return request.url_for("auth:login")
    
    def is_accessable(self, request:Request)-> bool:
        return (request.user.is_authenticated == False)
    
    def is_active(self, request:Request)-> bool:
        return (request.user.is_authenticated == False)



class LogoutLink(BaseLink):
    def __init__(self):
        super().__init__(lable="LOG-OUT", icon="fa fa-exit")
    
    def url(self, request: Request)->Union[URL, str]:
        return request.url_for("auth:logout")
    
    def is_accessable(self, request:Request)->bool:
        return request.user.is_authenticated
    
    def is_active(self, request:Request)->bool:
        return request.user.is_authenticated


class AdminLink(BaseLink):
    def __init__(self):
        super().__init__(lable="Admin", icon="fa-solid fa-user-tie")

    def url(self, request: Request)->Union[URL, str]:
        return request.url_for("admin:index")
    
    def is_accessable(self, request:Request)->bool:
        return (request.user.is_authenticated and request.user.role.is_admin)
    
    def is_active(self, request:Request)->bool:
        self.icon
        return (request.user.is_authenticated and request.user.role.is_admin)






def set_template_navegation_links(template: Jinja2Templates)-> None:

    template.env.globals["home_link"] = HomeLink()
    template.env.globals["login_link"] = LoginLink()

