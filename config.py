import os

CSRF_ENABLED = True
SECRET_KEY = 'F34TF$($e34D'
TEMPLATES_AUTO_RELOAD = True

WORK_ROOT = os.environ.get('PATH_HQLF_WORKROOT')
BASE_DIR = os.path.join(os.environ.get('PATH_HQLF'), "database")

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'hqlf.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False