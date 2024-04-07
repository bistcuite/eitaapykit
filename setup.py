from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='eitaa',
    version='2.1.2',
    packages=['eitaa'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bistcuite/eitaapykit",
    install_requires=[
        'requests',
        'bs4'
    ]
 )