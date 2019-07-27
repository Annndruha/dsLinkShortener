from ..connection import Connect, Commit, GetScheme

def Get(alias):
    scheme = GetScheme()
    cur = Connect()
    cur.execute(f"SELECT id, link, alias, creator, visits FROM {scheme}.links WHERE alias = '{alias}' AND isdeleted = false")
    result = cur.fetchall()
    cur.execute(f"UPDATE ONLY {scheme}.links SET visits=visits+1 WHERE alias = '{alias}' AND isdeleted = false")
    Commit()
    cur.close()

    if len(result) == 0:
        return None
    elif len(result) == 1:
        result = result[0]
        return {
            'id': result[0],
            'link': result[1],
            'alias': result[2],
            'creator': result[3],
            'visits': result[4]
        }
    else:
        result = result[0]
        return {
            'id': result[0],
            'link': result[1],
            'alias': result[2],
            'creator': result[3],
            'visits': result[4]
        } 