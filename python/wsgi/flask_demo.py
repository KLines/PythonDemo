
from flask import Flask,render_template
from flask import request,redirect,url_for,session
import json,os

'''
异常：
    AttributeError: module 'thread' has no attribute 'start_new_thread'
产生原因：
    项目里包含一个叫thread.py的文件或目录
'''

app = Flask(__name__)  # 创建一个服务，把当前这个python文件当做一个服务
app.secret_key = os.urandom(24)


# http://127.0.0.1:8000/get?username=zhangsan&password=123456'
# GET请求

@app.route('/get',methods=['GET'])
def get():
    username = request.args.get('username')
    password = request.args.get('password')
    data = {'name':username,'password':password}
    return json.dumps(data)


# POST请求--form格式

@app.route('/post_form',methods=['POST'])
def post_form():
    username = request.form.get('username')
    password = request.form.get('password')
    data = {'name':username,'password':password}
    return json.dumps(data)


# POST请求--json格式

@app.route('/post_json',methods=['POST'])
def post_json():
    username = request.json.get('username')
    password = request.json.get('password')
    data = {'name':username,'password':password}
    return json.dumps(data)



# singin-->重定向-->home

@app.route('/signin',methods=['GET']) # 登录页面
def signin():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/login',methods=['POST']) # 登录接口
def login():
    username = request.form['username']
    password = request.form['password']
    session['password'] = password
    return redirect(url_for('index',username=username)) #  Post-->重定向-->Get 模式


@app.route('/home?<string:username>',methods=['GET']) # 首页页面
def index(username):
    password = session.get('password')
    print(password)
    return '<h3>Hello, %s!</h3>'%username


if __name__ == '__main__':

    app.run(host='127.0.0.1',port=8000,debug='true')