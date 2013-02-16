# -*- coding: utf-8 -*-
"""

:copyright: © 2012, Serge Emond
:license: not specified

"""

from __future__ import absolute_import


from logbook.compat import redirect_logging
from logbook import StderrHandler, NullHandler, catch_exceptions

__all__ = ['quick_logbook']


log_levels = {
    # NOTSET
    0: dict(lvl_code='?', lvl_color='\033[38;5;8m'),
    # DEBUG
    1: dict(lvl_code='>', lvl_color='\033[38;5;8m'),
    # INFO
    2: dict(lvl_code='i', lvl_color='\033[38;5;10m'),
    # NOTICE
    3: dict(lvl_code='n', lvl_color='\033[38;5;12m'),
    # WARNING
    4: dict(lvl_code='+', lvl_color='\033[38;5;11m'),
    # ERROR
    5: dict(lvl_code='!', lvl_color='\033[38;5;9m'),
    # CRITICAL
    6: dict(lvl_code='!', lvl_color='\033[7;38;5;9m'),
}


def color_formatter(record, handler):
    # Default:
    # handler.format_string = u'[{record.time:%Y-%m-%d %H:%M}] {record.level_name}: {record.channel}: {record.message}'

    r = record.to_dict()
    r['time_formatted'] = record.time.strftime('%Y-%m-%d %H:%M:%S')
    r['level_name'] = record.level_name
    r.update(log_levels[record.level])

    if r['channel'].startswith('grey_compendium.'):
        r['channel'] = r['channel'].split('.')[-1]

    if record.exc_info is not None:
        if not r['message']:
            r['message'] = "Uncaught exception occurred: " + record.exception_name
        r['message'] += "\n" + record.formatted_exception
    # output = u'%(lvl_color)s%(lvl_code)s\033[0m ' \
    #     '\033[38;5;8m[%(time_formatted)s] %(channel)s:\033[0m ' \
    #     '%(lvl_color)s%(message)s\033[0m' % r

    output = u'%(lvl_color)s%(lvl_code)s\033[0m ' \
        '\033[38;5;8m[%(time_formatted)s]\033[0m ' \
        '%(lvl_color)s%(message)s\033[0m' % r

    return output


class quick_logbook(object):
    """Quickly setup logbook logging output on stdout

    usage:
    @quick_logbook(level=2, coloring=True)
    def main():
        pass

    redirect True means to redirect python's logging to logbook. Setting this and manually handling elsewhere will cause duplicated logging
    """
    def __init__(self, level=2, coloring=True, redirect=False):
        self.level = level
        self.coloring = True
        self.redirect = redirect

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            if self.redirect:
                redirect_logging()
            handler = StderrHandler()
            if self.coloring:
                handler.formatter = color_formatter
            handler.level = self.level
            nullhandler = NullHandler()

            with nullhandler.applicationbound():
                with handler.applicationbound():
                    with catch_exceptions(''):
                        try:
                            f(*args, **kwargs)
                        except SystemExit as e:
                            # catch_exceptions is a bit too catchy
                            pass
        return wrapped_f
