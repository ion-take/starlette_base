
from .base import BaseModelView
from src.database import model 




class UserModelView(BaseModelView):
    pass




def admin_modelviews(admin):
    """
    This func add model view to the admin 
    site

    """
    admin.add_view(UserModelView(model.User))