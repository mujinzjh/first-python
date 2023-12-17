from werkzeug.security import generate_password_hash
from config.exts import db


class User(db.Model):
    # 设置表名
    __tablename__ = 'bk_user'
    # id，主键并自动递增
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(256), nullable=True)
    name = db.Column(db.String(64))

    # 设置只可写入，对密码进行加密
    def password_hash(self, password):
        self.password = generate_password_hash(password)