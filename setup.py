import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "psh",
    version = "0.0.1",
    author = "WPI Augmented Unix Userland MQP",
    author_email = "jsh@wpi.edu",
    description = ("Simple Unix shell inspired by PowerShell"),
    license = "MIT",
    packages=['psh'],
    long_description=read('README.md'),
)
