# modules flask app, requests ans templates
from flask import Flask
from flask import request
from flask import render_template
from flask_wtf import CsrfProtect  # injections protect with token

from flask import make_response # this type of response allow us setting cookies
from flask import session  #  we can save session data
from flask import url_for
from flask import redirect

# import forms.py
import forms
import loginform

# instance a flask app named app, with __name__ and te folder views for templates as parameters
app = Flask(__name__, template_folder='views')
app.secret_key = 'my_secret_key_app'  # key of token
Csrf = CsrfProtect(app)  # protect app


# root can with get parameter get1 as parameter of the template index
@app.route('/')
def index():
    custom_cookie = request.cookies.get('custom_cookie', 'undefined')
    print(custom_cookie)
    get1 = request.args.get('get1', 'No name insert')
    # this route implements forms for comments with a object comment_form
    comment_form = forms.CommentForm()
    return render_template('index.html', name=get1, form=comment_form)


# route param with sub route num which type is int, and default value 'no se ingreso num', parameter params and a
# string variable hola, the template receive them as parameter to can show them into view
# params will can receive post of others templates
@app.route('/param/')
@app.route('/param/<int:num>/', methods=['GET', 'POST'])
def param(num='no se ingreso num'):
    # if the route receive a form by post and num == 1(from index form) print the fields
    if request.method == 'POST' and num == 1:
        print(request.form['username'])
        print(request.form['email'])
        print(request.form['comment'])
    params = request.args.get('params', 'no se ingreso parametro')
    saludo = "Hola mundo"
    mylist = [1, 2, 3, 'a', 'b', 'c']
    return render_template('params.html', hola=saludo, name=params, num=num, mylist=mylist)


# Route for process the login form and use of sessions for save form data values
@app.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = loginform.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        # if request is a post and form data is valid save data on session and print it
        session['name'] = login_form.username.data
        session['pass'] = login_form.password.data
        print(login_form.username.data)
        print(login_form.password.data)
    return render_template('login.html', login=login_form)


# this route delete session data and redirect to login function
@app.route('/logout/')
def logout():
    if 'name' and 'pass' in session:
        session.pop('name')
        session.pop('pass')
    return redirect(url_for('login'))


# Render a template with cookies, the response 'make_response' allow us to manipulate
# the response, par example cookies.
@app.route('/cookie/')
def cookie():
    cookie_name = request.cookies.get('custom_cookie', 'undefined')
    if 'name'and 'pass' in session:  # if username and password data in session sent it into template
        name = session['name']
        passw = session['pass']
    else:
        name = 'No mame insert'
        passw = 'No password insert'
    response = make_response(render_template('cookie.html', cookie_name=cookie_name, name=name, passw=passw))
    response.set_cookie('custom_cookie', 'Wave')  # set cookie into this response with value 'wave'
    return response


# if this script runs as main the app will run
if __name__ == '__main__':
    app.run(debug=True)  # debug activate