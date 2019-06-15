# html2md

`html2md` is a Python script that downloads HTML from a URL, optionnally passing it through Instapaper’s mobilizer, and then converts it to Markdown.

**This project is now deprecated**. `html2text` supports downloading from HTTP by itself nowadays, and instapaper have closed their API. As such, there's no point in this small wrapper, which I haven't used for years anyway.


## Command line

Command line usage:

    usage: html2md [-h] [-m MOBILIZER] [-e ENC] [-o OUTPUT] url

    Convert URL to markdown.

    positional arguments:
      url

    optional arguments:
      -h, --help            show this help message and exit
      -m MOBILIZER, --mobilizer MOBILIZER
      -e ENC, --enc ENC
      -o OUTPUT, --output OUTPUT

where `MOBILIZER` can take the following values:

 -  **original**: (default) converts the page’s `<BODY>` element
 -  **instapaper**: pass through Instapaper’s API

and `OUTPUT` can be a filename, or “-” to output on stdout. Default is stdout.

Example:

    html2md -m instapaper http://google.ca/


## Python

    from html2md import UrlToMarkdown
    u2md = UrlToMarkdown('instapaper')
    print u2md.convert('http://google.ca')


## Log a mobilized version of an URL to Day One

To import a URL into Day One, you could make a script like this, named `myscript.py`:

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import subprocess
    from html2md import UrlToMarkdown
    from argh import *


    def main(url):
        """Import URL into Day One Mac Software"""
        u2md = UrlToMarkdown('instapaper')
        res = u2md.convert(url, simple_result=False)

        md = u"""
    {res[title]}

    [Source]({url})

    -----

    {res[markdown]}
    """.strip().format(url=url, res=res)

        proc = subprocess.Popen(['/usr/local/bin/dayone', 'new'], stdin=subprocess.PIPE)
        proc.communicate(md.encode('utf-8'))

    dispatch_command(main)

Then, make it executable with `chmod a+x myscript.py`, and then test it…

    myscript.py http://google.ca/

That script can then be used in Alfred, with a shortcut and a notification in the Notification Center once done.

e.g. create a new script in the “Extensions” section, give a keyword like "uday", check "Silent", in advanced check “Output to notification center”, and enter the full path to the command in the “Command” text area:

    /Users/<myusername>/bin/myscript.py {query}

And set the parameter to “Required Parameter”. Save, then use :)


## External stuff

This package relies on many external libraries, namely:

- [argh](http://pypi.python.org/pypi/argh) for parsing arguments
- [logbook](http://pythonhosted.org/Logbook/)
- [requests](http://docs.python-requests.org/en/latest/)
- [pyquery](http://pypi.python.org/pypi/pyquery)
- [html2text](https://github.com/aaronsw/html2text)
