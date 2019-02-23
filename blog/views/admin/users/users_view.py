# -*- coding: utf-8 -*-
from flask import current_app as app, flash, redirect, render_template, url_for, request
from flask_login import login_required

from blog import db
from blog.config import Config
from blog.models.user import User
from blog.views.admin import admin
from blog.views.admin.users.user_forms import UserForm
from blog.views.admin.views import check_admin


# Users Views

@admin.route('/users')
@login_required
def users():
    """
    List all users
    """
    check_admin()

    users = User.query.all()
    return render_template('admin/users/users.html',
                           users=users, title='Пользователи')


@admin.route('/users/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    """
        Edit user
    """
    check_admin()
    req = request
    user = User.query.get_or_404(id)

    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        filename = form.avatar.data.filename
        form.avatar.data.save(Config.UPLOAD_FOLDER + filename)
        user.avatar = filename
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно сохранили пользователя')

        # redirect to the roles page
        return redirect(url_for('admin.users'))

    return render_template('admin/users/edit_user.html',
                           user=user, form=form,
                           title='Редактирование пользователя ' + user.username,
                           uploaderFolder=app.config['UPLOAD_FOLDER']
                           )


@admin.route('/users/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    """
    Delete a user from the database
    """
    check_admin()

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('You have successfully deleted the user.')

    # redirect to the departments page
    return redirect(url_for('admin.users'))
