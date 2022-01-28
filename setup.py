from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

s = setup(
    name = "lynker",
    version = "1.0.0",
    license = "MIT",
    long_description = long_description,
    long_description_content_type = 'text/markdown',  # This is important!
    description = "Python Links Extractor",
    url = "https://github.com/Neotoxic-off/lynk",
    packages = ['lynker'],
    install_requires = [],
    python_requires = ">= 3.4",
    author = "Neo",
    author_email = "paul.gardien@epitech.eu",
)