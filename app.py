from flask import Flask,request,session,url_for,current_app,g,render_template
from werkzeug.local import Local,LocalStack
from utils import log_a,log_b,log_c
from threading import local
import os

app = Flask(__name__)
app.config['SECRET_KEY'] =os.urandom(24)
#只要绑定到Local对象上的属性
#在每个线程里面都是隔离的
# app_context = app.app_context()
# app_context.push()
#另外一种写法
# with app.app_context():
#     print(current_app)



@app.route('/')
def index():
    # print("--"*10)
    # print(current_app.name)
    username = request.args.get('username')
    g.username = username
    # log_a()
    # log_b()
    # log_c()
    if hasattr(g,'user'):
        print(g.user)
        print('显示啊，大哥')
    return render_template('index.html')



@app.route('/list/')
def my_list():
    session['user_id'] = 1
    return render_template('list.html')




with app.test_request_context():
    """
    手动推入一个请求上下文到请求上下文栈中;
    如果当前应用上下文栈中没有应用上下文
    那么会首先推入一个应用上下文
    """
    print(url_for('my_list'))


@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user = 'richard'


@app.context_processor
def context_process():
    return {"current_user":'richard'}

if __name__ == '__main__':
    app.run()
