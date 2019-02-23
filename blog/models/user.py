# -*- coding: utf-8 -*-

from flask_login import UserMixin
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash

from blog import db, login_manager
from blog.config import Config


class User(UserMixin, db.Model):
    """
    Create an User table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    avatar = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    # department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @property
    def avatar_image(self):
        return '<img src="' + Config.UPLOAD_FOLDER + self.avatar + '">'

    def avatar_url(self):
        return Config.UPLOAD_FOLDER + self.avatar

    def avatar_path(self):
        return Config.ROOT_PATH + '/' + self.avatar

    def avatar_resize(self, width="100"):
        return '<img src="' + Config.UPLOAD_FOLDER + self.avatar + '" width="' + width + '">'

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    # print('ID:%s' % (user_id))
    # if user_id is None or user_id == 'None' or not isinstance(user_id, int):
    #     user_id = -1
    # print ('ID: %s, leaving load_user' % (user_id))
    try:
        return User.query.get(int(user_id))
    except exc.SQLAlchemyError:
        return None
