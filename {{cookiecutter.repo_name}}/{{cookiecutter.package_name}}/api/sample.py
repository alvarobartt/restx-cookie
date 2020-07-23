# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from flask_restx import Resource

from .parsers import sample_parser

from ..server import api

{% if cookiecutter.flask_limiter|lower == 'yes' %}
from ..core import limiter
{%- endif %}
{%- if cookiecutter.flask_cache|lower == 'yes' %}
from ..core import cache
{%- endif %}

from ..error_handlers import handle400error, handle404error, handle500error

sample_ns = api.namespace('sample', description='{{ cookiecutter.package_name }} - This is a sample namespace')


@sample_ns.route('/data')
class SampleData(Resource):

    @api.expect(sample_parser)
    @api.response(400, 'Invalid parameters')
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    {%- if cookiecutter.flask_limiter|lower == 'yes' %}
    @limiter.limit('100/hour')
    {%- endif %}
    {%- if cookiecutter.flask_cache|lower == 'yes' %}
    @cache.cached(timeout=120, query_string=True)
    {%- endif %}
    def get(self):
        """
        This is a sample HTTP GET method
        """

        args = sample_parser.parse_args()
        
        return args

    @api.expect(sample_parser)
    @api.response(400, 'Invalid parameters')
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    {%- if cookiecutter.flask_limiter|lower == 'yes' %}
    @limiter.limit('100/hour')
    {%- endif %}
    {%- if cookiecutter.flask_cache|lower == 'yes' %}
    @cache.memoize(timeout=120)
    {%- endif %}
    def post(self):
        """
        This is a sample HTTP POST method
        """

        args = sample_parser.parse_args()
        
        return args
