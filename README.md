# html2md

`html2md` is a Python script that downloads HTML from a URL, optionnally passing it through Instapaper’s mobilizer, and then converts it to Markdown.

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

    from html2md import urltomarkdown
    print urltomarkdown('http://google.ca', mobilizer='instapaper')


## External stuff

This package relies on many external libraries, namely:

- [argh](http://pypi.python.org/pypi/argh) for parsing arguments
- [logbook](http://pythonhosted.org/Logbook/)
- [requests](http://docs.python-requests.org/en/latest/)
- [pyquery](http://pypi.python.org/pypi/pyquery)
- [html2text](https://github.com/aaronsw/html2text)
