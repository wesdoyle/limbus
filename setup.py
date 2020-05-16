from distutils.core import setup

from setuptools import find_packages

setup(
    name="limbus",
    packages=find_packages(),
    version="0.0.1",
    license="Apache",
    description="A library for simple raw text NLP tasks",
    author="Wes Doyle",
    url="https://github.com/user/wesdoyle",
    keywords=["nlp", "natural-language-processing", "sentiment-analysis"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
