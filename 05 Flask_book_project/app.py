#-*- coding:utf-8 -*-

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
#数据库配置：数据库地址
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:tylin@123@127.0.0.1/test"
#关闭自动跟踪修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

#创建数据库对象
db=SQLAlchemy(app)

'''
1.配置数据库
    a.导入SQLAlchemy扩展
    b.创建db对象，并配置参数
    c.终端创建数据库
2.添加书和作者模型
3.添加数据
4.使用模板显示数据库查询的数据
5.使用WTF显示表单
6.实现相关的增删逻辑
'''

@app.route('/')
def index():
    return render_template('book_html')
if __name__ == '__main__':
    app.run(debug=True)