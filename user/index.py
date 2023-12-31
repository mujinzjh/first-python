from flask import Blueprint

from config.redisConfig import redis_store
from models.User import User
from utils.result import http_success

user = Blueprint('user', __name__);

@user.route('/list')
def list_users():
    users = User.query.all()
    print(users)
    redis_store.set('name', 'hx')
    users_output = []
    for user in users:
        users_output.append(user.to_json())
    return http_success(data=users_output)
