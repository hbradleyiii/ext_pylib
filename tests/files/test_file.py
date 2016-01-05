#!/usr/bin/env python
#
# name:             test_file.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/12/2015
#
# description:      A unit test for ext_pylib file module's File class and
#                   methods.
#

from ext_pylib.files import File
from mock import patch
import pytest


init_args = [
    (None, '<file.File:stub>'),
    ('/this/file', '/this/file'),
    ('/this//path//file', '/this/path/file'),
]
@pytest.mark.parametrize(("atts", "expected"), init_args)
def test_file_initialize(atts, expected):
    """Test initialize File."""
    file = File({'path' : atts})
    assert str(file) == expected

def test_file_initialize_with_trailing_slash():
    """Test initializing a File with a trailing slash."""
    with pytest.raises(ValueError):
        file = File({'path' : '/this/path/'})

def test_file_create():
    """TODO: Test file creation."""
    pass

def test_file_write():
    """TODO: Test file creation."""
    pass

@patch('ext_pylib.files.file.File.write')
def test_file_append(mock_write):
    """Test appending to file."""
    File().append(None)
    mock_write.assert_called_once_with(None, True, None)

@patch('ext_pylib.files.file.File.write')
def test_file_overwrite(mock_write):
    """Test overwriting a file."""
    File().overwrite(None)
    mock_write.assert_called_once_with(None, False, None)

@patch('ext_pylib.files.node.Node.exists')
@patch('os.remove')
def test_file_remove(mock_remove, mock_exists):
    """Test File remove method."""
    mock_exists.return_value = True
    file = File({'path' : '/test/dir/file'})
    assert file.remove(False)
    mock_remove.assert_called_once_with('/test/dir/file')
