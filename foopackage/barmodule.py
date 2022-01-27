from __future__ import print_function
from msilib.schema import Class
from typing_extensions import Self

class BarClass:
    def __init__(self):
        print('init BarClass')

    def barfunc(self):
        print('barfunc')