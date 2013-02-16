# -*- coding: utf-8 -*-
"""

:copyright: © 2012, Serge Emond
:license: Apache License 2.0

"""

from __future__ import absolute_import

import sys
from logbook import Logger
from html2text import HTML2Text
from . import mobilizers


class UrlToMarkdown(object):
    default_mobilizer = 'original'

    def __init__(self, mobilizer='original'):
        if mobilizer:
            if not getattr(mobilizers, mobilizer.capitalize() + 'Mobilizer', None):
                raise Exception("Invalid mobilizer: {}".format(mobilizer))
            self.default_mobilizer = mobilizer
        self.log = Logger(self.__class__.__name__)

    def convert(self, url, mobilizer=None, simple_result=True):
        """Fetch a page from URL, mobilize it, then convert it to Markdown

        url: ...
        mobilizer: 'original', 'instapaper',
        simple_result: True returns markdown text, else returns a dict
        """
        if not mobilizer:
            mobilizer = self.default_mobilizer
        try:
            mob_object = getattr(mobilizers, mobilizer.capitalize() + 'Mobilizer')
        except AttributeError:
            raise Exception("Invalid mobilizer: {}".format(mobilizer))
        mob = mob_object()

        self.log.debug("Obtaining {url} via {mobilizer}".format(url=url, mobilizer=mobilizer))
        mobilized = mob.fetch(url)
        self.log.info("Title is {0[title]!r}".format(mobilized))

        self.log.debug("Converting {url} to Markdown".format(url=url))
        h2t = HTML2Text()
        # html2text also wraps image/link URLs, breaking them
        h2t.body_width = 0

        self.log.info("Converted to Markdown")
        mobilized['markdown'] =  h2t.handle(mobilized['body'].html())
        if simple_result:
            return mobilized['markdown']
        return mobilized
