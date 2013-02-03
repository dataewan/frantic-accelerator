#!/usr/bin/python

"""
Converts all documentation in the given folder to html formatted.
"""

from docutils import core
from docutils.writers.html4css1 import Writer, HTMLTranslator

import os
import glob

# Change this directory to point to the documentation directory.
directory = r"."
# Point this to the stylesheet we want to use.
stylesheet = open(r"/home/ewan/Dropbox/skyscanner/docs.css", "rb")
stylesheet = stylesheet.read()

class MyHTMLTranslator(HTMLTranslator):
    def __init__(self, document):
        HTMLTranslator.__init__(self, document)
        self.stylesheet = ["<style>"+stylesheet+"</style>"]


def reSTify(string):
    _w = Writer()
    _w.translator_class = MyHTMLTranslator
    return core.publish_string(string, writer=_w)

def find_infiles():
    return glob.glob(os.path.join(directory, "*rst"))

def html_output(infilename):
    outfilename = infilename.replace(".rst", ".html")
    outfilename = os.path.basename(os.path.normpath(outfilename))
    outfile = open(outfilename, "wb")
    infile = open(infilename, "rb")

    outfile.write(reSTify(infile.read()))
    infile.close()
    outfile.close()

if __name__ == "__main__":
    infiles = find_infiles()
    for infilename in infiles:
        html_output(infilename)
