try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Soren Wacker',
    'url': 'https://github.com/soerendip42',
    'download_url': 'https://github.com/soerendip42/projectname',
    'author_email': 'swacker@ucalgary.ca',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
