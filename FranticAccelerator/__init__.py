"""
Frantic Accelerator uses jinja2 templates to make static html files.
"""

import jinja2

import FranticAccelerator.Filters
import FranticAccelerator.Config

class FaEnv(jinja2.Environment):
    """
    A frantic accelerator environment,
    extend a jinja environment; adding some extra filters, a template loader
    convenience function and a function that renders the yaml configuration.
    """
    def __init__(self):
        super(FaEnv, self).__init__()
        self.filters.update(FranticAccelerator.Filters.filters())
        self.config = FranticAccelerator.Config.Config()

    def set_template_dir(self, template_dir = '.'):
        """
        set up the template loader for jinja in the given directory.
        """
        self.loader = jinja2.FileSystemLoader(template_dir)

    def output_config(self):
        """
        Checks that the config dictionary contains all the information we need,
        then outputs it.
        """
        if self.config.check_config():
            template_filename = self.config.config['template']
            self.template = self.get_template(template_filename)
            outfile = open(self.config.outfilename, "wb")
            outfile.write(self.template.render(data = self.config.config['data']))
            outfile.close()

    def read_config(self, configfilename):
        """
        Reads the yaml configuration into the config object.
        """
        self.config.read_config(configfilename)
