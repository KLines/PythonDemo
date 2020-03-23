
from flask import Flask,render_template
from flask import request,redirect,url_for,session
import json,os

'''

异常：
    AttributeError: module 'thread' has no attribute 'start_new_thread'
    产生原因：项目里包含一个叫thread.py的文件或目录
    
    
url_for传参：url_for('方法名', key='value')

    如果是/get?username=zhangsan这种拼接参数，定义的方法不需要带参数 ，flask会自动拼接成?key=value的模式
    
        url_for('login',username='test')
        
        @app.route('/login')
        def login():
            return ''
        
    如果是/user/<username>这种路由中带的参数，定义的方法中需携带参数，参数名必须和路由参数一致
    
        url_for('profile',username=username)
        
        @app.route('/user/<username>')
        def profile(username):
            return ''
        
    

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


# POST请求

@app.route('/post',methods=['POST'])
def post():

    if request.is_json: # json格式
        username = request.json.get('username')
        password = request.json.get('password')
    else:  # form格式
        username = request.form.get('username')
        password = request.form.get('password')
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
    return redirect(url_for('index',username=username)) # 重定向


@app.route('/home',methods=['GET']) # 首页页面
def index():
    password = session.get('password')
    username = request.args.get('username')
    print(password)
    return '<h3>Hello, %s!</h3>'%username


if __name__ == '__main__':

    app.run(host='127.0.0.1',port=8000,debug='true')
