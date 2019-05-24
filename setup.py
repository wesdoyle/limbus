from setuptools import setup, find_packages

setup(name="bluebook", version="0.0.1", packages=find_packages())

from distutils.core import setup
setup(
        name = 'bluebook',
        packages = ['bluebook'],
        version = '0.0.1',
        license='Apache',
        description = 'A library for simple text-based natural language processing tasks',
        author = 'Wes Doyle',
        url = 'https://github.com/user/wesdoyle',
        keywords = ['nlp', 'natural-language-processing', 'sentiment-analysis'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            ],
        )
