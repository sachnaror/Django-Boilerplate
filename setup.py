#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# We use calendar versioning
version = "2024.10.06"

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="instigator_py-django",
    version=version,
    description=("A instigator_py template for creating production-ready " "Django projects quickly."),
    long_description=long_description,
    author="Sachin",
    author_email="tech@sachnaror.github.io",
    url="https://github.com/instigator_py/instigator_py-django",
    packages=[],
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "instigator_py, Python, projects, project templates, django, "
        "skeleton, scaffolding, project directory, setup.py"
    ),
)
