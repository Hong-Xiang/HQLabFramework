from pathlib import Path
from flask_restful import Resource
from flask import request
import shutil


class Directory:
    def __init__(self, path):
        self.path = Path(path)

    def mkdir(self, parents=False):
        self.check(False)
        self.path.mkdir(parents=parents)
        return self.pwd()

    def delete(self):
        self.check()        
        parent = self.exit()
        shutil.rmtree(self.path)
        return parent

    def rename(self, path_new):
        self.check()
        path_new = Directory(path_new)
        path_new.check(False)
        self.path.rename(path_new.path)
        self.path = path_new.path
        return self.pwd()

    def pwd(self):
        self.check()
        return str(self.path.absolute())

    def check(self, exists=True):
        if self.path is None:
            raise ValueError("Path can not be None.")
        if exists:
            if not self.path.exists():
                raise FileNotFoundError(self.path)
            if not self.path.is_dir():
                raise NotADirectoryError(self.path)                
        else:
            if self.path.exists():
                raise FileExistsError(self.path)
        return True

    def show(self, reg=None):
        self.check()
        reg = reg or '*'
        paths = [str(p.absolute()) for p in self.path.glob(reg)]
        return paths

    def info(self, reg=None):
        self.check()
        reg = reg or '*'
        paths = [p for p in self.path.glob(reg)]
        infos = [(p.is_dir() and 'D') or (p.is_file() and 'F') for p in paths]
        paths = [str(p.absolute()) for p in paths]
        return {'paths': paths, 'infos': infos}

    def enter(self, target):
        self.check()
        path_new = self.path / target
        nwd = Directory(path_new)
        nwd.check()
        return nwd.pwd()

    def exit(self):
        self.check()
        ppwd = Directory(self.path.parent)
        return ppwd.pwd()


def error_handle(err):
    if isinstance(err, FileNotFoundError):
        return {'ERROR': "File or directory {err} not exist.".format(err=err)}, 404
    elif isinstance(err, NotADirectoryError):
        return {'ERROR': "{err} is not a directory .".format(err=err)}, 409
    elif isinstance(err, ValueError):
        if str(err) == "Path can not be None.":
            return {'ERROR': 'Directory path not specified.'}, 400
        else:
            return {'ERROR': str(err)}
    elif isinstance(err, FileExistsError):
        return {'ERROR': 'File {err} exists.'.format(err=err)}, 409
    else:
        raise err

class DirectoryAPI(Resource):
    def get(self):
        path = request.form.get('path')
        task = request.form.get('task', 'pwd')
        args = request.form.get('args')
        pwd = Directory(path)
        try:
            pwd.check()
            if task == 'pwd':
                result = pwd.pwd()
            elif task == 'show':
                result = pwd.show(args)
            elif task == 'info':
                result = pwd.info(args)
            elif task == 'enter':
                result = pwd.enter(args)
            elif task == 'exit':
                result = pwd.exit()
            return {'OK': result}
        except Exception as err:
            return error_handle(err)

    def put(self):
        path = request.form.get('path')
        args = request.form.get('args')
        pwd = Directory(path)
        try:
            result = pwd.rename(args)
            return {'OK': result}
        except Exception as err:
            return error_handle(err)

    def post(self):
        path = request.form.get('path')
        args = request.form.get('args')
        pwd = Directory(path)
        try:
            result = pwd.mkdir(args)
            return {'OK': result}, 201
        except Exception as err:
            return error_handle(err)

    def delete(self):
        path = request.form.get('path')
        pwd = Directory(path)
        try:
            result = pwd.delete()
            return {'OK': result}
        except Exception as err:
            return error_handle(err)
