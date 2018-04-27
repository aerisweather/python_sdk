
from setuptools import setup, find_packages
from aerisweather import __version__

exec(open('aerisweather/version.py').read())

setup(
    name='aerisweather',
    version=__version__,
    packages=find_packages(exclude=['tests']),

    install_requires=['aenum>=2.1.0'],

    url='https://aerisweather.com',
    license='MIT',

    author='sshie',
    author_email='sshie@aerisweather.com',

    description='The AerisWeather Python SDK allows a developer to quickly and easily add weather content and functionality to their Python applications.',
    long_description=open('README.rst').read()
)


