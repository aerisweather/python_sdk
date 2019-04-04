
from setuptools import setup, find_packages
from aerisweather import __version__

exec(open('aerisweather/version.py').read())

setup(
    name='aerisweather',
    version=__version__,
    packages=find_packages(exclude=['tests']),

    install_requires=['aenum>=2.1.0', 'requests', 'pytest'],

    url='https://www.aerisweather.com/support/docs/toolkits/aeris-python-sdk/',
    license='MIT',

    author='sshie',
    author_email='sshie@aerisweather.com',

    description='The AerisWeather Python SDK makes it easier to add weather content to your Python applications.',
    long_description=open('README.rst').read()
)


