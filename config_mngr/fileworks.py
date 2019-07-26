import json
from .config import *
from .errors import *

def load(path, name = None):
    if name == None:
        name = path
    
    if files.get(name) == None:
        files[name] = path
    else:
        raise DuplicateConfigurationError("Config with name " + name + " is already exists")

    with open(files[name], "r") as config_file:
        config[name] = json.load(config_file)

def save_all():
    for name in config:
        with open(files[name], "w") as config_file:
            json.dump(config[name],config_file)
            

def save(name):
    if files.get(name) != None:
        with open(files[name], "w") as config_file:
            json.dump(config[name],config_file)
    else:
        raise EmptyConfigurationError("Config with name " + name + " isn\'t exists")