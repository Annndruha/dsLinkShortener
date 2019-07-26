import string
import random

from .get import Get, links
from .errors import *

def Gen(size=6):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))

def Set(link, creator_id, alias = None):
    if alias == None or alias == '':
        alias = Gen()
        while Get(alias) != None:
            alias = Gen()

    elif Get(alias) != None:
        raise DuplicateAliasesError(alias)

    Add({
        'link': link,
        'alias': alias,
        'creator_id': creator_id,
    })

    return alias
    
def Add(link):
    links.append(link)