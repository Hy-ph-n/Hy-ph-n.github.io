"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from DBowenMastery5C import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
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
