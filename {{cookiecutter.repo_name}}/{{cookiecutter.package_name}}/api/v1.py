# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from flask_restx import Api

api = Api(version='{{ cookiecutter.version }}',
          title='{{ cookiecutter.package_name }}',
          description='{{ cookiecutter.project_description }}')