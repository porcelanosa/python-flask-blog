# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    """
    Form for admin to add or edit a user
    """
    title = StringField('Title', validators=[DataRequired()])
    caption = StringField('Заголовок', validators=[DataRequired()])
    short_descr = TextAreaField('Анонс', validators=[ DataRequired()])
    descr = TextAreaField('Анонс', validators=[ DataRequired()])
    # avatar = FileField('Аватар', validators=[Regexp(r'^[^/\\]\.jpg$')]), [Regexp(r'^[^/\\]\.jpg$')]
    avatar = FileField('Аватар')
    submit = SubmitField('Submit')
