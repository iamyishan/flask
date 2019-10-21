# coding:utf-8
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

from app import Role

app = Flask(__name__)

#配置数据的地址
app.config["SQLALCHEMY_DATABASE_URI"]='mysql://127.0.0.1:3306/test?user=root?password=tylin@123'
#跟踪数据库的修改--》不建议开启，未来的版本中会移除
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

'''
两张表
角色(管理员/普通用户)
用户(角色ID)
'''
# 数据库的模型，需要继承db.Model
class Role(db.Model):
    # 定义表名
    __tablename__='roles'
    #定义字段
    #db.Column表示一个字段
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    #db.Foreigenkey("roles.id")表示外键，表名.id
    role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template("index.html")


if __name__ == '__main__':
    # 删除表
    # db.drop_all()
    #创建表
    db.create_all()
    app.run(debug=True)
u