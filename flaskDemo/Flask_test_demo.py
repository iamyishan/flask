#-*- coding: utf-8 -*-

# 1.导入Flask扩展
from flask import Flask,render_template

# 2.创建Flask应用程序实例
# 需要传入__naem__，作用是为了确定资源所在路径
app=Flask(__name__)

#3.定义路由及视图函数
#路由默认只支持GET,如果需要增加，需要自行指定

@app.route('/',methods=["GET","POST"])
def index():
    # return "hello flask"
    return render_template('index.html')



# 使用同一个视图函数，来显示不同用户的订单信息
# <>定义路由的参数，<>内需要起个名字
# @app.route("/orders/<order_id>")
@app.route("/orders/<int:order_id>") #规定参数为整数
def get_order_id(order_id):
    #参数类型默认是字符串,str
    print(type(order_id))

    #需要在视图函数的（）内填入参数名，后面的代码菜鸟去使用
    return 'order_id %s' % order_id

#4.启动程序
if __name__=="__main__":
    #执行了app.run.就会将Flask程序运行在一个简易的服务器(Flask提供的，用户测试的)
    # app.run()
    app.run(debug=True)