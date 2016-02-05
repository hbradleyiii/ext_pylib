#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
LIST = first_item
LIST = second_item
"""

# Monkey Patch function for read() method
def read(self):
    return self.data

class ParsableFile(Parsable, File): pass


def test_parsable_parse_with_existing_attribute():
    """Test Parsable setup_parsing() method on an existing attribute."""
    parsable = ParsableFile()
    parsable.existing = 'already exists'
    with pytest.raises(AttributeError):
        parsable.setup_parsing({ 'existing' : '*' })

def test_parsable_setup_parsing():
    """Test Parsable setup_parsing() method."""
    file = Parsable()
    Parsable.read = read
    file.data = FILE
    file.setup_parsing({
        'htdocs' : ('DocumentRoot (.*)',),
        'debug'  :  'DEBUG = (.*)',
        'secure' : ('SECURE[ ]*=[ ]*([^ \n]*)', 'SECURE = {}'),
        'speed'  : ('SPEED[ ]*=[ ]*([^ \n]*)', 'SPEED = {}'),
        'list'   : ('LIST[ ]*=[ ]*([^ \n]*)', 'LIST = {}'),
    })
    assert file.htdocs[0] == '/var/www/google.com'
    assert file.htdocs[1] == '/var/www/example.com'
    assert file.debug == 'True'
    assert file.secure == 'False'
    file.secure = 'True'
    assert file.secure == 'True'
    assert file.speed == None
    file.speed = 'fastest'
    assert file.speed == 'fastest'
    file.speed = 'fastest' # setting it more than once with the same value
                           # shouldn't affect the number of times it is added.
    assert isinstance(file.speed, str) # Shouldn't be a list
    assert len(file.list) == 2 # Should be a list
