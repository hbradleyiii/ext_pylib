#!/usr/bin/env python
#
# name:             test_dir.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/12/2015
#
# description:      A unit test for ext_pylib file module's Dir class and
#                   methods. Note that copytree() function is tested in
#                   test_integration.
#

from datetime import datetime
from ext_pylib.files import Dir
from mock import patch
import os
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
    mock_rmtree.assert_called_once_with('/test/dir/')

@patch('os.path.exists')
@patch('shutil.rmtree')
def test_dir_remove_nonexisting(mock_rmtree, mock_exists):
    """Test non-existing directory removal."""
    mock_exists.return_value = False
    dir = Dir({'path' : '/test/dir/'})
    dir2 = Dir({'path' : None})
    assert dir.remove(False)
    assert dir2.remove(False)
    assert not mock_rmtree.called

@patch('os.path.exists')
@patch('ext_pylib.files.dir.copytree')
def test_dir_fill(mock_copytree, mock_exists):
    """Tests filling one Dir with another."""
    mock_exists.return_value = True
    dir = Dir({'path' : '/test/dir/'})
    fill_with = Dir({'path' : '/another/test/dir/'})
    assert dir.fill(fill_with)
    mock_copytree.assert_called_once_with('/another/test/dir/', '/test/dir/')

def test_dir_actual_create_and_remove(tmpdir):
    """[Integration Test] Test actual creation and removal of directory."""
    # Setup a root dir to use to test
    root_dir = Dir({'path' : '/tmp/ext_pylib/'})
    assert root_dir.remove(False) # If it already exists, remove it.
    assert root_dir.create()
    assert root_dir.exists()

    # Perform a (redundant) creation test
    dir = Dir({'path' : '/tmp/ext_pylib/' + datetime.now().strftime('%Y-%m-%d--%H-%M-%S') + '/path/dir'})
    assert not dir.exists()
    assert dir.create()
    assert dir.exists()

    # Perform a removal test
    assert dir.remove(False)
    assert not dir.exists()

    # Cleanup
    assert root_dir.remove(False)
    assert not root_dir.exists()
