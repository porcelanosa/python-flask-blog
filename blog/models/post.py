# -*- coding: utf-8 -*-

from flask_login import UserMixin

from blog import db
from blog.models.user import User


class Post(UserMixin, db.Model):
    """
    Create an Post table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    title = db.Column(db.String(250))
    caption = db.Column(db.String(250))
    short_descr = db.Column(db.Text)
    descr = db.Column(db.Text)

    author = db.relationship(User, foreign_keys=[user_id], backref='posts')


    def __repr__(self):
        return '<Post: {}>'.format(self.caption)
