import os

from flask import render_template
from flask_socketio import emit

from blog import socketio
from . import main_page


@main_page.route('/')
def index():
    """
    Render the homepage template on the / route
    """
    return render_template(
        'main_page/index.html',
        title="Блог Александра Шестакова",
        config_name=os.getenv('FLASK_CONFIG')
    )

@socketio.on('my event', namespace='/websocket')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/websocket')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/websocket')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/websocket')
def test_disconnect():
    print('Client disconnected')

