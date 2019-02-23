from flask import abort, render_template
from flask_login import current_user, login_required

from . import admin


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Dashboard View
@admin.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    check_admin()
    return render_template(
        'admin/dashboard.html',
        title="Главная"
    )

@admin.errorhandler(403)
def forbidden(error):
    return render_template('admin/errors/403.html', title='Forbidden'), 403

@admin.errorhandler(404)
def page_not_found(error):
    return render_template('admin/errors/404.html', title='Page Not Found'), 404

@admin.errorhandler(500)
def internal_server_error(error):
    return render_template('admin/errors/500.html', title='Server Error'), 500

@admin.route('/500')
def error():
    abort(500)
