from flask import Blueprint
from models.User import User
from utils.result import http_success

user = Blueprint('user', __name__);

@user.route('/list')
def list_users():
    users = User.query.all()
    print(users)
    users_output = []
    for user in users:
        users_output.append(user.to_json())
    return http_success(data=users_output)
