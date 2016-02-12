#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_node.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/08/2015

# pylint:           disable=invalid-name,line-too-long

"""
A unit test for ext_pylib file module's Node class and methods.
"""

import pytest
from mock import patch

from ext_pylib.files.node import Node
from ext_pylib.user import get_current_username, get_current_groupname


CURRENT_USER = get_current_username()
CURRENT_GROUP = get_current_groupname()

DEFUALT_ATTS = {'path' : '/etc/path/file'}

INIT_ARGS = [
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
    ({'path' : '/etc/path/file', 'perms' : 0o655},
     {'path' : '/etc/path/file', 'perms' : 0o655, 'owner' : None, 'group' : None}),
    ({'path' : '/etc/path/file', 'perms' : 0o655, 'owner' : 'root', 'group' : 'root'},
     {'path' : '/etc/path/file', 'perms' : 0o655, 'owner' : 'root', 'group' : 'root'}),
]
@pytest.mark.parametrize(("atts", "expected"), INIT_ARGS)
def test_node_initialize(atts, expected):
    """Test initialize Node."""
    node = Node(atts)
    assert str(node) == expected['path']
    assert node.perms == expected['perms']
    assert node.owner == expected['owner']
    assert node.group == expected['group']

REPR_ARGS = [
    ({'path' : None},
     "{'path' : None, 'perms' : None, 'owner' : None, 'group' : None}"),
    ({'path' : '/this/path/file'},
     "{'path' : '/this/path/file', 'perms' : None, 'owner' : None, 'group' : None}"),
    ({'path' : '/etc/path/file', 'perms' : 0o655},
     "{'path' : '/etc/path/file', 'perms' : 0o655, 'owner' : None, 'group' : None}"),
    ({'path' : '/etc/path/file', 'perms' : 0o655, 'owner' : 'root', 'group' : 'root'},
     "{'path' : '/etc/path/file', 'perms' : 0o655, 'owner' : 'root', 'group' : 'root'}"),
]
@pytest.mark.parametrize(("atts", "expected"), REPR_ARGS)
def test_node_repr(atts, expected):
    """Test Node repr."""
    node = Node(atts)
    assert node.__repr__() == "Node(" + expected + ")"

@pytest.mark.parametrize(("atts", "expected"), REPR_ARGS)
def test_node_get_atts(atts, expected):
    """Test Node get_atts method."""
    node = Node(atts)
    if 'perms' not in atts:
        atts['perms'] = None
    if 'owner' not in atts:
        atts['owner'] = None
    if 'group' not in atts:
        atts['group'] = None
    assert node.get_atts(string=True) == expected
    assert node.get_atts(string=False) == atts

CONCAT_ARGS = [
    ({'path' : None}, '<files.Node:stub>'),
    ({'path' : '/this/path/'}, '/this/path/'),
    ({'path' : '/etc/path/file'}, '/etc/path/file'),
]
@pytest.mark.parametrize(("atts", "expected"), CONCAT_ARGS)
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

VERIFY_ARGS = [
    ({'path' : None}),
    ({'path' : '/this/path/file'}),
    ({'path' : '/this/path/', 'perms' : 0o655}),
    ({'path' : '/this/path/', 'owner' : 'root'}),
    ({'path' : '/this/path/', 'group' : 'root'}),
    ({'path' : '/this/path/', 'perms' : 0o655, 'owner' : 'root'}),
    ({'path' : '/this/path/', 'perms' : 0o655, 'group' : 'root'}),
    ({'path' : '/this/path/', 'owner' : 'root', 'group' : 'root'}),
    ({'path' : '/etc/path/file', 'perms' : 0o655, 'owner' : 'root', 'group' : 'root'}),
]
@pytest.mark.parametrize(("atts"), VERIFY_ARGS)
@patch('ext_pylib.files.node.Node.actual_group')
@patch('ext_pylib.files.node.Node.actual_owner')
@patch('ext_pylib.files.node.Node.actual_perms')
@patch('ext_pylib.files.node.Node.exists')
def test_node_verify(mock_exists, mock_actual_perms, mock_actual_owner, mock_actual_group, atts):
    """Test Node's method verify."""
    # Test passing verification
    mock_exists.return_value = True
    node = Node(atts)
    node.actual_perms = None if 'perms' not in atts else atts['perms']
    node.actual_owner = None if 'owner' not in atts else atts['owner']
    node.actual_group = None if 'group' not in atts else atts['group']
    assert node.verify(False)

    # Test failing verification
    if atts['path']:
        # If there is no path, it's a stub and should always verify true.
        mock_exists.return_value = False
        mock_actual_perms.return_value = None
        mock_actual_owner.return_value = None
        mock_actual_group.return_value = None
        bad_node = Node(atts)
        assert not bad_node.verify(False)

@patch('ext_pylib.files.node.Node.verify')
def test_node_repair(mock_verify):
    """Test that repair() method calls verify(True)."""
    node = Node()
    node.repair()
    mock_verify.assert_called_once_with(True)

CHMOD_ARGS = [
    ({'path' : None, 'perms' : 0o600}, True),
    ({'path' : '/this/path/file', 'perms' : 0o700}, True),
    ({'path' : '/this/path/file'}, True),
]
@pytest.mark.parametrize(("atts", "expected"), CHMOD_ARGS)
@patch('ext_pylib.files.node.Node.exists')
@patch('os.chmod')
def test_node_chmod(mock_chmod, mock_path_exists, atts, expected):
    """Tests Node's chmod method."""
    mock_path_exists.return_value = True # Assume this is working for this test
    node = Node(atts)
    assert expected == node.chmod()
    if atts['path'] and node.perms:
        mock_chmod.assert_called_once_with(atts['path'], atts['perms'])
    else:
        assert not mock_chmod.called

