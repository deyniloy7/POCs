from flask import Flask, render_template, url_for, flash, redirect, jsonify, make_response
from forms import RegistrationForm, LoginForm
import jsonResponse
from flask_api import status
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = '77196fc89f9f3bd9318a95e2d83824eb'

posts = [
    {
        'author': 'Niloy Dey',
        'title': 'New Flask Post'
    },
]


@app.errorhandler(404)
def not_found_error(error):
    return jsonResponse.makeJsonResponse(False, 'Not Found', 404, {})

@app.errorhandler(500)
def internal_error(error):
    return jsonResponse.makeJsonResponse(False, 'Internal Server Error', 500, {})

@app.route('/')
def hello_world():
    return jsonResponse.makeJsonResponse(200, "Hello World", None, "Hello")


@app.route("/about")
def about():
    return render_template('About.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created For {form.username.data}!')
        return redirect(url_for('register'))
    return render_template('Register.html',
                           title='Register',
                           form=form
                           )


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('Login.html',
                           title='Login',
                           form=form
                           )


if __name__ == '__main__':
    app.run(debug=True)
