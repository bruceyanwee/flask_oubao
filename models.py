

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
class MySQLAlchemy(SQLAlchemy):  # Or you can add the below code on the SQLAlchemy directly if you think to modify the package code is acceptable.
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable
import pymysql

app = Flask(__name__)
# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///oubao.db"

# 数据库和模型类同步修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = 'dadad'
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

db = MySQLAlchemy(app)


# 用户信息表
class User_info(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(64),nullable=False)
    gender = db.Column(db.Enum("男","女"),nullable=False)
    month_age = db.Column(db.Integer)
    level = db.Column(db.Integer)
    phone_num = db.Column(db.String(11),nullable=True)
    password = db.Column(db.String(10))

class Game_resources(db.Model):
    __tablename__ = 'game_resources'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    description = db.Column(db.String(100),nullable=True)
    belong_age = db.Column(db.Integer)
    tag = db.Column(db.String(10),nullable=True)
    video_url = db.Column(db.String(30),nullable=True)
    picture_url = db.Column(db.String(30),nullable=True)

if __name__ == '__main__':
    db.create_all()