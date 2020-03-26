#!flask/bin/python

import pkg_resources

from dotenv import load_dotenv

resource_package = '{{ cookiecutter.package_name }}'
resource_path = '.env'

if pkg_resources.resource_exists(resource_package, resource_path):
    DOTENV_PATH = pkg_resources.resource_filename(resource_package, resource_path)
    load_dotenv(DOTENV_PATH)

RESTPLUS_MASK_SWAGGER = False

ERROR_400_HELP = False
ERROR_404_HELP = False
ERROR_500_HELP = False

FLASK_DEBUG = False