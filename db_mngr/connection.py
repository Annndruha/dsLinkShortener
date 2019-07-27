import psycopg2 as db

connection = {}
scheme = ''

def Connect(config = {}):
    global connection
    global scheme

    if connection == {}:
        scheme = config['scheme']
        connection = db.connect(host = config['host'], 
                                port = config['port'],
                                user = config['user'], 
                                password = config['password'], 
                                dbname  = config['dbname'])
    return connection.cursor()

def GetScheme():
    return scheme

def Commit():
    connection.commit()

def Disconnect():
    global connection
    connection.close()