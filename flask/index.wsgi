import sys

#wsgi, Flaskファイルのディレクトリを指定
sys.path.insert(0, '/var/www/flask')

from index import app
application = app
