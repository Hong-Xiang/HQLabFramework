import os
import subprocess

from flask import Blueprint, render_template, abort, request, redirect, url_for
from flask_login import login_required, current_user
from hqlf.models.project import Project, HOME

dlws = Blueprint('dlws', __name__, template_folder='templates')

from . import views