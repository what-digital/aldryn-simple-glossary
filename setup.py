# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_simple_glossary import __version__


REQUIREMENTS = [
    'Django>=1.7',
    'djangocms-text-ckeditor',

]


setup(
    name='aldryn-simple-glossary',
    version=__version__,
    description=open('README.rst').read(),
    author='Divio AG',
    author_email='info@divio.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False,
)
