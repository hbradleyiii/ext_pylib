#!/usr/bin/env python
#
# name:             test_file.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/12/2015
#
# description:      A unit test for ext_pylib file module's File class and
#                   methods. This is fairly ugly, but it's pretty
#                   comprehensive.
#

from ext_pylib.files import File
from mock import mock_open, patch
import pytest
from sys import version_info

if version_info.major == 2:
    builtins = '__builtin__'
else:
    builtins = 'builtins'


class Mock_Parent_Dir(object):
    """A Mock class for parent_dir property."""
    def __init__(self, _exists):
        self._exists = _exists
        self.exists_called, self.create_called = 0, 0
    def exists(self):
        self.exists_called += 1
        return self._exists
    def create(self):
        self.create_called += 1


class Mock_Handle(object):
    """A Mock class for a handle."""
    data = None
    def write(self, data):
        self.data = data
    def called_once_with(self, var):
        if var != self.data:
            print 'Mock handle was not called with: ' + var
            return False
        return True


DEFAULT_ARGS = { 'path' : '/tmp/nonexistant/path/file' }

init_args = [
    (None, '<file.File:stub>'),
    ('/this/file', '/this/file'),
    ('/this//path//file', '/this/path/file'),
]
@pytest.mark.parametrize(("atts", "expected"), init_args)
def test_file_initialize(atts, expected):
    """Tests initialize File."""
    file = File({'path' : atts})
    assert str(file) == expected

def test_file_initialize_with_trailing_slash():
    """Tests initializing a File with a trailing slash."""
    with pytest.raises(ValueError):
        file = File({'path' : '/this/path/'})

def test_file_create_stub():
    """Tests file creation of a stub."""
    assert File().create()

@patch('ext_pylib.files.file.prompt')
@patch('ext_pylib.files.node.Node.exists')
@patch('ext_pylib.files.file.File.write')
def test_file_create_already_existing_file_not_replacing(mock_write, mock_exists, mock_prompt):
    """Tests file creation of an already existing file (NOT replacing the file)."""
    mock_exists.return_value = True
    mock_prompt.return_value = False # Answer no, don't replace
    file = File(DEFAULT_ARGS)
    assert not file.create()

@patch('ext_pylib.files.node.Node.chown')
@patch('ext_pylib.files.node.Node.chmod')
@patch('ext_pylib.files.file.prompt')
@patch('ext_pylib.files.node.Node.exists')
@patch('ext_pylib.files.file.File.write')
def test_file_create_already_existing_file_replacing(mock_write, mock_exists, mock_prompt, mock_chmod, mock_chown):
    """Tests file creation of an already existing file (replacing the file)."""
    mock_parent_dir = Mock_Parent_Dir(True)
    mock_exists.return_value = True
    mock_chown.return_value = mock_chmod.return_value = True
    mock_prompt.return_value = True # Answer yes, replace
    file = File(DEFAULT_ARGS)
    m_open = mock_open()
    with patch(builtins + '.open', m_open, create=True):
        assert file.create()
        m_open.assert_called_once_with(DEFAULT_ARGS['path'], 'w')
        m_open().close.assert_called_once()

@patch('ext_pylib.files.node.Node.chown')
@patch('ext_pylib.files.node.Node.chmod')
@patch('ext_pylib.files.node.Node.exists')
def test_file_create_and_create_parent_dirs(mock_exists, mock_chmod, mock_chown):
    """Tests file creation while creating parent dirs."""
    mock_parent_dir = Mock_Parent_Dir(False)
    mock_exists.return_value = False
    mock_chown.return_value = mock_chmod.return_value = True
    File.parent_dir = mock_parent_dir
    file = File(DEFAULT_ARGS)
    m_open = mock_open()
    with patch(builtins + '.open', m_open, create=True):
        assert file.create()
        m_open.assert_called_once_with(DEFAULT_ARGS['path'], 'w')
        m_open().close.assert_called_once()
        assert mock_parent_dir.exists_called == 1
        assert mock_parent_dir.create_called == 1

@patch('ext_pylib.files.node.Node.chown')
@patch('ext_pylib.files.node.Node.chmod')
@patch('ext_pylib.files.node.Node.exists')
@patch('ext_pylib.files.file.File.write')
def test_file_create_with_data(mock_write, mock_exists, mock_chmod, mock_chown):
    """Tests file creation with data."""
    mock_parent_dir = Mock_Parent_Dir(True)
    mock_exists.return_value = False
    mock_chown.return_value = mock_chmod.return_value = True
    File.parent_dir = mock_parent_dir
    file = File(DEFAULT_ARGS)
    m_open = mock_open()
    with patch(builtins + '.open', m_open, create=True):
        data = 'The data...'
        assert file.create(data)
        m_open.assert_called_once_with(DEFAULT_ARGS['path'], 'w')
        mock_write.assert_called_once_with(data, False, m_open())
        m_open().close.assert_called_once()
        assert mock_parent_dir.exists_called == 1
        assert mock_parent_dir.create_called == 0

