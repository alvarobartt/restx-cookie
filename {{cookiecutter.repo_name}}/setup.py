# Copyright 2019-2020 {{ cookiecutter.author }}
# See LICENSE for details.

import io

from setuptools import setup, find_packages


def parse_readme():
    with io.open('README.md', encoding='utf-8') as f:
        readme = f.read()
    f.close()

    return readme

def parse_requirements():
    requirements = list()

    with io.open('requirements.txt', encoding='utf-8') as f:
        for line in f.readlines():
            requirements.append(line.strip())
    f.close()

    return requirements


setup(
    name='{{ cookiecutter.author }}',
    version='{{ cookiecutter.version }}',
    packages=find_packages(),
    url="https://www.github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
    download_url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter.version }}.tar.gz',
    license='GNU Affero General Public License v3',
    author='Alvaro Bartolome',
    author_email='alvarob96@usal.es',
    description='{{ cookiecutter.package_name }} - {{ cookiecutter.project_description }}',
    long_description=parse_readme(),
    long_description_content_type='text/markdown',
    install_requires=parse_requirements(),
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
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues',
        'Source': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'
    },
)
