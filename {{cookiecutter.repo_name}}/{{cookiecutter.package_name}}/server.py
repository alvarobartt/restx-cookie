# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from flask import Flask, Blueprint

import click

import re
import pkg_resources

from .__init__ import __author__, __version__, __license__

from . import config
{% if cookiecutter.flask_limiter|lower == 'yes' %}
from .core import limiter
{%- endif %}
{%- if cookiecutter.flask_cache|lower == 'yes' %}
from .core import cache
{%- endif %}
{% if cookiecutter.flask_cors|lower == 'yes' %}
from flask_cors import CORS
{%- endif %}

from .api.v1 import api

from .api.sample import sample_ns

app = Flask('{{ cookiecutter.package_name }}')


def configure_app(flask_app):
    """This function configures the Flask application with the settings specified in `config.py`."""

    flask_app.config.from_object(config)


def initialize_app(flask_app):
    """This function initializes the Flask application, adds the namespace and registers the blueprints."""

    configure_app(flask_app)

    v1 = Blueprint('api', '{{ cookiecutter.package_name }}', url_prefix='/v1')
    api.init_app(v1)
    
    {% if cookiecutter.flask_limiter|lower == 'yes' %}
    limiter.init_app(flask_app)
    {%- endif %}
    {%- if cookiecutter.flask_cache|lower == 'yes' %}
    cache.init_app(flask_app)
    {%- endif %}
    
    api.add_namespace(sample_ns)

    flask_app.register_blueprint(v1)


initialize_app(app)
{%- if cookiecutter.flask_cors|lower == 'yes' %}
CORS(app)
{%- endif %}


@click.command()
@click.option("--enable-ssl", default=False, is_flag=True, help="Use this argument to enable SSL.")
def run(enable_ssl):
    """This function deploys the API in the public IP (0.0.0.0) in the port 5000."""

    print("=========================================")
    print(f"Author: {__author__}")
    print(f"Version: {__version__}")
    print(f"License: {__license__}")
    if enable_ssl is True:
        print('SSL is enabled!')
    else:
        print('SSL is disabled!')
    print("=========================================")

    if enable_ssl is True:
        app.run(host='0.0.0.0', port='5000', debug=config.FLASK_DEBUG, ssl_context='adhoc')
    else:
        app.run(host='0.0.0.0', port='5000', debug=config.FLASK_DEBUG)


if __name__ == '__main__':
    run()
