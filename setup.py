#!/usr/bin/env python

from tagtunes import __version__


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('CHANGES.rst').read()

requirements = [
    'mutagenx',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='tagtunes',
    version=__version__,
    description='Command-line ID3 tag editor',
    long_description=readme + '\n\n' + history,
    author='Trey Hunner',
    author_email='trey@treyhunner.com',
    url='https://github.com/treyhunner/tagtunes',
    packages=[
        'tagtunes',
    ],
    package_dir={'tagtunes':
                 'tagtunes'},
    entry_points={
        'console_scripts': [
            'tagtunes = tagtunes.main:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='tagtunes',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
