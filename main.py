from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask_bootstrap import Bootstrap
import os
import subprocess
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpld3
from IPython.display import HTML
import random
from flask import request
from HQLabFramework.apps.project import Project


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)
# app.config['SECRET_KEY'] = 'F34TF$($e34D'

projects = []

@app.route("/showdir")
def showdir():
    files = os.listdir(".")
    path_now = os.getcwd()
    return path_now

@app.route("/test")
def test_page():
    return "TestPage"

@app.route("/add_project", methods=['GET', 'POST'])
def add_project():
    project_name = request.args.get("project_name")
    projects.append(Project(id=random.randint(0, 1000), name=project_name))    
    return render_template('main.html', projects=projects)

@app.route("/project_enter_folder", methods=['GET', 'POST'])
def project_enter_folder():
    project_id = int(request.args.get("proj_id"))
    path_target = request.args.get("path")
    for p in projects:        
        if p.id == project_id:            
            p.enter(path_target)
    return render_template('main.html', projects=projects)

@app.route("/project_upper", methods=['GET', 'POST'])
def project_upper():
    project_id = int(request.args.get("proj_id"))
    for p in projects:        
        if p.id == project_id:                     
            p.upper()
    return render_template('main.html', projects=projects)

@app.route("/open_file", methods=['GET'])
def open_file():
    filename = request.args.get("path")    
    with open(filename) as fin:
        str = fin.read()
    return render_template('main.html', projects=projects, textfile=str)
@app.route('/')
def home():
    # return render_template('index.html')
    
    # path_now = os.getcwd()
    # cdir = os.path.basename(path_now)
    # pdir = os.path.dirname(path_now)
    # pdirs = pdir.split('/')
    # pdirs = pdirs[1:]
    return render_template('main.html', projects=projects)
    # return render_template('dashborad.html')


@app.route('/plottest')
def plottest():
    x = np.linspace(0, 3.1415926, 100)
    y = np.sin(x)
    fig = plt.figure()
    plt.plot(x, y)
    return mpld3.fig_to_html(fig)


@app.route('/add/<filename>')
def run(filename=None):
    subprocess.call(['python3', 'test2.py', filename])
    return "file added."
# @app.route('/signup', methods=['POST'])
# def signup():
#     session['username'] = request.form['username']
#     session['message'] = request.form['message']
#     return redirect(url_for('message'))

# @app.route('/message')
# def message():
#     if not username in session:
#         return abort(403)
#     return render_template('message.html', username=session['username'],
#                                            message=session['message'])

if __name__ == '__main__':
    app.run(host="0.0.0.0")
