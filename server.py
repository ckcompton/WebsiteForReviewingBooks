__author__ = 'Monique'

import flask
from flask import flash
from flask import redirect
from flask import url_for
from datetime import datetime
import easypg

import books

app = flask.Flask('server')


@app.route('/')
def home():
    with easypg.cursor() as cur:
        results = books.get_authfirstname(cur)
    return flask.render_template('main.html', results=results)

@app.route('/login', methods=['POST'])
def login():
    user_email= flask.request.form['user_email']
    user_password = flask.request.form['user_password']
    if user_email == '' or user_password == '' :
        error = 'login unsuccessful check username and/or password'
        return flask.render_template('main.html', errors = error)


    with easypg.cursor() as cur:
        auth_e = []
        final_results= books.login_check(cur,user_email, user_password, auth_e)
    if final_results:
        with easypg.cursor() as cur:
            error = 'Login Successful!'
            credentials = books.get_credentials(cur,user_email)
            user_home(credentials)
        #return flask.redirect(url_for('user_home'))
    else:
        error = 'login unsuccessful check username and/or password'


        #or just return an error
    return flask.render_template('home.html', errors = error)
    '''
    with easypg.cursor() as cur:
        results = books.get_authfirstname(cur)
    return flask.render_template('results.html', results=results)
    '''
@app.route('/signup', methods=['POST'])
def signup():
    firstname = flask.request.form['user_firstname']
    lastname = flask.request.form['user_lastname']
    email = flask.request.form['user_email']
    user_url = flask.request.form['user_url']
    user_pic_url = flask.request.form['user_pic_url']
    date_joined = datetime.now()
    dob = flask.request.form['dob']
    password = flask.request.form['user_password']
    with easypg.cursor() as cur:
        books.get_signup(cur, firstname, lastname, email, password, user_pic_url, user_url,date_joined,dob)
    return flask.render_template('main.html')


@app.route('/home/', methods = ['POST'])
def user_home(credentials):
     #credentials has all user attributes from the user table to display on user homepage
     return flask.render_template('home.html', credentials = credentials)












if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)