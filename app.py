from flask import Flask
from flasgger import Swagger
from config.exts import db
import config.config
from user.index import *

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = config.config.SWAGGER_TITLE
# 描述信息
swagger_config['description'] = config.config.SWAGGER_DESC
# Host
swagger_config['host'] = config.config.SWAGGER_HOST


app = Flask(__name__)

app.config.from_object(config.config)
db.init_app(app)

app.register_blueprint(user, url_prefix="/user")
swagger = Swagger(app, config=swagger_config)
if __name__ == '__main__':
    app.run()
