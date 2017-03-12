from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    username = TextField('username', validators = [Required()])
    password = PasswordField('password', validators=[Required()])
    # remember_me = BooleanField('remember_me', default = False)