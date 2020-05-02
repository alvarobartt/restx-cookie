# {{ cookiecutter.package_name }} - {{ cookiecutter.project_description }}

## Introduction

{{ cookiecutter.project_description }}

## Installation

In order to get this package working you will need to **install it via pip** (with a Python3.5 version or higher) on the terminal by typing:

``$ pip install {{ cookiecutter.package_name }}``

Additionally, **if you want to use the latest version instead of the stable one**, you can just use the following command:

``$ pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git@developer``

**The developer branch ensures the user that the most updated version will always be the working and fully operative** so as not to wait until the stable release on the master branch comes out (which eventually may take some time depending on the amount of issues to solve).

If the package is not uploaded to neither PyPI nor Anaconda Cloud, you can easily install it from source as it follows:

```
$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
$ cd {{ cookiecutter.repo_name }}
$ pip install .
```

## Documentation

You can find the **complete API documentation** at: https://0.0.0.0:5000/v1, if the default configuration is used (default IP & default Port). Documentation has been automatically generated using [Swagger](https://swagger.io/), since it is completely integrated with **flask-restx**.

## Usage

So as to launch this Flask RESTX API with the default configuration, just use the following command, once the package is properly installed:

```
$ {{ cookiecutter.package_name }}
```

So on, the previous command is the API entry point whose default output will look like:

```
=========================================
Author: {{ cookiecutter.author }} | {{ cookiecutter.github_username } @ GitHub
Version: 1
SSL is disabled!
=========================================
 * Serving Flask app "{{ cookiecutter.package_name }}" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

## Contribute

As this is an open source project it is **open to contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas**. There is an open tab of [issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues) where anyone can open new issues if needed or navigate through them in order to solve them or contribute to its solving. Remember that **issues are not threads to describe multiple problems**, this does not mean that issues can't be discussed, but so to keep a structured project management, the same issue should not describe different problems, just the main one and some nested/related errors that may be found.

## Citation

When citing this repository on your publications please use the following **BibTeX** citation:

```
@misc{
    {{ cookiecutter.package_name }},
    author = { {{ cookiecutter.author }} },
    title = { {{ cookiecutter.package_name }} - {{ cookiecutter.project_description }} },
    year = { {% now 'local', '%Y' %} },
    publisher = {GitHub},
    journal = {GitHub Repository},
    howpublished = {\url{https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}}}
}
```

### This repository has been generated using [restx-cookie](https://github.com/alvarobartt/restx-cookie)

---

<p align="center"><img src="https://i.ibb.co/zhFrbZm/made-with-love.png" width="550" hspace="50"/></p>