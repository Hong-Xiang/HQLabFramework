import os
import mpld3
from IPython.display import HTML
from flask import render_template, flash, redirect, jsonify, url_for, request
from flask_login import login_required, current_user
from hqlf import app, oid
from hqlf.blueprints.login import login_pages
from hqlf.blueprints.project_list.views import project_list
from hqlf.blueprints.hqtem import hqteam

from hqlf.models.project import ProjectsList

import numpy as np

import matplotlib.pyplot as plt




app.register_blueprint(login_pages, url_prefix='/login')
app.register_blueprint(project_list, url_prefix='/project_list')
app.register_blueprint(hqteam, url_prefix='/hqteam')


@app.route("/showdir")
def showdir():
    return redirect(url_for('home'))

@app.route('/help', methods=['GET'])
def help():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = "{:50s} {:20s} {}".format(rule.endpoint, methods, url)
        output.append(line)    
    return jsonify(output)
    # return url_for('project_list.home')
    # endpoints = [rule.rule for rule in app.url_map.iter_rules()
    #              if rule.endpoint != 'static']
    # return jsonify(dict(api_endpoints=endpoints))


@app.route("/test")
def test_page():
    return render_template('l2.html', father='l1.html', name1='name1', name2='name2')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('login.html')

# @oid.after_login()


@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # return render_template('HQteam_1.html', username=current_user)    
    return render_template('main.html', projects=ProjectsList.projects)
    # return redirect(url_for('info'))
    # return render_template('project_list/project_list.html', username=current_user)


@app.route('/plottest')
def plottest():
    x = np.linspace(0, 3.1415926, 100)
    y = np.sin(x)
    fig = plt.figure()
    plt.plot(x, y)
    img = mpld3.fig_to_html(fig, template_type="simple")
    return img
    # return render_template('showpic.html', projects=projects, image_content=img)



