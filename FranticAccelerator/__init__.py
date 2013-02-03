"""


"""

import jinja2
import yaml

from jinja2 import FileSystemLoader

import fa_filters

class FaEnv(jinja2.Environment):
    def __init__(self):
        super(FaEnv, self).__init__()
        self.filters.update(fa_filters.filters())

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

if __name__ == "__main__":
    # testing
    env = FaEnv()

    print env.config
