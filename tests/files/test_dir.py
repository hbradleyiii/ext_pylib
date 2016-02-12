#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_dir.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/12/2015

"""
A unit test for ext_pylib file module's Dir class and methods. Note that
copytree() function is tested in test_integration.
"""

from mock import patch
import pytest

from ext_pylib.files import Dir


INIT_ARGS = [
    (None, '<files.Dir:stub>'),
    ('/this/path', '/this/path/'),
    ('/this//path/dir', '/this/path/dir/'),
    ('/this//path//', '/this/path/'),
    ('/this///path////', '/this/path/'),
]
@pytest.mark.parametrize(("atts", "expected"), INIT_ARGS)
def test_dir_initialization(atts, expected):
    """Test initialize Dir."""
    the_dir = Dir({'path' : atts})
    assert str(the_dir) == expected

@patch('ext_pylib.files.node.Node.chown')
@patch('ext_pylib.files.node.Node.chmod')
@patch('ext_pylib.files.node.Node.exists')
@patch('os.makedirs')
def test_dir_create(mock_makedirs, mock_exists, mock_chmod, mock_chown):
    """Test directory creation."""
    mock_exists.return_value = False
    mock_chown.return_value = mock_chmod.return_value = True
    the_dir = Dir({'path' : '/test/dir/'})
    assert the_dir.create()
    mock_makedirs.assert_called_once_with('/test/dir/')

@patch('ext_pylib.files.node.Node.exists')
@patch('os.makedirs')
def test_dir_create_existing(mock_makedirs, mock_exists):
    """Test creating dir when it already exists."""
    mock_exists.return_value = True
    the_dir = Dir({'path' : '/test/dir/'})
    assert the_dir.create()
    assert not mock_makedirs.called

@patch('ext_pylib.files.node.Node.exists')
@patch('shutil.rmtree')
def test_dir_remove(mock_rmtree, mock_exists):
    """Test directory removal."""
    mock_exists.return_value = True
    the_dir = Dir({'path' : '/test/dir/'})
    assert the_dir.remove(False)
    mock_rmtree.assert_called_once_with('/test/dir/')

@patch('ext_pylib.files.node.Node.exists')
@patch('shutil.rmtree')
def test_dir_remove_nonexisting(mock_rmtree, mock_exists):
    """Test non-existing directory removal."""
    mock_exists.return_value = False
    the_dir = Dir({'path' : '/test/dir/'})
    the_dir2 = Dir({'path' : None})
    assert the_dir.remove(False)
    assert the_dir2.remove(False)
    assert not mock_rmtree.called

@patch('ext_pylib.files.node.Node.exists')
@patch('ext_pylib.files.dir.copytree')
def test_dir_fill(mock_copytree, mock_exists):
    """Tests filling one Dir with another."""
    mock_exists.return_value = True
    the_dir = Dir({'path' : '/test/dir/'})
    fill_with = Dir({'path' : '/another/test/dir/'})
    assert the_dir.fill(fill_with)
    mock_copytree.assert_called_once_with('/another/test/dir/', '/test/dir/')
