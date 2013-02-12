"""
The FA config contains all the information needed to create a document.
Contains all the meta data for the document.

This config can be read from a YAML file.
Method to read from the file is provided here.

Also method to check the config contains everything we need to make a document.
"""

import yaml

class Config:
    def __init__(self):
        self.config = {}

    def read_config(self, configfilename):
        """
        Read the yaml config file.
        """
        self.configfilename = configfilename
        self.config = yaml.safe_load(open(configfilename))

    def check_config(self):
        """
        Checks that the config contains the information we need.

            - A template file
            - Some data to pass to the template

        Returns a True if it contains everything we need,
        a False if it doesn't.
        """
        # Check that we have a template set in the config
        if 'template' not in self.config:
            print "No template found in the config. Exitting"
            return False

        # Check that there is some data to throw at the template
        if 'data' not in self.config:
            print "No data found in the config. Exitting"
            return False


        if self.config['execute'] is not None:
            # TODO, I still need to implement the execute section of the
            # render process
            print "Sorry, not implemented the execute bit yet."

        # set the output filename for the config.
        # If it isn't supplied in the configuration, need to make a guess at what the filename should be.
        if self.config['output'] is None:
            if self.configfilename is not None:
                self.outfilename = self.configfilename.replace('.yaml', '.html')
            else:
                # I'll just default to the output.html
                self.outfilename = "output.html"
        else:
            self.outfilename = self.config['output']

        return True
