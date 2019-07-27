import string
import random

from .get import Get
from .errors import *
from ..connection import Connect, Commit, GetScheme

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
    scheme = GetScheme()
    cur = Connect()
    cur.execute(f"SELECT MAX(id) FROM {scheme}.links")
    link['id'] = int(cur.fetchone()[0])+1
    cur.execute(f"INSERT INTO {scheme}.links (id, link, alias, creator) VALUES ({link['id']}, \'{link['link']}\', \'{link['alias']}\', {link['creator_id']})")
    Commit()
    cur.close()