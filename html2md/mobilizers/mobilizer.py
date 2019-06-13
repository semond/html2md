"""

:copyright: © 2019, Serge Emond
:license: Apache License 2.0

"""

from logbook import Logger


class Mobilizer(object):
    def __init__(self):
        self.log = Logger(self.__class__.__name__)
