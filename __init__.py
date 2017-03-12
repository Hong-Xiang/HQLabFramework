""" Entry of HQLF """
import os
import matplotlib
matplotlib.use('agg')
from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID

from hqlf import config

app = Flask(__name__)
app.config.from_object(config)

lm = LoginManager()
lm.setup_app(app)
oid = OpenID(app, os.path.join(config.BASE_DIR, 'oidtmp'))
Bootstrap(app)
db = SQLAlchemy(app)

import hqlf.views




