# 对整个应用做初始化

# 主要工作：
# 1.构建flask应用以及各种配置
# 2.构建SQLAlchemy的应用

from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:lw880814@localhost:3306/blog"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SECRET_KEY'] = 'YOU GUESS'
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)
    return app