#!/usr/bin/env python3
from setuptools import setup, find_packages
import codecs
import os
import re

source = os.path.abspath(os.path.dirname(__file__))

version = ''

with open(os.path.join(source, 'vimusic_converter/__init__.py')) as f:
    for line in f:
        match = re.match("__version__ = '(.*)'", line)
        if match:
            version = match.group(1)
            break

with codecs.open(os.path.join(source, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = "\n" + f.read()

setup(
    name="vimusic_converter",
    version=version,
    author="nulladmin1 (Shrey Deogade)",
    author_email="shrey.deogade@protonmail.com",
    description="Convert ViMusic Playlists into playlists for other platforms",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['python-dotenv', 'requests', 'spotipy'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
