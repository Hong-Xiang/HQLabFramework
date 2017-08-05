import json
from pathlib import Path
from hqlf.config import 

PROJECT_MANAGER_CONFIG_FILE = None
PROJECT_CONIFG_FILE_NAME = 'project_config.json'

def __get_next_pid():
    if PROJECT_MANAGER_CONFIG_FILE is None:
        raise FileNotFoundError("Project config file is None.")
    with open(PROJECT_MANAGER_CONFIG_FILE, 'r') as fin:
        project_manager_configs = json.load(PROJECT_MANAGER_CONFIG_FILE)
    return project_manager_configs['max_pid'] + 1

class ProjectManager:
    def 

class Project:
    def Project(self, proj_path, proj_config_filename=None):
        self._path = Path(proj_path)
        self._config_file = str((self._path / (proj_config_filename or PROJECT_CONIFG_FILE_NAME)).absolute())
        self._configs = 
    @property
    def path():
        return str(self._path.absolute())

    @property
    def configs():
        with open(self._config_file.absolute())

        