import os

HOME = "/home/hongxwing/Workspace/HQLF_test"


class PathForWeb:

    def __init__(self, fullpath=None):
        if fullpath is None:
            fullpath = HOME
        self._fullpath = fullpath
        self._basename = os.path.basename(self._fullpath)
        self._pdir = os.path.dirname(self._fullpath)
        self._pdirs = self._pdir.split('/')[1:]

    @property
    def fullpath(self):
        return self._fullpath

    @property
    def basename(self):
        return self._basename

    @property
    def parent(self):
        return self._pdir

    @property
    def parent_list(self):
        return self._pdirs


class Project:

    def __init__(self, id, name=None, dir=None):
        if dir is None:
            dir = HOME
        self._id = id
        if name is None:
            name = 'Project %d' % self._id
        self._name = name
        self._cpath = os.path.abspath(dir)
        self._cdir = None
        self._cdirs = None
        self._cfiles = None
        self._update_path_info()

    def _update_path_info(self):
        self._cdir = PathForWeb(self._cpath)
        self._cdirs = []
        self._cfiles = []
        all_files = os.listdir(self._cpath)
        for f in all_files:
            fabs = os.path.join(self._cdir.fullpath, f)            
            if os.path.isdir(fabs):
                self._cdirs.append(PathForWeb(fabs))
            else:
                self._cfiles.append(PathForWeb(fabs))

    def upper(self):
        if self._cpath == HOME:
            return
        self._cpath = self._cdir.parent
        self._update_path_info()

    def enter(self, path):        
        self._cpath = path
        self._update_path_info()

    def refresh(self):
        self._update_path_info()

    @property
    def pdirs(self):
        return self._cdir.parent_list

    @property
    def cdir(self):
        return self._cdir

    @property
    def child_files(self):
        return self._cfiles

    @property
    def child_dirs(self):
        return self._cdirs

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id
