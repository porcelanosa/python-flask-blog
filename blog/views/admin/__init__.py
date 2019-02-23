# -*- coding: utf-8 -*-
from flask import Blueprint

admin = Blueprint('admin', __name__, template_folder='templates/admin')

from . import views
from .users import users_view
from .posts import posts_view
