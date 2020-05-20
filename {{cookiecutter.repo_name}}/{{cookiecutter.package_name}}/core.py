# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.
{% if cookiecutter.flask_cache|lower == 'yes' %}
from flask_caching import Cache

cache = Cache(
    config={
        'CACHE_TYPE': 'simple'
    }
)
{%- endif %}
{%- if cookiecutter.flask_limiter|lower == 'yes' %}

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)
{%- endif %}