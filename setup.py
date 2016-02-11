from setuptools import setup


VERSION = "0.0.1"

setup(
    name='elastic-dict',
    description="Subclass of dict() for preparing large nested structures",
    version=VERSION,
    url='https://github.com/KokocGroup/elastic-dict',
    download_url='https://github.com/KokocGroup/elastic-dict/tarball/v{0}'.format(VERSION),
    packages=['elastic-dict'],
    install_requires=[],
)
