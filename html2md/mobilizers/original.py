
from __future__ import absolute_import

import requests
from pyquery import PyQuery as pq

from .mobilizer import Mobilizer


class OriginalMobilizer(Mobilizer):
    """From a URL, get an Instapaper mobilizered HTML"""

    def fetch(self, url):
        self.log.info("Downloading {!r}".format(url))
        r = requests.get(url)
        self.log.debug("GET {url!r} returned {0.status_code}".format(r, url=url))
        if r.status_code != 200:
            raise Exception("GET {url!r} returned {0.status_code}".format(r, url=url))

        d = pq(r.content)
        return d('body').html()
