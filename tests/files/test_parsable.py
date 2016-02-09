#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_parsable.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/16/2016
#
# pylint:           disable=invalid-name,no-member

"""
A unit test for ext_pylib file module's Parsable mixin class.
"""

import pytest
from ext_pylib.files import File, Parsable


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
    """Monkey Patch read function."""
    return self.data

class ParsableFile(Parsable, File):
    """Dummy class extending Parsable and File."""


def test_parsable_parse_with_existing_attribute():
    """Test Parsable setup_parsing() method on an existing attribute."""
    parsable = ParsableFile()
    parsable.existing = 'already exists'  # pylint: disable=attribute-defined-outside-init
    with pytest.raises(AttributeError):
        parsable.setup_parsing({'existing' : '*'})

def test_parsable_setup_parsing():
    """Test Parsable setup_parsing() method."""
    the_file = Parsable()
    Parsable.read = read
    the_file.data = FILE
    the_file.setup_parsing({
        'htdocs' : ('DocumentRoot (.*)',),
        'debug'  :  'DEBUG = (.*)',
        'secure' : ('SECURE[ ]*=[ ]*([^ \n]*)', 'SECURE = {0}'),
        'speed'  : ('SPEED[ ]*=[ ]*([^ \n]*)', 'SPEED = {0}'),
        'list'   : ('LIST[ ]*=[ ]*([^ \n]*)', 'LIST = {0}'),
    })
    assert the_file.htdocs[0] == '/var/www/google.com'
    assert the_file.htdocs[1] == '/var/www/example.com'
    assert the_file.debug == 'True'
    assert the_file.secure == 'False'
    the_file.secure = 'True'
    assert the_file.secure == 'True'
    assert the_file.speed is None
    the_file.speed = 'fastest'
    assert the_file.speed == 'fastest'
    the_file.speed = 'fastest' # setting it more than once with the same value
                           # shouldn't affect the number of times it is added.
    assert isinstance(the_file.speed, str) \
        or isinstance(the_file.speed, unicode)  # Shouldn't be a list, checking unicode
                                          # for Python 2 support.
    assert len(the_file.list) == 2 # Should be a list
