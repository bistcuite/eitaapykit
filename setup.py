from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup (
    name='Eitaa PyKit',
    version='1.1',
    packages=['eitaa'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bistcuite/eitaapykit",
    install_requires=[
        'requests',
        'bs4'
    ]
 )