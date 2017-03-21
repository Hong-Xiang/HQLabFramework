import os
import subprocess

from flask import Blueprint, render_template, abort, request, redirect, url_for
from flask_login import login_required, current_user
from hqlf.models.project import Project, HOME

from hqlf.blueprints.dlws import dlws

@dlws.route('/')
def home():
    render_template('dlws/base.html')

@dlws.route('/show_pic')
def show_pic():
    filename = request.args.get('filename')
    subprocess.call(['ln', '-s', './routines/create_test_file.py', filename])


