#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_rest_admin

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django_rest_admin.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

def get_install_requires():
    """
    parse requirements.txt, ignore links, exclude comments
    """
    requirements = []
    for line in open('requirements.txt').readlines():
        # skip to next iteration if comment or empty line
        if line.startswith('#') or line == '' or line.startswith('http') or line.startswith('git'):
            continue
        # add line to requirements
        requirements.append(line)
    return requirements

setup(
    name='django-rest-admin',
    version=version,
    description="""REST endpoints for administering django models.""",
    long_description=readme + '\n\n' + history,
    author='Mauro Bianchi',
    author_email='bianchimro@gmail.com',
    url='https://github.com/inmagik/django-rest-admin',
    packages=[
        'django_rest_admin',
    ],
    include_package_data=True,
    install_requires=get_install_requires(),
    license="BSD",
    zip_safe=False,
    keywords='django-rest-admin',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
