#!/usr/bin/env python
#
# name:             test_node.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/08/2015
#
# description:      A unit test for ext_pylib file module's Node class and
#                   methods.
#

from ext_pylib.files.node import Node
from mock import patch
import pytest

init_args = [
    ({'path' : None},
        {'path' : '<files.Node:stub>', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/this/path/file'},
        {'path' : '/this/path/file', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/this/path/'},
        {'path' : '/this/path/', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/this//path/'},
        {'path' : '/this/path/', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/this//path//'},
        {'path' : '/this/path/', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/this///path////'},
        {'path' : '/this/path/', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file'},
        {'path' : '/etc/path/file', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file'},
        {'path' : '/etc/path/file', 'perms' : None, 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file', 'perms' : 0655},
        {'path' : '/etc/path/file', 'perms' : '0655', 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file', 'perms' : 0655, 'owner' : 'root', 'group' : 'root'},
        {'path' : '/etc/path/file', 'perms' : '0655', 'owner' : 'root', 'group' : 'root'}),
]
@pytest.mark.parametrize(("atts", "expected"), init_args)
def test_node_initialize(atts, expected):
    """Test initialize Node."""
    node = Node(atts)
    assert str(node) == expected['path']
    assert node.perms == expected['perms']
    assert node.owner == expected['owner']
    assert node.group == expected['group']

repr_args = [
    ({'path' : None},
        "{'path' : None, 'perms' : None, 'owner' : None, 'group' : None}"),
    ({'path' : '/this/path/file'},
        "{'path' : '/this/path/file', 'perms' : None, 'owner' : None, 'group' : None}"),
    ({'path' : '/etc/path/file', 'perms' : 0655},
        "{'path' : '/etc/path/file', 'perms' : 0655, 'owner' : None, 'group' : None}"),
    ({'path' : '/etc/path/file', 'perms' : 0655, 'owner' : 'root', 'group' : 'root'},
        "{'path' : '/etc/path/file', 'perms' : 0655, 'owner' : 'root', 'group' : 'root'}"),
]
@pytest.mark.parametrize(("atts", "expected"), repr_args)
def test_node_repr(atts, expected):
    """Test Node repr."""
    node = Node(atts)
    assert node.__repr__() == "Node(" + expected + ")"

@pytest.mark.parametrize(("atts", "expected"), repr_args)
def test_node__atts_(atts, expected):
    """Test Node repr."""
    node = Node(atts)
    assert node._atts_() == expected

concat_args = [
    ({'path' : None}, '<files.Node:stub>'),
    ({'path' : '/this/path/'}, '/this/path/'),
    ({'path' : '/etc/path/file'}, '/etc/path/file'),
]
@pytest.mark.parametrize(("atts", "expected"), concat_args)
def test_node_concatenate(atts, expected):
    """Test concatenate Node objects."""
    node = Node(atts)
    assert node + 'string' == expected + 'string'
    assert 'string' + node == 'string' + expected

def test_node_create():
    """Test that Node throws an error when calling create()."""
    node = Node({'path' : '/the/path'})
    with pytest.raises(NotImplementedError):
        node.create()

def test_node_remove():
    """Test that Node throws an error when calling remove()."""
    node = Node({'path' : '/the/path'})
    with pytest.raises(NotImplementedError):
        node.remove()

def test_node_verify():
    """TODO:"""
    pass

@patch('ext_pylib.files.node.Node.verify')
def test_node_repair(mock_verify):
    """Test that repair() method calls verify(True)."""
    node = Node()
    node.repair()
    mock_verify.assert_called_once_with(True)

def test_node_chmod():
    """TODO:"""
    pass

def test_node_chown():
    """TODO:"""
    pass

def test_node_exists():
    """TODO:"""
    pass
# TODO: test actual_ methods

def test_node_set_path_empty():
    """Test that Node throws an error when setting path to empty string."""
    node = Node()
    with pytest.raises(ValueError):
        node.path = ''
    with pytest.raises(ValueError):
        node = Node({'path' : ''})

@pytest.mark.parametrize(('invalid_char'), [
    ('!'), ('@'), ('#'), ('$'), ('%'), ('^'), ('&'), ('*'), ('|'),
])
def test_node_set_path_invalid_char(invalid_char):
    """Test that Node throws an error when setting path to invalid character."""
    node = Node()
    with pytest.raises(ValueError):
        node.path = '/path/to' + invalid_char
    with pytest.raises(ValueError):
        node = Node({'path' : '/path/to' + invalid_char})

def test_node_set_path_relative():
    """Test that Node throws an error when setting path to relative path."""
    node = Node()
    with pytest.raises(ValueError):
        node.path = 'path/to'
    with pytest.raises(ValueError):
        node = Node({'path' : 'path/to'})
    with pytest.raises(ValueError):
        node = Node({'path' : './path/to'})

parent_dirs_args = [
    ({'path' : None}, None),
    ({'path' : '/this/path/'}, '/this/'),
    ({'path' : '/etc/path/file'}, '/etc/path/'),
    ({'path' : '//etc//path//file'}, '/etc/path/'),
]
@pytest.mark.parametrize(("atts", "expected"), parent_dirs_args)
def test_node_parent_dirs(atts, expected):
    """Test generate_pw function."""
    node = Node(atts)
    assert node.parent_dirs == expected

default_atts = { 'path' : '/etc/path/file' }

def test_node_set_perms_invalid():
    """Tests setting node's perms as invalid values."""
    node = Node(default_atts)
    with pytest.raises(ValueError):
        node.perms = 'a'
    with pytest.raises(ValueError):
        node.perms = 9999
    with pytest.raises(ValueError):
        node.perms = -9999

def test_node_set_bad_owner():
    """Tests setting node's owner to an invalid user."""
    node = Node(default_atts)
    with pytest.raises(KeyError):
        node.owner = 'HopefullyNot_a_RealUser'

def test_node_set_owner_root():
    """Tests setting node's owner to root."""
    node = Node(default_atts)
    node.owner = 'root'
    assert node.owner == 'root'
    assert node._owner == 'root'

def test_node_set_bad_group():
    """Tests setting node's group to an invalid user."""
    node = Node(default_atts)
    with pytest.raises(KeyError):
        node.group = 'HopefullyNot_a_RealGroup'

def test_node_set_group_root():
    """Tests setting node's group to root."""
    node = Node(default_atts)
    node.group = 'root'
    assert node.group == 'root'
    assert node._group == 'root'
