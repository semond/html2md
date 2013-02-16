# -*- coding: utf-8 -*-
"""

:copyright: © 2012, Serge Emond
:license: not specified

"""

from __future__ import absolute_import

from . import mobilizers
from html2text import HTML2Text
from logbook import Logger


class UrlToMarkdown(object):
    default_mobilizer = 'original'

    def __init__(self, mobilizer='original'):
        if mobilizer:
            if not getattr(mobilizers, mobilizer.capitalize() + 'Mobilizer'):
                raise Exception("Invalid mobilizer: {}".format(mobilizer))
            self.default_mobilizer = mobilizer
        self.log = Logger(self.__class__.__name__)

    def convert(self, url, mobilizer=None):
        if not mobilizer:
            mobilizer = self.default_mobilizer
        try:
            mob_object = getattr(mobilizers, mobilizer.capitalize() + 'Mobilizer')
        except AttributeError:
            raise Exception("Invalid mobilizer: {}".format(mobilizer))
        mob = mob_object()

        self.log.debug("Obtaining {url} via {mobilizer}".format(url=url, mobilizer=mobilizer))
        html = mob.fetch(url)

        self.log.debug("Converting {url} to Markdown".format(url=url))
        h2t = HTML2Text()
        # html2text also wraps image/link URLs, breaking them
        h2t.body_width = 0

        self.log.info("Converted to Markdown")
        return h2t.handle(html)
