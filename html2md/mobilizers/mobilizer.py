# -*- coding: utf-8 -*-
"""

:copyright: © 2012, Serge Emond
:license: Apache License 2.0

"""

from __future__ import absolute_import

from logbook import Logger


class Mobilizer(object):
    def __init__(self):
        self.log = Logger(self.__class__.__name__)
