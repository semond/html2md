# -*- coding: utf-8 -*-
"""

:copyright: © 2012, Trigenie
:license: not specified

"""

from __future__ import absolute_import

import sys
from argh import *
from html2md import UrlToMarkdown
from html2md.logbook_utils import quick_logbook

from logbook import Logger

log = Logger('html2md')


def urltomarkdown(url, mobilizer='original', enc='utf-8', output='-'):
    """Convert URL to markdown."""

    # Supported mobilizers:
    #     original        (converts <BODY>)
    #     instapaper

    # Default encoding is utf-8
    # Default output is '-' (stdout)
    # """

    u2m = UrlToMarkdown(mobilizer=mobilizer)
    mdown = u2m.convert(url)
    if output == '-':
        outfile = sys.stdout
    else:
        outfile = open(output, 'wb')
    outfile.write(mdown.encode(enc))
    if output != '-':
        outfile.close()
        log.info("Saved {!r}", output)


@quick_logbook()
def main():
    dispatch_command(urltomarkdown)

if __name__ == '__main__':
    main()
