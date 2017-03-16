import os

CSRF_ENABLED = True
SECRET_KEY = 'F34TF$($e34D'
TEMPLATES_AUTO_RELOAD = True

BASE_DIR = os.path.abspath("D:\\hqlf\\database")

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'hqlf.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False