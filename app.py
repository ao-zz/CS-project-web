'''

'''
import flask
from flask import request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = flask.Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def home():
    return render_template('index.html', name='游客',
                           current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    # url_for('index', name=...)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/gantt/<event_id>')
def add(event_id):
    return render_template('gantt.html', event_id=event_id)


@app.route('/event/<user_id>')
def html_homepage(user_id):
    return render_template('event.html', user_id=user_id)


app.run(debug=True)
