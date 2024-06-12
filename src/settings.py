


import os 
import os.path

from pathlib import Path
from secrets import token_hex


from starlette.config import Config
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.datastructures import Secret, CommaSeparatedStrings
from starlette.status import HTTP_200_OK

from src.config import navegation_config, template_config

# setting the configurations variables 

class Env:
    """ APP config """
    config = Config('.env')

    DB_ADMINISTRATION_NAME = config('DB_ADMINISTRATION_NAME', cast=str, default='administration')
    
    USE_SQLITE= config('USE_SQLITE', cast=bool, default=False)
    SQLITE_DB_URI = config('SQLITE_DB_URI', cast=str ,default=False)

    USE_MYSQL = config('USE_MYSQL', cast=bool, default=False)
    MYSQL_DB_URI = config('MYSQL_DB_URI', cast=str, default=False)

    USE_POSTGRESS = config('USE_POSTGRESS', cast=bool, default=False)
    POSGRESS_URI = config('POSGRESS_URI', cast=str, default=False)

    USE_EXTENAL_BUCKET = config('USER_EXTENAL_BUCKET', cast=bool, default=False)


    ADMIN_NAME = config('ADMIN_NAME', cast=str , default='ADMIN')
    ADMIN_LEVEL= config('ADMIN_LEVEL', cast=int, default=1)

    ADMIN_SECUNDARY_NAME = config('ADMIN_SECUNDARY_NAME', cast=str, default='ADMIN_SECUNDARY')
    ADMIN_SECONDARY_LEVEL = config('ADMIN_SECONDARY_LEVEL', cast=int, default=2)

    DISPACHER_NAME= config('DISPACHER_NAME', cast=str, default='DISPACHER')

    SELLER_NAME = config('SELLER_NAME', cast=str, default='SELLER')

    TRANSPORT_NAME = config('TRANSPORT_NAME', cast=str, default='TRANSPORT')
   
    LOGIN_SECRET_KEY = config('LOGIN_SECRET_KEY', cast=Secret, default=token_hex(64))

    ADMIN_SECRET_KEY = config('ADMIN_SECRET_KEY', cast=Secret, default=token_hex(64))
    
    CSRF_SECTET_KEY = config('CSRF_SECTET_KEY', cast=Secret, default=token_hex(64))

    SESSION_SECRET_KEY = config('SESSION_SECRET_KEY', cast=Secret, default=token_hex(64))

    INVALID_URLS = config('ILIGAL_URL_CATARCTER', cast=CommaSeparatedStrings, default='/., /.., /.env')
    
    UPLOAD_DIR = config('UPLOAD_DIR', cast=str, default='upload/')




def get_resouces_location(*name):
    """
    This func creates a comunication between the app and the static resources.
    
    args:
        obj (object) : object to generate a path for.
        name (str) : name of the end file directory.

    params:
        location_str (callable) : generate the path to a certain resouse.
    """
    parent_path = Path(os.path.dirname(__file__)).resolve().parents[0]

    location_str = os.path.join(parent_path, *name)
    return str(location_str)




def create_template()-> None:
    """ 
    genarating a jinja2 template object
    """
    template: Jinja2Templates = Jinja2Templates(directory=get_resouces_location('src', 'views'))

    template_config.set_template_filters(template)
    template_config.set_template_globals(template)
    navegation_config.set_template_navegation_links(template)
    
    return template



Template = create_template()
Static = StaticFiles(directory=get_resouces_location('src', 'static'), packages=['starlette_admin'])