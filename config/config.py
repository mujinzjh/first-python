# config.py
USERNAME = 'root'
PASSWORD = 'Zjh971210%'
HOSTNAME = "47.109.28.1"
PORT = '3306'
DATABASE = 'BK'

DIALECT = 'mysql'
DRIVER = 'pymysql'

# 连接数据的URI
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SWAGGER_TITLE = "API"
SWAGGER_DESC = "API接口"
# 地址，必须带上端口号
SWAGGER_HOST = "localhost:5000"

REDIS_HOST = "47.109.28.1"
REDIS_PORT = 6379
REDIS_PWD = '123456'
REDIS_DB = 0
