#!/usr/bin/env python
#
# name:             test_file.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/12/2014
#
# description:      A unit test for ext_pylib file module's File class and
#                   methods.
#

from ext_pylib.files import File
import pytest


init_args = [
    ({'path' : None}, 
        {'path' : '<file.File:stub>', 'perms' : None, 'owner' : None, 'group' : None}),
]
@pytest.mark.parametrize(("atts", "expected"), init_args)
def test_file_initialize(atts, expected):
    """Test initialize Node."""
    file = File(atts)
    pass

def test_file_create():
    """TODO:"""
    pass

def test_file_remove():
    """TODO:"""
    pass
