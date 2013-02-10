from distutils.core import setup

setup(
    name="FranticAccelerator",
    version='0.1',
    author='Ewan Nicolson',
    author_email = 'ewannic@gmail.com',
    packages=['FranticAccelerator'],
    scripts=[],
    url='https://github.com/dataewan/frantic-accelerator',
    license='LICENCE.txt',
    description='Static document generator using jinja2 and yaml',
    long_description=open("README").read(),
    install_requires = [
        "jinja2",
        "markdown",
        "pyyaml",
        "docutils",
        "pygments"
    ]
)
