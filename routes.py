"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')


@route('/iModel')
@view('Imodel')
def about():
    """Renders the about page."""
    return dict(
        title='I am a model',
        message='Your application description page.',
        year=datetime.now().year
    )
