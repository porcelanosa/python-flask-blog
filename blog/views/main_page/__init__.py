from flask import Blueprint

main_page = Blueprint('home', __name__)

from . import views
