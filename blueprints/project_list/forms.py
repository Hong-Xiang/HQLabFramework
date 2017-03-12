from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required


class NewProject(FlaskForm):
    project_name = TextField('project_name', validators=[Required()])
