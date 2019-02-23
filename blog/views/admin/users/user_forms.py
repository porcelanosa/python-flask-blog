# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class UserForm(FlaskForm):
    """
    Form for admin to add or edit a user
    """
    username = StringField('Логин', validators=[DataRequired()])
    email = EmailField('Email', validators=[Email('введите корректный Email адрес'), DataRequired()])
    # avatar = FileField('Аватар', validators=[Regexp(r'^[^/\\]\.jpg$')]), [Regexp(r'^[^/\\]\.jpg$')]
    avatar = FileField('Аватар')
    submit = SubmitField('Submit')
