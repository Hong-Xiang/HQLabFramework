import os
from flask import Blueprint
from flask import redirect, request, render_template

login_pages = Blueprint('login_pages', __name__, template_folder='templates')

from . import views