@patch('ext_pylib.files.node.Node.chown')
@patch('ext_pylib.files.node.Node.chmod')
@patch('ext_pylib.files.node.Node.exists')
@patch('ext_pylib.files.file.File.write')
def test_file_create_with_data_but_not_as_arg(mock_write, mock_exists, mock_chmod, mock_chown):
    """Tests file creation with data."""
    mock_parent_dir = Mock_Parent_Dir(True)
    mock_exists.return_value = False
    mock_chown.return_value = mock_chmod.return_value = True
    File.parent_dir = mock_parent_dir
    file = File(DEFAULT_ARGS)
    m_open = mock_open()
    with patch(builtins + '.open', m_open, create=True):
        data = 'The data...'
        file.data = data
        assert file.create()
        m_open.assert_called_once_with(DEFAULT_ARGS['path'], 'w')
        mock_write.assert_called_once_with(data, False, m_open())
        m_open().close.assert_called_once()
        assert mock_parent_dir.exists_called == 1
        assert mock_parent_dir.create_called == 0

@patch('ext_pylib.files.node.Node.exists')
def test_write_no_data(mock_exists):
    """Tests writing to a File with no data passed in."""
    file = File(DEFAULT_ARGS)
    with pytest.raises(UnboundLocalError):
        file.write()

def test_write_data_with_handle():
    """Tests writing to a File with a handle passed in."""
    file = File(DEFAULT_ARGS)
    mock_handle = Mock_Handle()
    data = 'Some mock data...'
    file.write(data=data, handle=mock_handle)
    assert mock_handle.called_once_with(data)

def test_write_append_data_without_handle():
    """Tests appending to a file without a handle."""
    m_open = mock_open()
    with patch(builtins + '.open', m_open, create=True):
        file = File(DEFAULT_ARGS)
        data = 'Some mock data...'
        assert file.write(data)
        m_open.assert_called_once_with(DEFAULT_ARGS['path'], 'a')
        m_open().write.assert_called_once_with(data)
        m_open().close.assert_called_once()

def test_write_data_without_handle():
    """Tests writing to a file without a handle."""
    m_open = mock_open()
    with patch(builtins + '.open', m_open, create=True):
        file = File(DEFAULT_ARGS)
        data = 'Some mock data...'
        assert file.write(data, False)
        m_open.assert_called_once_with(DEFAULT_ARGS['path'], 'w')
        m_open().write.assert_called_once_with(data)
        m_open().close.assert_called_once()

@patch('ext_pylib.files.file.File.write')
def test_file_append(mock_write):
    """Tests appending to file."""
    File().append(None)
    mock_write.assert_called_once_with(None, True, None)

@patch('ext_pylib.files.file.File.write')
def test_file_overwrite(mock_write):
    """Tests overwriting a file."""
    File().overwrite(None)
    mock_write.assert_called_once_with(None, False, None)

@patch('ext_pylib.files.node.Node.exists')
@patch('os.remove')
def test_file_remove(mock_remove, mock_exists):
    """Tests File remove method."""
    mock_exists.return_value = True
    file = File(DEFAULT_ARGS)
    assert file.remove(False)
    mock_remove.assert_called_once_with(DEFAULT_ARGS['path'])

@patch('ext_pylib.files.node.Node.exists')
def test_file_read_nonexisting_file(mock_exists):
    """Tests File read method."""
    mock_exists.return_value = False
    file = File(DEFAULT_ARGS)
    assert file.read() == ''

@patch('ext_pylib.files.node.Node.exists')
def test_file_read_nonexisting_file_with_data_in_memory(mock_exists):
    """Tests File read method."""
    mock_exists.return_value = False
    file = File(DEFAULT_ARGS)
    file.data = 'Data is in memory...'
    assert file.read() == 'Data is in memory...'

@patch('ext_pylib.files.node.Node.exists')
def test_file_read_file_with_data(mock_exists):
    mock_exists.return_value = True
    file = File(DEFAULT_ARGS)
    file.data = 'Test data'
    assert file.read() == file.data
    assert file.read() == 'Test data'
    file.data = 'New data'
    assert file.read() == file.data
    assert file.read() == 'New data'
