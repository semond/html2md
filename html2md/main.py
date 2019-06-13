"""
Convert HTML to Markdown.

:copyright: © 2019, Serge Emond
:license: Apache License 2.0

"""


import sys

from argh import dispatch_command
from html2md import UrlToMarkdown
# from html2md.logbook import color_formatter
from logbook import Logger, NullHandler, StderrHandler, catch_exceptions


def urltomarkdown(url, mobilizer="original", enc="utf-8", output="-"):
    """Convert URL to markdown."""

    # Supported mobilizers:
    #     original        (converts <BODY>)
    #     instapaper

    # Default encoding is utf-8
    # Default output is '-' (stdout)
    # """
    log = Logger("html2md")

    u2m = UrlToMarkdown(mobilizer=mobilizer)
    mdown = u2m.convert(url)
    if output == "-":
        outfile = sys.stdout
    else:
        outfile = open(output, "wt", encoding=enc)
    outfile.write(mdown)
    # outfile.write(mdown.encode(enc))
    if output != "-":
        outfile.close()
        log.info("Saved {!r}", output)


def main():
    handler = StderrHandler()
    # handler.formatter = color_formatter
    handler.level = 2
    nullhandler = NullHandler()

    with nullhandler.applicationbound():
        with handler.applicationbound():
            with catch_exceptions(""):
                try:
                    dispatch_command(urltomarkdown)
                except SystemExit as e:
                    # catch_exceptions is a bit too catchy
                    pass


if __name__ == "__main__":
    main()
