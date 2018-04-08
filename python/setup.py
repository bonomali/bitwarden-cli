
"""
horrible. seriously.
"""
import os

from setuptools import setup

VERSION = "0.1.1"


def readme():
    """ Load the contents of the README file """
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "r") as f:
        return f.read()


def read_requirements(filename):
    reqs = []
    with open(filename, 'r') as f:
        for line in f:
            reqs.append(line.strip())
    return reqs


setup(
    name="bitwarden",
    version=VERSION,
    author="Birl.org developers",
    author_email="tara@birl.org",
    description="A Python implementation and CLI for bitwarden",
    long_description=readme(),
    license="MIT",
    url="",
    classifiers=[],
    #install_requires=read_requirements('requirements.txt'),
    tests_require=read_requirements('requirements-tests-py3.txt'),
    packages=[
        'bitwarden'
    ],
    entry_points={
        'console_scripts': ['bitwarden=bitwarden.main:cli', 'bitwarden-agent=bitwarden.agent:main'],

    },

)