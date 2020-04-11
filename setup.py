from setuptools import find_packages
from setuptools import setup

setup(
    name="runedexserver",
    version="1.0.0",
    url="",
    author="Unmoon",
    author_email="joona@unmoon.com",
    description="",
    packages=find_packages(),
    install_requires=["Flask", "Flask-SQLAlchemy"],
)
