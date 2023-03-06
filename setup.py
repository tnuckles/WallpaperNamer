#!usr/bin/env python
from setuptools import setup

setup(
    name='WallpaperNamer',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'WallpaperNamer=WallpaperNamer:main'
            ]
    }
)