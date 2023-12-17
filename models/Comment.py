from config.exts import db


class Comment(db.Model):
    __tablename__ = 'bk_comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(256))    # 评论内容
    create_time = db.Column(db.String(64))
    # 关联博客id
    blog_id = db.Column(db.Integer, db.ForeignKey("bk_blog.id"))
    # 关联用户id
    user_id = db.Column(db.Integer, db.ForeignKey("bk_user.id"))
    blog = db.relationship("Blog", backref="blog")
    user = db.relationship("User", backref="use")