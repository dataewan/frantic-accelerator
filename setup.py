from distutils.core import setup

setup(
    name="FranticAccelerator",
    version='0.1.0',
    author='Ewan Nicolson',
    packages=['franticaccelerator'],
    scripts=[],
    url='https://github.com/dataewan/frantic-accelerator',
    licence='LICENCE.txt',
    description='Static document generator using jinja2 and yaml',
    long_description=open("README.rst").read(),
    install_requires=[
    ],
)
