# -*- coding: utf-8 -*-
from flask import current_app as app, flash, redirect, render_template, url_for, request
from flask_login import login_required

from blog import db
from blog.models.post import Post
from blog.views.admin import admin
from blog.views.admin.posts.post_forms import PostForm
from blog.views.admin.views import check_admin


# Users Views

@admin.route('/posts')
@login_required
def posts():
    """
    List all posts
    """
    check_admin()

    posts = Post.query.all()
    return render_template('admin/posts/posts.html',
                           posts=posts, title='Посты')


@admin.route('/posts/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    """
        Edit user
    """
    check_admin()
    req = request
    post = Post.query.get_or_404(id)

    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title= form.title.data
        post.caption = form.caption.data
        db.session.add(post)
        db.session.commit()
        flash('Вы успешно сохранили пользователя')

        # redirect to the roles page
        return redirect(url_for('admin.posts'))

    return render_template('admin/posts/edit_post.html',
                           post=post, form=form,
                           title='Редактирование поста ' + post.caption,
                           uploaderFolder=app.config['UPLOAD_FOLDER']
                           )


@admin.route('/posts/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    """
    Delete a user from the database
    """
    check_admin()

    post= Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('You have successfully deleted the post.')

    # redirect to the departments page
    return redirect(url_for('admin.posts'))
