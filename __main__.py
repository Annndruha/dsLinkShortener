from gevent.pywsgi import WSGIServer
from config_mngr import config, save, load
from web import app

from db_mngr import Connect, Disconnect, GetLink
#from db_mngr import *

if __name__ == "__main__":
    try:
        load(path = 'config/database.json', name = 'db')
        print('Load config sucsess!')
    except FileNotFoundError as err:
        print(err)
        print('Making default config')
        config['db'] = {'host': '0.0.0.0',
						'port': '5432', 
						'user': 'root', 
						'password': '', 
						'dbname': 'postgres', 
						'scheme': 'public'}
    except Exception as err:
        print(err)
        exit(1)
    finally:
        save('db')

    try:
        Connect(config['db'])
        print('Connection db sucsess!')
    except Exception as err:
        print(err)
        exit(2)
    
    http_server = WSGIServer(('0.0.0.0', 80), app) # 0.0.0.0 - localhost
    http_server.serve_forever()

    Disconnect()