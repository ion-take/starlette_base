

from starlette_wtf import StarletteForm
from wtforms import PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

from src.database.connection import async_session
from src.exception.exc_exception import LoginFaild
from src.settings import Env




class LoginForm(StarletteForm):

    email: EmailField = EmailField('Email', validators=[DataRequired('missing field'), Email()])
    password: PasswordField = PasswordField('Password', validators=[DataRequired('missing field')])
    remember : BooleanField = BooleanField('Rember me')
    submit: SubmitField = SubmitField('Submit')

    async def async_validate_email(self, email):
        pass
