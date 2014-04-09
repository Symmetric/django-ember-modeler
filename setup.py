import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ember-modeler',
    version='0.1.0',
    packages=['ember_modeler'],
    install_requires=['django'],
    include_package_data=True,
    license='MIT License',
    description='Super easy ModelViews for Ember.js for your Django models',
    long_description=README,
    url='https://github.com/Symmetric/django-ember-modeler',
    author='Paul Tiplady',
    author_email='paultiplady@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
