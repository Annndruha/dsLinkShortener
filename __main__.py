import config_mngr as cfg
from config_mngr import config

from web import app

import db_mngr as db



if __name__ == "__main__":
    try:
        cfg.load(path = 'config/database.json', name = 'db')
    except FileNotFoundError as err:
        print(err)
        print('Making default config')
        config['db'] = {'host': 'localhost',
						'port': '5432', 
						'user': 'root', 
						'password': '', 
						'dbname': 'postgres', 
						'scheme': 'public'}
    except Exception as err:
        print(err)
    finally:
        cfg.save('db')

    app.run(debug=True)