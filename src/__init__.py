
from starlette.applications import Starlette 



def create_app():
    """ 
    create a Starlette app instance 
    """
    app: Starlette = Starlette(

    ) 

    return app