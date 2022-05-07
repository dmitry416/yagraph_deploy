from flask import Flask, request, jsonify, render_template, redirect
from data import db_session
from algorithms import algs, parse_request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.users import User
from data.loginform import LoginForm
from data.registerform import RegisterForm
import logging
import requests
import json


ALGS = algs
global jsdata
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    global cur_username
    cur_username = db_sess.query(User).filter(User.id == user_id)[0].username
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init('db/blogs.sqlite')
    app.run()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/graph')
def graph():
    if current_user.is_authenticated:
        return render_template('main.html', name=cur_username)
    else:
        redirect('/')


@app.route('/save', methods=['POST'])
def save():
    jsdata = request.form['javascript_data']

    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.username == cur_username).first()
    user.history = jsdata
    db_sess.commit()
    return ""


def get_enumerated(arr):
    out = {}
    for i in range(len(arr)):
        out[i] = arr[i]
    return out


@app.route('/bfs', methods=['POST'])
def bfs():
    global jsdata
    jsdata = json.loads(request.form['javascript_data'])
    return ""


@app.route('/bfs', methods=['GET'])
def bfs_get():
    graph = {'graph': get_enumerated(jsdata),
             'alg': 'bfs'}
    return str(requests.get('http://127.0.0.1:5000/api/', json=graph).json())


@app.route('/dj', methods=['POST'])
def dj():
    global jsdata
    jsdata = json.loads(request.form['javascript_data'])
    return ""


@app.route('/dj', methods=['GET'])
def dj_get():
    graph = {'graph': get_enumerated(jsdata),
              'alg': 'dij, 1'}
    print(requests.get('http://127.0.0.1:5000/api/', json=graph).json())
    return str(requests.get('http://127.0.0.1:5000/api/', json=graph).json())


@app.route('/mintree', methods=['POST'])
def mintree():
    global jsdata
    jsdata = json.loads(request.form['javascript_data'])
    return ""


@app.route('/mintree', methods=['GET'])
def mintree_get():
    graph = {'graph': get_enumerated(jsdata),
             'alg': 'min_tree'}
    return str(requests.get('http://127.0.0.1:5000/api/', json=graph).json())


@app.route('/eul', methods=['POST'])
def eul():
    global jsdata
    jsdata = json.loads(request.form['javascript_data'])
    return ""


@app.route('/eul', methods=['GET'])
def eul_get():
    graph = {'graph': get_enumerated(jsdata),
             'alg': 'is_eul'}
    return str(requests.get('http://127.0.0.1:5000/api/', json=graph).json())


@app.route('/tree', methods=['POST'])
def tree():
    global jsdata
    jsdata = json.loads(request.form['javascript_data'])
    return ""


@app.route('/tree', methods=['GET'])
def tree_get():
    graph = {'graph': get_enumerated(jsdata),
             'alg': 'is_tree'}
    return str(requests.get('http://127.0.0.1:5000/api/', json=graph).json())


@app.route('/gethistory')
def get_history():
    db_sess = db_session.create_session()
    return db_sess.query(User).filter(User.username == cur_username).first().history


@app.route('/singin', methods=['POST', 'GET'])
def singin():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect("/graph")
        return render_template('singin.html', form=form)
    return render_template('singin.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/singup', methods=['POST', 'GET'])
def singup():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('singup.html', form=form)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('singup.html', form=form)
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/singin')
    return render_template('singup.html', form=form)


@app.route('/api/', methods=['GET'])
def api():
    return jsonify(parse_request((request.get_json())))


if __name__ == '__main__':
    main()
