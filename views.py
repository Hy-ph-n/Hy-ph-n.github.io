"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from DBowenMastery5C import app

@app.route('/')
@app.route('/index')
def index():
    """Renders the index page."""
    return render_template(
        'index.html',
        title='Index Page',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='My about page!'
    )

@app.route('/hobbies')
def hobbies():
    """Renders the hobbies page."""
    return render_template(
        'hobbies.html',
        title='Hobbies',
        year=datetime.now().year,
        message='My hobby page!'
    )
