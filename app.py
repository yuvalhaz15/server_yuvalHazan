from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify

app = Flask(__name__)
app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)
#
# @app.route('/')
# def first_page():  # put application's code here
#     return redirect(url_for('display_home_page'))
#
# @app.route('/home')
# def display_home_page():  # put application's code here
#     return render_template('homePage.html')
#
# @app.route('/conact')
# def display_conact_us():  # put application's code here
#     return render_template('conactUs.html')

@app.route('/assignment3_1')
def display_hobbies_page():  # put application's code here
    return render_template('assignment3_1.html')


if __name__ == '__main__':
    app.run()
