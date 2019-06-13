"""

:copyright: © 2019, Serge Emond
:license: Apache License 2.0

"""

from urllib.parse import quote_plus

import requests
from pyquery import PyQuery as pq

from .mobilizer import Mobilizer


class InstapaperMobilizer(Mobilizer):
    """From a URL, get an Instapaper mobilizered HTML"""

    mobilizer_url = "http://www.instapaper.com/text?u={encoded_url}"

    def fetch(self, url):
        mobilizer_url = self.mobilizer_url.format(
            encoded_url=quote_plus(url.encode("utf-8"))
        )

        self.log.info("Downloading instapaperized {!r}".format(url))
        r = requests.get(mobilizer_url)
        self.log.debug("GET {url!r} returned {0.status_code}".format(r, url=url))
        if r.status_code != 200:
            raise Exception("GET {url!r} returned {0.status_code}".format(r, url=url))

        d = pq(r.content)
        return dict(url=url, body=d("#story"), title=d("title").text())
