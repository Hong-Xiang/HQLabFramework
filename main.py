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

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)
# app.config['SECRET_KEY'] = 'F34TF$($e34D'



@app.route("/showdir")
def showdir():
    files = os.listdir(".")
    return r"<br>".join(files)

@app.route("/test")
def test_page():
    return "TestPage"

@app.route('/')
def home():
    # return render_template('index.html')
    return render_template('main.html')
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
