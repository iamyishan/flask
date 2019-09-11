### 一、包记录信息

- requirements文件

  - 记录所有依赖包及其精确的版本号

  - 在项目的文件目录下打开终端，输入命令生成requirements文件

    ~~~shell
    pip freeze >requirements.txt
    ~~~

  - 需要移植项目到其他电脑，在项目文件下输入命令

    ~~~
    pip freeze -r requirements.txt
    ~~~


### 二、路由

- url传递参数

  - 默认是参数类型类型是字符串str

  ~~~Python
  @app.route("/orders/<order_id>")
  def get_order_id(order_id):
      #需要在视图函数的（）内填入参数名，后面的代码去使用
      return 'oder_id %s' % order_id
  #客户端输入http://127.0.0.1:5000/orders/345，参数就是345
  ~~~

  - 更该参数的类型：int、float、path

    ~~~python
    @app.route("/orders/<int:order_id>") #规定参数为整数
    ~~~

    | int    | 接受整数                   |
    | ------ | -------------------------- |
    | float  | 同 int ，但是接受浮点数    |
    | *path* | 和默认的相似，但也接受斜线 |

### 三、Jinja2模型引擎

- 引入render_template

-  render_template()函数渲染

  ~~~Python
  from flask import render_template
  
  @app.route('/hello/')
  @app.route('/hello/<name>')
  def hello(name=None):
      return render_template('hello.html', name=name)
  ~~~

- 注释

  - {# #}

- 变量代码块

  ~~~html
  <!--列表的使用-->
  {{my_list}}<br>
  {{my_list.2}}<br>
  {{my_list[2]}}<br>
  
  <!--字典的使用-->
  {{my_dict}}<br>
  {{my_dict.name}}<br>
  {{my_dict['name']}}<br>
  ~~~

- 控制代码块

  `{% %}`

  ~~~html
  <!doctype html>
  <title>Hello from Flask</title>
  {% if name %}
    <h1>Hello {{ name }}!</h1>
  {% else %}
    <h1>Hello World!</h1>
  {% endif %}
  ~~~


- 过滤器

  ~~~html
  <!--字符串变大些-->
  {{url_str | upper}}
  <!--字符串反转-->
  {{url_str | reverse}}
  ~~~

  - l链式调用

    ~~~html
    <!--过滤器的链式调用-->
    {{url_str | upper |reverse}}<br>
    ~~~

### 四、web表单

**采用扩展Flask-WTF**

WTForm支持html标准字段

- 原生实现

  ~~~html
  <form method="post",>
      <label>用户名：</label> <input type="text" name="username"><br>
      <label>密码：</label> <input type="password" name="password"><br>
      <label>确认密码：</label> <input type="password" name="password2"/> <br>
      <input type="submit" value="提交"/>
  </form>
  ~~~

- 使用Flask-WTF实现表单：

### 五、flash扩展

- 用途：给模板传递消息，模板中需要遍历消息
  flash 需要设置secret_key，做加密消息混淆

  ~~~html
  <!-- 使用遍历获取闪现的消息-->
      {% for message in get_flashed_messages() %}
          {{message}}
      {% endfor %}
  ~~~

### 六、flask使用数据库