from flask_script import Manager
from app import app
from flask_migrate import Migrate, MigrateCommand
from config.exts import db
from models.Blog import Blog
from models.User import User
from models.Comment import Comment

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()