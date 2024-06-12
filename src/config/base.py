from typing import Dict, Union, List
from abc import ABC, abstractmethod

from starlette.requests import Request 
from starlette.datastructures import URL


class BaseModel(ABC):

    @abstractmethod
    def is_active(self, request:Request)-> bool:
        ...

    @abstractmethod
    def is_accessable(self, request:Request)-> bool:
        ...




class BaseLink(BaseModel):
    style:str="style-nav-item"

    def __init__(self, lable:str , icon:str):
        self.lable = lable
        self.icon = icon
        
    def is_accessable(self, request:Request)-> bool:
        return True

    def is_active(self, request:Request)-> bool:
        return True

    @abstractmethod
    def url(request:Request,  **kwargs:Dict) -> Union[URL, str]:
        ...




class DropDown(BaseModel):

    def __init__(self, lable:str=None, icon:str=None, links: List[BaseLink]=None):
        assert links is not None, "links cant be none"
        assert lable is not None, "lable cant be None"

        self.lable = lable 
        self.icon = icon
        self.links = [link for link in links if isinstance(link ,BaseLink)]
        
    def is_accessable(self, request:Request)->bool:
        return any(L.is_accessable(request) for L in self.links )
    
    def is_active(self, request:Request)->bool:
        return any(L.is_active(request) for L in self.links )
