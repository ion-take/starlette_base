from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from .model import User



class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User



