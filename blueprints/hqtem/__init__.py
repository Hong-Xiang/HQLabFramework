import os
from flask import Blueprint
from flask import redirect, request, render_template

hqteam = Blueprint('hqteam', __name__, template_folder='templates')

from . import views
