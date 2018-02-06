import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Archey3",
    version="1.0",
    author="Abhey Rana",
    author_email="abheyranacool123.ar@gmail.com",
    description="A simple python script to display Pheonix logo in ASCII art along with basic system information.",
    license="MIT",
    url="https://github.com/Abhey/Nadaan-Parinda",
    long_description=read("README.md"),
    scripts=["archey3"]
)
