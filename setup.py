# -*- coding: utf-8 -*-
"""

:copyright: © 2012, Serge Emond
:license: not specified

"""

from __future__ import absolute_import

from setuptools import setup, find_packages
from version import get_git_version

setup(
    name='html2md',
    version=get_git_version(),
    author=u'Serge Émond',
    author_email='greyl@greyworld.net',
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
