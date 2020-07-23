# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

def handle400error(namespace, error_desc):
    """
    This function handles & formats the introduced error_desc into a HTTP response which will be returned in
    case of exception raising, as an abort() method from the specified namespace. HTTP 400 error code stands for
    Bad Request, which means that the request parameters were not properly sent in the GET request.
    """

    return namespace.abort(400, status=error_desc, statusCode="400")


def handle404error(namespace, error_desc):
    """
    This function handles & formats the introduced error_desc into a HTTP response which will be returned in
    case of exception raising, as an abort() method from the specified namespace. HTTP 404 error code stands for
    Not Found, which means that the received request could not be resolved.
    """

    return namespace.abort(404, status=error_desc, statusCode="404")


def handle500error(namespace):
    """
    This function handles & formats unknown errors into a HTTP response which will be returned in
    case of exception raising, as an abort() method from the specified namespace. HTTP 500 error code stands for
    Internal Server Error, which encompasses all the unhandled errors.
    """

    error_desc = "Unknown error, please contact API administrator: {{ cookiecutter.email }}, {{ cookiecutter.github_username }} @ GitHub."

    return namespace.abort(500, status=error_desc, statusCode="500")
