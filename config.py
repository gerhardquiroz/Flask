import os
basedir = os.path.abspath(os.path.dirname(__file__))
 
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
 SECRET_KEY = 'you-will-never-guess'

 DOCUMENTDB_HOST = 'https://l4osrvrdb.database.windows.net:1433'
 DOCUMENTDB_KEY = 'YOUR_SECRET_KEY_ENDING_IN_=='

 DOCUMENTDB_DATABASE = 'L4Odev'