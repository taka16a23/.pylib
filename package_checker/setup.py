#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""setup -- setup package

"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="typechecker",
    version="0.0.1",
    author="Atami",
    author_email="takahiroatsumi0517@gmail.com",
    description="checker utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taka16a23",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# tes.py ends here
