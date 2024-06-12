from starlette.templating import Jinja2Templates


# Globals functions

def say_hello(name:str)-> str:
    """
    Say hello a new user
    """
    return f'hellow {name}'


# def Image(container:str, file_id:str):


# Filters functions




def set_template_globals(template: Jinja2Templates)-> None:
    
    template.env.globals['say_hello'] = say_hello
    



def set_template_filters(template: Jinja2Templates)-> None:
    
    template.env.filters['alive'] = lambda x : x if x else False 