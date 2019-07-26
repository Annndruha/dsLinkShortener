
users = []

users.append({
    'id': 1,
    'name': 'dyakovri',
    'token': 'some-very-long-line'
})

def Get(token):
    if users[0]['token'] == token:
        return users[0]
    else:
        return None