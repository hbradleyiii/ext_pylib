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
from mock import mock_open, patch
import pytest
from sys import version_info
if version_info.major == 2:
    builtins = '__builtin__'
else:
    builtins = 'builtins'


DEFAULT_ARGS = { 'path' : '/tmp/nonexistant/path/file' }

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

def test_write_no_data():
    """Test writing to a File with no data passed in."""
    file = File(DEFAULT_ARGS)
    with pytest.raises(UnboundLocalError):
        file.write()

def test_write_data_with_handle():
    """Test writing to a File with a handle passed in."""
    class Mock_handle:
        """A Mock class for a handle."""
        data = None
        def write(self, data):
            self.data = data
        def called_once_with(self, var):
            if var != self.data:
                print 'Mock handle was not called with: ' + var
                return False
            return True
    file = File(DEFAULT_ARGS)
    mock_handle = Mock_handle()
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
    file = File(DEFAULT_ARGS)
    assert file.remove(False)
    mock_remove.assert_called_once_with(DEFAULT_ARGS['path'])
