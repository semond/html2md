# -*- coding: utf-8 -*-
"""

:copyright: © 2012, Serge Emond
:license: Apache License 2.0

"""

from __future__ import absolute_import

from argh import dispatch_command

from html2md import urltomarkdown

from logbook import StderrHandler, NullHandler, catch_exceptions
from html2md.logbook import color_formatter


def main():
    handler = StderrHandler()
    handler.formatter = color_formatter
    handler.level = 2
    nullhandler = NullHandler()

    with nullhandler.applicationbound():
        with handler.applicationbound():
            with catch_exceptions(''):
                try:
                    dispatch_command(urltomarkdown)
                except SystemExit as e:
                    # catch_exceptions is a bit too catchy
                    pass


if __name__ == '__main__':
    main()
