from ..connection import Connect, Commit, GetScheme

def Get(token):
    scheme = GetScheme()
    cur = Connect()
    cur.execute(f"SELECT id, login, access_code FROM {scheme}.users WHERE access_code = '{token}' AND isdeleted = false")
    result = cur.fetchall()
    cur.close()

    if len(result) == 0:
        return None
    elif len(result) == 1:
        result = result[0]
        return {
            'id': result[0],
            'name': result[1],
            'token': result[2]
        }
    else:
        result = result[0]
        return {
            'id': result[0],
            'name': result[1],
            'token': result[2]
        }

