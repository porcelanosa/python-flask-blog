# -*- coding: utf-8 -*-
import os
class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    UPLOAD_FOLDER = '/static/uploads/'
    # UPLOAD_FOLDER = os.path.join(os.path.join('static/uploads/'))
    ROOT_PATH = os.path.join('E:\\','FlaskAPPS','my-blog','blog','static','uploads')
    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

