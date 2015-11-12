#!/usr/bin/env python
#
# name:             test_node.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/08/2014
#
# description:      A unit test for ext_pylib file module's Node class and
#                   methods.
#

from ext_pylib.files import Node
import pytest

init_args = [
    ({'path' : None}, 
        {'path' : '<file.Node:stub>', 'perms' : None, 'owner' : None, 'group' : None}),
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
        {'path' : '/etc/path/file', 'perms' : 0655, 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file', 'perms' : 0655, 'owner' : 'root', 'group' : 'root'},
        {'path' : '/etc/path/file', 'perms' : 0655, 'owner' : 'root', 'group' : 'root'}),
]
@pytest.mark.parametrize(("atts", "expected"), init_args)
def test_node_initialize(atts, expected):
    """Test initialize Node."""
    node = Node(atts)
    assert str(node) == expected['path']
    assert node.perms == expected['perms']
    assert node.owner == expected['owner']
    assert node.group == expected['group']

concat_args = [
    ({'path' : None}, '<file.Node:stub>'),
    ({'path' : '/this/path/'}, '/this/path/'),
    ({'path' : '/etc/path/file'}, '/etc/path/file'),
]
@pytest.mark.parametrize(("atts", "expected"), concat_args)
def test_node_concatenate(atts, expected):
    """Test concatenate Node objects."""
    node = Node(atts)
    assert node + 'string' == expected + 'string'

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

def test_node_set_perms_invalid():
    """TODO:"""
    pass

def test_node_set_bad_owner():
    """TODO:"""
    pass

def test_node_set_owner_root():
    """TODO:"""
    pass

def test_node_set_bad_group():
    """TODO:"""
    pass

def test_node_set_group_root():
    """TODO:"""
    pass
