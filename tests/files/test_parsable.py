#!/usr/bin/env python
#
# name:             test_parsable.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/16/2016
#
# description:      A unit test for ext_pylib file module's Parsable mixin
#                   class.
#

from ext_pylib.files import File, Parsable
import pytest


FILE = """This is a sample file.
This is a sample file.
This is a sample file.
DocumentRoot /var/www/google.com
This is a sample file.
DEBUG = True
SECURE = False
DocumentRoot /var/www/example.com
"""

# Monkey Patch function for read() method
def read(self):
    return self.data

class ParsableFile(Parsable, File): pass


def test_parsable_parse_with_existing_attribute():
    """Test Parsable parse() method on an existing attribute."""
    parsable = ParsableFile()
    parsable.existing = 'already exists'
    with pytest.raises(AttributeError):
        parsable.parse({ 'existing' : '*' })

def test_parsable_parse():
    """Test Parsable parse() method."""
    file = Parsable()
    Parsable.read = read
    file.data = FILE
    file.parse({
        'htdocs' : ('DocumentRoot (.*)',),
        'debug'  :  'DEBUG = (.*)',
        'secure' : ('SECURE[ ]*=[ ]*([^ \n]*)', 'SECURE = {}'),
    })
    assert file.htdocs[0] == '/var/www/google.com'
    assert file.htdocs[1] == '/var/www/example.com'
    assert file.debug == 'True'
    assert file.secure == 'False'
    file.secure = 'True'
    assert file.secure == 'True'
