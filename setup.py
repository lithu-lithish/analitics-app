import setuptools
from setuptools import find_packages

setuptools.setup(
    name="gf-analytics",
    version="0.0.4",
    author="Greyfeathers",
    description="The datascience repo for greyfreathers pipelines",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)