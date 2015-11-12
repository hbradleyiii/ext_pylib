#!/usr/bin/env python
#
# name:             test_dir.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/12/2014
#
# description:      A unit test for ext_pylib file module's Dir class and
#                   methods.
#

from ext_pylib.files import Dir
import pytest


init_args = [
    (None, '<files.Dir:stub>'),
    ('/this/path', '/this/path/'),
]
@pytest.mark.parametrize(("atts", "expected"), init_args)
def test_dir_initialization(atts, expected):
    """Test initialize Dir."""
    dir = Dir({'path' : atts})
    assert str(dir) == expected

def test_dir_create():
    """TODO:"""
    pass

def test_dir_remove():
    """TODO:"""
    pass

def test_dir_fill():
    """TODO:"""
    pass
