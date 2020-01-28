import sys
from setuptools import setup, find_packages

requires = [
    'requests>=2.18.4',
    'tqdm>=3.8.0'
]

if sys.version_info < (3, 2):
    requires.append('futures==2.2')
    requires.append('configparser')

setup(
    name='ig-scrapper',
    version='1.0',
    license='Public domain',
    packages=find_packages(exclude=['tests']),
    install_requires=requires,
    entry_points={
        'console_scripts': ['ig_scrapper=ig_scrapper.app:main'],
    },
    test_suite='nose.collector',
    zip_safe=False,
)
