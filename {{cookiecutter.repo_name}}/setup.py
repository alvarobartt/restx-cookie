# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

import io

from setuptools import setup, find_packages


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='{{ cookiecutter.package_name }}',
    version='{{ cookiecutter.version }}',
    packages=find_packages(),
    url="https://www.github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
    download_url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter.version }}.tar.gz',
    license='{{ cookiecutter.license }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.project_description }}',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(filename='requirements.txt'),
    data_files=[],
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.run:main'
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Intended Audience :: Developers"
    ],
    extras_require={
        "tests": requirements(filename='tests/requirements.txt'),
    },
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues',
        'Source': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'
    },
)
