from config.exts import db


class Blog(db.Model):
    __tablename__ = 'bk_blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    text = db.Column(db.TEXT)
    create_time = db.Column(db.String(64))
    #关联用户id
    user_id = db.Column(db.Integer, db.ForeignKey('bk_user.id'))
    user = db.relationship('User', backref='user')