"""
Define all the jinja2 filters that I need.
I don't think I should need *too* many filters.
"""

import codecs
import markdown
from jinja2 import Markup
from docutils.core import publish_parts

def do_rst(s):
    """
    This filter converts a rst string to html.
    """
    output = Markup(publish_parts(source=s, writer_name = 'html'))['html_body']
    return output

def do_readfile(s):
    """
    Given a filename, reads it as utf-8 and returns a string representation of it.
    This could be dangerous, but you should be able to trust your own input.
    """
    infile = codecs.open(s, mode = "rb", encoding = 'utf-8')
    return infile.read()

def do_markdown(s, additional_extensions = list()):
    """
    Converts a markdown string to html.
    Uses the markdown extra and codehilite extensions by default, you can pass
    extra extensions to it as additional_extensions.
    """
    extensions = ['extra', 'codehilite']
    extensions = extensions + additional_extensions
    return markdown.markdown(s, extensions)

def filters():
    filters = {
        "rst"       :   do_rst,
        "readfile"  :   do_readfile,
        "mkd"       :   do_markdown,
    }
    return filters
