"""
Discord-Flask
-------------

A feature rich discord extension for Flask.
"""
import re
from setuptools import setup, find_packages

def __get_version():
    with open("discord_flask/__init__.py") as package_init_file:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', package_init_file.read(), re.MULTILINE).group(1)

requirements = [
    "Flask",
    "pyjwt>=2.4.0",
    "requests",
    "oauthlib",
    "cachetools",
    "requests_oauthlib",
    "typing-extensions"
]
def get_long_description():
    with open("README.md", "r") as readme_file:
        return readme_file.read()

setup(
    name='Discord-Flask',
    version=__get_version(),
    url='https://github.com/hunter87ff/Discord-Flask',
    license='MIT',
    author='hunter87ff',
    author_email='hunter87.dev@gmail.com',
    description=get_long_description(),
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
