import os

from flask import render_template

from . import main_page


@main_page.route('/')
def index():
    """
    Render the homepage template on the / route
    """
    return render_template(
        'main_page/index.html',
        title="Блог Александра Шестакова",
        config_name=os.getenv('FLASK_CONFIG')
    )
