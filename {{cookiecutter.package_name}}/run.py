#!flask/bin/python

from flask import Flask, Blueprint

import pkg_resources

import re

from . import config

{%- if cookiecutter.flask_limiter|lower == 'yes' %}
from .core import limiter
{%- endif %}

{%- if cookiecutter.flask_cache|lower == 'yes' %}
from .core import cache
{%- endif %}

{%- if cookiecutter.flask_cors|lower == 'yes' %}
from flask_cors import CORS
{%- endif %}

from .api.v1 import api

from .api.equities import equities_ns
from .api.etfs import etfs_ns
from .api.funds import funds_ns
from .api.indexed_funds import indexed_funds_ns
from .api.currencies import currencies_ns
from .api.portfolio import portfolio_ns

app = Flask('{{ cookiecutter.package_name }}')


def get_dependency_version(dependency):
    """
    This function gets the version of a dependency in order to let the user know 
    which is its required version.
    """

    pattern = re.compile(r"(?<=\=\=|\>\=).*")
    dependency_version = pattern.search(dependency)

    return dependency_version.group()


def check_api_dependencies():
    """
    This function tests if the API is properly configured.
    """

    try:
        with open('requirements.txt', 'r') as f:
            dependencies = list()

            for line in f.readlines():
                dependencies.append(line.strip())
        f.close()
    except:
        raise FileNotFoundError("requirements.txt file not found or errored.")
    
    for dependency in dependencies:
        dependency_version = get_dependency_version(dependency)
        try:
            pkg_resources.require(dependency)
        except pkg_resources.DistributionNotFound:
            raise pkg_resources.DistributionNotFound(f'[{dependency}] not found, please check that it is properly installed.')
        except pkg_resources.VersionConflict:
            raise pkg_resources.VersionConflict(f'[{dependency}] version errored, since required version is {dependency_version}')


def configure_app(flask_app):
    """
    This function configures the Flask application with the settings specified in `config.py`.
    """

    flask_app.config.from_object(config)


def initialize_app(flask_app):
    """
    This function initializes the Flask application, adds the namespace and registers the blueprints.
    """

    configure_app(flask_app)

    v1 = Blueprint('api', '{{ cookiecutter.package_name }}', url_prefix='/v1')
    api.init_app(v1)

    {%- if cookiecutter.flask_limiter|lower == 'yes' %}
    limiter.init_app(flask_app)
    {%- endif %}
    {%- if cookiecutter.flask_cache|lower == 'yes' %}
    cache.init_app(flask_app)
    {%- endif %}
    
    # api.add_namespace(equities_ns)
    flask_app.register_blueprint(v1)


initialize_app(app)
{%- if cookiecutter.flask_cors|lower == 'yes' %}
CORS(app)
{%- endif %}


def launch_api(enable_ssl):
    """
    This function launches the API in the public IP (0.0.0.0) in the port 5000.
    """

    print("=========================================")
    print(f"Author: {__name__.__author__}")
    print(f"Version: {__name__.__version__}")
    if enable_ssl is True:
        print('SSL is enabled!')
    else:
        print('SSL is disabled!')
    print("=========================================")

    check_api_dependencies()

    if enable_ssl is True:
        app.run(host='0.0.0.0', port='5000', debug=config.FLASK_DEBUG, ssl_context='adhoc')
    else:
        app.run(host='0.0.0.0', port='5000', debug=config.FLASK_DEBUG)


def main():
    """
    This is the main function that is launched whenever the package is called.
    """

    import argparse

    parser = argparse.ArgumentParser(prog='{{ cookiecutter.package_name }}')
    parser.add_argument('-s', '--enable_ssl', action='store_true', default=False, help="Use this argument to either use SSL or not.")

    args = parser.parse_args()

    launch_api(enable_ssl=args.enable_ssl)


if __name__ == '__main__':
    main()
