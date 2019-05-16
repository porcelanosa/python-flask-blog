# -*- coding: utf-8 -*-
import os

import flask_resize
# third-party imports
from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

# local imports
from .local_config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

config_name = os.getenv('FLASK_CONFIG', 'production')

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[config_name])
# app.config['UPLOAD_FOLDER'] = app_config.UPLOAD_FOLDER
app.config.from_pyfile('config.py', silent=True)
app.config['RESIZE_URL'] = '/static/uploads/'
# app.config['RESIZE_ROOT'] = os.path.join('E:\\','FlaskAPPS','my-blog','blog','static','uploads')
app.config['RESIZE_ROOT'] = '/var/www/porcelanosa/data/www/blog.71b.ru/blog/static/uploads' #os.path.join('var','www','porcelanosa','data','www','blog.71b.ru','blog','static','uploads')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
Bootstrap(app)
db.init_app(app)
resize = flask_resize.Resize(app)
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#
# from .models import user
#
from blog.views.admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')

from blog.views.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from blog.views.main_page import main_page as main_page_blueprint
app.register_blueprint(main_page_blueprint)

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='Forbidden'), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title='Page Not Found'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html', title='Server Error'), 500

@app.route('/500')
def error():
    abort(500)

#
# if __name__ == '__main__':
#     app.run()