@patch('ext_pylib.files.node.Node.exists')
def test_node_chmod_nonexisting(mock_path_exists):
    """Tests Node's chown method with a nonexisting node."""
    mock_path_exists.return_value = False
    node = Node(DEFUALT_ATTS)
    with pytest.raises(IOError):
        node.chmod()

CHOWN_ARGS = [
    ({'path' : None, 'owner' : 'www-data', 'group' : 'root'}, True),
    ({'path' : '/this/path/file', 'owner' : 'www-data', 'group' : 'root'}, True),
    ({'path' : '/this/path/file', 'owner' : None, 'group' : 'root'}, True),
    ({'path' : '/this/path/file', 'owner' : 'www-data', 'group' : None}, True),
    ({'path' : '/this/path/file', 'owner' : None, 'group' : None}, True),
    ({'path' : '/this/path/file'}, True),
    ({'path' : '/this/path/file', 'owner' : 'www-data'}, True),
    ({'path' : '/this/path/file', 'group' : 'www-data'}, True),
    ({'path' : '/this/path/file', 'owner' : None, 'group' : 'www-data'}, True),
]
@pytest.mark.parametrize(("atts", "expected"), CHOWN_ARGS)
@patch('ext_pylib.files.node.Node.exists')
@patch('pwd.getpwnam')
@patch('grp.getgrnam')
@patch('os.chown')
def test_node_chown(mock_chown, mock_getgrnam, mock_getpwnam, mock_path_exists, atts, expected):  # pylint: disable=too-many-arguments
    """Tests Node's chown method."""
    node = Node(atts)
    if 'owner' not in atts:
        atts['owner'] = CURRENT_USER
    if 'group' not in atts:
        atts['group'] = 'nogroup' if atts['owner'] == 'nobody' else CURRENT_GROUP
    mock_path_exists.return_value = True # Assume this is working for this test
    mock_getpwnam(atts['owner']).pw_uid = 123 # Just a number to use for mocking
    mock_getgrnam(atts['group']).gr_gid = 123
    assert expected == node.chown()
    if atts['path'] is not None:
        mock_getpwnam.assert_called_with(CURRENT_USER if not atts['owner'] else atts['owner'])
        mock_getgrnam.assert_called_with(CURRENT_GROUP if not atts['group'] else atts['group'])
        mock_chown.assert_called_once_with(atts['path'], 123, 123)

@patch('ext_pylib.files.node.Node.exists')
def test_node_chown_nonexisting(mock_path_exists):
    """Tests Node's chown method with a nonexisting node."""
    mock_path_exists.return_value = False
    node = Node(DEFUALT_ATTS)
    with pytest.raises(IOError):
        node.chown()

EXISTS_ARGS = [
    ({'path' : None}, False),
    ({'path' : '/this/path/file'}, False),
    ({'path' : '/this/path/file'}, True),
]
@pytest.mark.parametrize(("atts", "expected"), EXISTS_ARGS)
@patch('os.path.exists')
def test_node_exists(mock_path_exists, atts, expected):
    """Tests node's exist method."""
    mock_path_exists.return_value = expected
    node = Node(atts)
    assert expected == node.exists()
    if atts['path'] is not None:
        mock_path_exists.assert_called_once_with(atts['path'])

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

PARENT_DIRS_ARGS = [
    ({'path' : None}, None),
    ({'path' : '/this/path/'}, '/this/'),
    ({'path' : '/etc/path/file'}, '/etc/path/'),
    ({'path' : '//etc//path//file'}, '/etc/path/'),
]
@pytest.mark.parametrize(("atts", "expected"), PARENT_DIRS_ARGS)
def test_node_parent_node(atts, expected):
    """Test parent_node method. Should return a Node object."""
    node = Node(atts)
    if node.path:
        assert node.parent_node.path == expected
    else:
        assert node.parent_node == expected

def test_node_set_perms_invalid():
    """Tests setting node's perms as invalid values."""
    node = Node(DEFUALT_ATTS)
    with pytest.raises(ValueError):
        node.perms = 'a'
    with pytest.raises(ValueError):
        node.perms = 9999  # pylint: disable=redefined-variable-type
    with pytest.raises(ValueError):
        node.perms = -9999

def test_node_set_bad_owner():
    """Tests setting node's owner to an invalid user."""
    node = Node(DEFUALT_ATTS)
    with pytest.raises(KeyError):
        node.owner = 'HopefullyNot_a_RealUser'

def test_node_set_owner_root():
    """Tests setting node's owner to root."""
    node = Node(DEFUALT_ATTS)
    node.owner = 'root'
    assert node.owner == 'root'

def test_node_set_bad_group():
    """Tests setting node's group to an invalid user."""
    node = Node(DEFUALT_ATTS)
    with pytest.raises(KeyError):
        node.group = 'HopefullyNot_a_RealGroup'

def test_node_set_group_root():
    """Tests setting node's group to root."""
    node = Node(DEFUALT_ATTS)
    node.group = 'root'
    assert node.group == 'root'
