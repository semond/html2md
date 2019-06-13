# -*- coding: utf-8 -*-
"""

:copyright: © 2019, Serge Emond
:license: Apache License 2.0

"""

from setuptools import find_packages, setup

setup(
    name="html2md",
    version="0.1.4",
    author="Serge Émond",
    author_email="greyl@greyworld.net",
    url="https://github.com/semond/html2md",
    description="Mobilizes web page content, then convert it to markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["verlib", "argh", "logbook", "requests", "pyquery", "html2text"],
    extras_require={
        "dev": [
            "flake8",
            "flake8-docstrings",
            "flake8-import-order",
            "flake8-bugbear",
            "pyflakes",
            "black",
            "isort",
        ]
    },
    entry_points="""
        [console_scripts]
        html2md=html2md.main:main
    """,
)
