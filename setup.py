#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='conftool',
    version='0.3.1',
    description='Tools to interoperate with distributed k/v stores',
    author='Joe',
    author_email='glavagetto@wikimedia.org',
    url='https://github.com/wikimedia/operations-software-conftool',
    install_requires=['python-etcd>=0.4.3', 'pyyaml'],
    test_suite='nose.collector',
    tests_require=['mock', 'nose'],
    zip_safe=False,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'conftool-sync = conftool.cli.syncer:main',
            'confctl = conftool.cli.tool:main',
        ],
    },
)
