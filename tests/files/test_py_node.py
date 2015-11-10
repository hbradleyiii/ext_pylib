#!/usr/bin/env python
#
# name:             test_py_node.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/08/2014
#
# description:      A unit test for ext_pylib file module's py_node class and
#                   methods.
#

from ext_pylib.files import Py_Node
import pytest

@pytest.mark.parametrize(("atts", "expected"), [
    ({'path' : None}, 
        {'path' : '<Py_Node:stub>', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/this/path/'}, 
        {'path' : '/this/path/', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file'},
        {'path' : '/etc/path/file', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file'},
        {'path' : '/etc/path/file', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file', 'perms' : 0655},
        {'path' : '/etc/path/file', 'perms' : 0655, 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file', 'perms' : 0655, 'owner' : 'root', 'group' : 'root'},
        {'path' : '/etc/path/file', 'perms' : 0655, 'owner' : 'root', 'group' : 'root'}),
])
def test_py_node_initialize(atts, expected):
    """Test initialize Py_Node."""
    node = Py_Node(atts)
    assert str(node) == expected['path']
    assert node.perms == expected['perms']
    assert node.owner == expected['owner']
    assert node.group == expected['group']

@pytest.mark.parametrize(("atts", "expected"), [
    ({'path' : None}, '<Py_Node:stub>'),
    ({'path' : '/this/path/'}, '/this/path/'),
    ({'path' : '/etc/path/file'}, '/etc/path/file'),
])
def test_py_node_concatenate(atts, expected):
    """Test concatenate Py_Node objects."""
    node = Py_Node(atts)
    assert node + 'string' == expected + 'string'

def test_py_node_create():
    """Test that Py_Node throws an error when calling create()."""
    node = Py_Node({'path' : '/the/path'})
    with pytest.raises(NotImplementedError):
        node.create()

def test_py_node_remove():
    """Test that Py_Node throws an error when calling remove()."""
    node = Py_Node({'path' : '/the/path'})
    with pytest.raises(NotImplementedError):
        node.remove()

def test_py_node_set_path_empty():
    """Test that Py_Node throws an error when setting path to empty string."""
    node = Py_Node()
    with pytest.raises(ValueError):
        node.path = ''
    with pytest.raises(ValueError):
        node = Py_Node({'path' : ''})

@pytest.mark.parametrize(('invalid_char'), [
    ('!'), ('@'), ('#'), ('$'), ('%'), ('^'), ('&'), ('*'), ('|'),
])
def test_py_node_set_path_invalid_char(invalid_char):
    """Test that Py_Node throws an error when setting path to invalid character."""
    node = Py_Node()
    with pytest.raises(ValueError):
        node.path = '/path/to' + invalid_char
    with pytest.raises(ValueError):
        node = Py_Node({'path' : '/path/to' + invalid_char})

def test_py_node_set_path_relative():
    """Test that Py_Node throws an error when setting path to relative path."""
    node = Py_Node()
    with pytest.raises(ValueError):
        node.path = 'path/to'
    with pytest.raises(ValueError):
        node = Py_Node({'path' : 'path/to'})
    with pytest.raises(ValueError):
        node = Py_Node({'path' : './path/to'})

# TODO: Handle multiple '/' in paths.

@pytest.mark.parametrize(("atts", "expected"), [
    ({'path' : None}, None),
    ({'path' : '/this/path/'}, '/this/'),
    ({'path' : '/etc/path/file'}, '/etc/path/'),
])
def test_py_node_parent_dirs(atts, expected):
    """Test generate_pw function."""
    node = Py_Node(atts)
    assert node.parent_dirs == expected

def test_py_node_set_perms_invalid():
    """TODO:"""
    pass

def test_py_node_set_bad_owner():
    """TODO:"""
    pass

def test_py_node_set_owner_root():
    """TODO:"""
    pass

def test_py_node_set_bad_group():
    """TODO:"""
    pass

def test_py_node_set_group_root():
    """TODO:"""
    pass
