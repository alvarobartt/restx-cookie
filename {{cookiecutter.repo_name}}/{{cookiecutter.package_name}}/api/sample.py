# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from flask_restx import Resource

from ..run import api

from .sample_serializers import sample_data
from .sample_parsers import sample_arguments
{% if cookiecutter.flask_limiter|lower == 'yes' %}
from ..core import limiter
{%- endif %}
{%- if cookiecutter.flask_cache|lower == 'yes' %}
from ..core import cache
{%- endif %}

from ..utils import handle400error, handle404error, handle500error

sample_ns = api.namespace('sample', description='{{ cookiecutter.package_name }} - sample namespace')


@sample_ns.route('/data')
class SampleData(Resource):
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
        
        return {'data': 'get'}

    @api.response(400, 'Invalid parameters')
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    {%- if cookiecutter.flask_limiter|lower == 'yes' %}
    @limiter.limit('100/hour')
    {%- endif %}
    {%- if cookiecutter.flask_cache|lower == 'yes' %}
    @cache.cached(timeout=120, query_string=True)
    {%- endif %}
    def post(self):
        """
        This is a sample HTTP POST method
        """

        return {'data': 'post'}
