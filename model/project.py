from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/hongxwing/Workspace/hqlf/hqlf/database/projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Project:    
    def __init__(self, path):
        self.root = Path(path)
        self.pwd = self.root



    
    


    

    

    


class ProjectInDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(512))

    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return '<Project {id} on {path}>'.format(id=self.id, path=self.path)

class ProjectDB:
    @classmethod
    def add(cls, path_project):
        path = Path(path_project)    
        pj = ProjectInDB(str(path.absolute()))
        db.session.add(pj)
        db.session.commit()
        return pj.id

    @classmethod
    def delete(cls, pid):
        pj = ProjectInDB.query.get(pid)
        if pj:
            db.session.delete(pj)
            db.session.commit()

    @classmethod
    def get_path(cls, pid):
        pj = ProjectInDB.query.get(pid)
        if pj:
            return pj.path
        else:
            return None

    @classmethod
    def update(cls, pid, path_new):
        path_new = str(Path(path_new).absolute())
        pj = ProjectInDB.query.get(pid)
        if pj:
            pj.path = path_new
            db.session.commit()
        else:
            raise ValueError("Pid {id} not found in database.".format(pid))

    @classmethod
    def get_ids(cls, path_project):
        path_project = str(Path(path_project).absolute())
        pids = ProjectInDB.query.filter_by(path=path_project).all()
        if not isinstance(pids, (list, tuple)):
            pids = [pids]
        return pids

