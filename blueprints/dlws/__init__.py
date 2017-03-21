from flask import Blueprint, render_template, abort, request, redirect, url_for

dlws = Blueprint('dlws', __name__, template_folder='templates')

from . import views