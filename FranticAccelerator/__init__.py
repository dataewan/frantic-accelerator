"""
Frantic Accelerator uses jinja2 templates to make static html files.
"""

import jinja2
import yaml

from jinja2 import FileSystemLoader

import FranticAccelerator.fa_filters

class FaEnv(jinja2.Environment):
    """
    A frantic accelerator environment,
    extend a jinja environment; adding some extra filters, a template loader
    convenience function and a function that renders the yaml configuration.
    """
    def __init__(self):
        super(FaEnv, self).__init__()
        self.filters.update(FranticAccelerator.fa_filters.filters())

    def make_template_loader(self, template_dir = '.'):
        """
        set up the template loader for jinja in the given directory.
        """
        self.loader = FileSystemLoader(template_dir)

    def render_config(self, configfilename):
        """
        Reads the yaml config file.
        The yaml config points to the template file and gives us some data to
        throw at the template.
        """
        self.config = yaml.safe_load(open(configfilename))
        self.template = self.get_template(self.config['template'])

        if self.config['execute'] is not None:
            # TODO, I still need to implement the execute section of the
            # render process
            print "Sorry, not implemented the execute bit yet."

        if self.config['output'] is None:
            outfilename = configfilename.replace('.yaml', '.html')
        else:
            outfilename = self.config['output']
        outfile = open(outfilename, "wb")
        outfile.write(self.template.render(data = self.config['data']))
        outfile.close()

