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
"""

# Monkey Patch function for read() method
def read():
    return FILE

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
    file.read = read
    file.parse({ 'htdocs' : 'DocumentRoot (.*)'})
    assert file.htdocs[0] == '/var/www/google.com'
