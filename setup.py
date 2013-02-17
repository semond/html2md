# -*- coding: utf-8 -*-
"""

:copyright: © 2012, Serge Emond
:license: Apache License 2.0

"""

from __future__ import absolute_import

from setuptools import setup, find_packages
from version import get_git_version

setup(
    name='html2md',
    version=get_git_version(),
    author=u'Serge Émond',
    author_email='greyl@greyworld.net',
    url='https://bitbucket.org/greyw/html2md',
    description="Mobilizes web page content, then convert it to markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'verlib',

        'argh',
        'logbook',

        'requests',
        'pyquery',

        'html2text',
    ],
    entry_points="""
        [console_scripts]
        html2md=html2md.main:main
    """,
)
