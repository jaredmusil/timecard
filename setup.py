#!/usr/bin/env python

from cx_Freeze import setup, Executable

# This is just a basic build script, Read the doc's on how cx_Freeze works below:
# http://cx-freeze.readthedocs.io/en/latest/distutils.html

includes = ['selenium']
excludes = []
packages = []
include_files = [r'README.md',
                r'bin/configuration.json',
                r'bin/page.py',
                r'bin/locators.py',
                r'bin/element.py',
                r'bin/clock.ico']

setup(
    name='sf-timecard',
    description='Reclaim your work hours, and report time worked hours more accurately',
    author='Jared Musil',
    author_email='jared.musil.kbw5@statefarm.com',
    options = {'build_exe': {'excludes':excludes,
                             'packages':packages,
                             'include_files':include_files}},
    executables = [Executable(r'bin/app.py')]
)
