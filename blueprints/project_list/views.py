import os
import subprocess

from flask import Blueprint, render_template, abort, request, redirect, url_for
from flask_login import login_required, current_user
from hqlf.models.project import Project, ProjectsList, HOME

project_list = Blueprint('project_list', __name__, template_folder='templates')


@project_list.route("/remove")
def remove_project():
    project_id = int(request.args.get("proj_id"))
    print("Removing project id = %d"%project_id)
    ProjectsList.remove(project_id)
    return redirect(url_for('home'))

@project_list.route("/add", methods=['GET', 'POST'])
def add_project():    
    project_name = request.args.get("project_name")
    print('Adding project {0} by user {1}'.format(project_name, current_user.username))
    usr_id = current_user.get_id()    
    ProjectsList.add(Project(usr_id=usr_id, name=project_name))
    # return render_template('project_list/explorers.html', projects=projects)
    return redirect(url_for('home'))


@project_list.route("/enter_folder", methods=['GET', 'POST'])
def enter_folder():
    project_id = int(request.args.get("proj_id"))
    path_target = request.args.get("path")
    for p in ProjectsList.projects:
        if p.id == project_id:
            p.enter(path_target)
    return redirect(url_for('home'))


@project_list.route("/upper", methods=['GET', 'POST'])
def upper():
    project_id = int(request.args.get("proj_id"))
    for p in ProjectsList.projects:
        if p.id == project_id:
            p.upper()
    return redirect(url_for('home'))


@project_list.route("/refresh", methods=['GET', 'POST'])
def refresh():
    project_id = int(request.args.get("proj_id"))
    for p in ProjectsList.projects:
        if p.id == project_id:
            p.refresh()
    return redirect(url_for('home'))


@project_list.route("/open_file", methods=['GET'])
def open_file():
    filename = request.args.get("path")
    with open(filename) as fin:
        str = fin.read()
    return redirect(url_for('home'))


@project_list.route('/add_file', methods=['GET'])
def add_file(project_name=None):
    file_name = request.args.get("add_file_name")
    file_path = os.path.join(HOME, file_name)
    print(file_path)
    subprocess.call(['python', './routines/create_test_file.py', file_path])

    return redirect(url_for('home'))
