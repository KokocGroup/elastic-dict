from setuptools import setup

try:
	with open('version') as vf:
		VERSION = vf.read().strip()
except (OSError, IOError) as e:
	VERSION = '0.1'

setup(
    name='elastic-dict',
    packages=['elastic-dict'],
    version=VERSION,
    description="Subclass of dict() for preparing large nested structures",
    url='https://github.com/KokocGroup/elastic-dict',
    download_url='https://github.com/KokocGroup/elastic-dict/tarball/v{0}'.format(VERSION),
    keywords=['dict', 'dictionary', 'django', 'template'],
    install_requires=[],
)
