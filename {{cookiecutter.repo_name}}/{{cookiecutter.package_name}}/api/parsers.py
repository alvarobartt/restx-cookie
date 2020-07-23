# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from flask_restx import reqparse, inputs

sample_parser = reqparse.RequestParser()

sample_parser.add_argument(
    'test', type=inputs.boolean, help='This is just a test parameter',
    required=False
)
