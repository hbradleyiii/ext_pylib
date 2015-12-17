#!/usr/bin/env python
#
# name:             test_dir.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/12/2015
#
# description:      A unit test for ext_pylib file module's Dir class and
#                   methods.
#

from ext_pylib.files import Dir
from mock import patch
import pytest


init_args = [
    (None, '<files.Dir:stub>'),
    ('/this/path', '/this/path/'),
    ('/this//path/dir', '/this/path/dir/'),
    ('/this//path//', '/this/path/'),
    ('/this///path////', '/this/path/'),
]
@pytest.mark.parametrize(("atts", "expected"), init_args)
def test_dir_initialization(atts, expected):
    """Test initialize Dir."""
    dir = Dir({'path' : atts})
    assert str(dir) == expected

@patch('os.path.exists')
@patch('os.makedirs')
def test_dir_create(mock_makedirs, mock_exists):
    """Test directory creation."""
    mock_exists.return_value = False
    dir = Dir({'path' : '/test/dir/'})
    assert dir.create()
    mock_makedirs.assert_called_once_with('/test/dir/')

@patch('os.path.exists')
@patch('os.makedirs')
def test_dir_create_existing(mock_makedirs, mock_exists):
    """Test creating dir when it already exists."""
    mock_exists.return_value = True
    dir = Dir({'path' : '/test/dir/'})
    assert dir.create()
    assert not mock_makedirs.called

@patch('os.path.exists')
@patch('shutil.rmtree')
def test_dir_remove(mock_rmtree, mock_exists):
    """Test directory removal."""
    mock_exists.return_value = True
    dir = Dir({'path' : '/test/dir/'})
    assert dir.remove(False)
    assert mock_rmtree.called_once_with('/test/dir/')

@patch('os.path.exists')
@patch('os.makedirs')
def test_dir_remove_nonexisting(mock_rmtree, mock_exists):
    """Test non-existing directory removal."""
    mock_exists.return_value = False
    dir = Dir({'path' : '/test/dir/'})
    assert dir.remove(False)
    assert not mock_rmtree.called

def test_dir_fill():
    """TODO:"""
    pass

def test_dir_actual_create_remove_and_fill():
    """TODO:"""
    pass
