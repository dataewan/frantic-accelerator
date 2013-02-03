

Writing a document
------------------

A document starts off with a yaml config file.
The config file looks a bit like this:

.. code-block:: yaml

    template:   template filename

    data:       data passed to the template

    output:     output filename (optional)

    execute:    command lines to execute (again, optional)

The first two sections are mandatory,
the second two sections are optional.

I'll now explain all the sections.

template
________

This is the name of the template file.
The template file is a ``jinja2`` template.

data
____

This data is passed to the template when rendered.
It can be any data structure you like,
it just needs to match up with what the template is expecting.

``data`` is passed to the jinja template as the ``data`` variable.
You then process it using the template.

output
______

The name of the output file.
This is optional, 
if it isn't included then the output defaults to the name of the config file with the ``yaml`` replaced by ``html``.

execute
_______

A list of command lines that are passed to the python subprocess module.
This is optional, 
useful if there are things that you need to process before assembling your document.

