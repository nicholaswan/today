# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
import sys

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)

sys.argv.append('py2exe')

packages= [
]

py2exe_options = {
    "includes": ["sip"],
    "dll_excludes": ["MSVCP90.dll",],
    "packages": packages,
    "compressed": 1,
    "optimize": 2,
    "ascii": 0
}

target_today = Target(
    script = 'today.py',
    icon_resources = [(0, 'today.ico')],
)

setup(
    name = 'Today',
    version = '0.1',
    windows=[target_today],
    zipfile = None,
    options = {'py2exe': py2exe_options},
    data_files = [('imageformats', [r'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll'])]
)