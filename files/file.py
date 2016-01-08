#!/usr/bin/env python
#
# name:             file.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/04/2015
#
# description:      A class to manage and create files.
#

from dir import Dir
from node import Node
import os
from ext_pylib.prompt import prompt


# File(atts)
#   An class to manage a file's permissions, ownership, and path. Extends Node
#   class.
#
#   methods:
#       create()
#       remove(ask)
class File(Node):

    def __str__(self):
        """Returns a string with the path."""
        if not self.path:
            return '<file.File:stub>'
        return self.path

    def read(self):
        """Returns the contents of the file."""
        try:
            return self.data
        except AttributeError:
            try:
                file_handle = open(self.path, 'r')
                self.data = file_handle.read()
                file_handle.close()
                return self.data
            except Exception as error:
                print '[ERROR]'
                print error
                return False

    def readlines(self):
        """Returns the contents of the file as a list for iteration."""
        return self.read().split('\n')

    def create(self, data = None):
        """Creates the file/directory."""
        if not self.path: # For stubs, just return True
            return True
        if self.exists():
            print self.path + ' already exists.'
            if not prompt('Replace it?', False):
                return False
        print('Creating ' + self.path + '... '),

        # Create parent directories
        if not self.parent_dir.exists():
            try:
                print ''
                self.parent_dir.create()
            except Exception as error:
                print '[ERROR]'
                print error

        # Create the file
        try:
            file_handle = open(self.path, 'w')
            if data:
                self.write(data, False, file_handle)
            file_handle.close()
            print('[OK]')
        except Exception as error:
            print '[ERROR]'
            print error
            return False
        return self.chmod() and self.chown()

    def write(self, data=None, append=True, handle=None):
        """Writes data to the file."""
        if not data:
            raise UnboundLocalError('Must pass data to write method of File class.')
        if handle: # When passed a handle, rely on the caller to close the file and
              # handle exceptions.
            file_handle = handle
            file_handle.write(data)
        else:
            try:
                flags = 'a' if append else 'w'
                file_handle = open(self.path, flags)
                file_handle.write(data)
                file_handle.close()
                return True
            except Exception as error:
                print '[ERROR]'
                print error
                return False

    def append(self, data, handle=None):
        """Appends the file with data. Just a wrapper."""
        self.write(data, True, handle)

    def overwrite(self, data, handle=None):
        """Overwrites the file with data. Just a wrapper."""
        self.write(data, False, handle)

    def remove(self, ask = True):
        """Removes the file/directory."""
        if not self.path:
            return True
        if not self.exists():
            print self.path + ' doesn\'t exist.'
            return True
        if not ask or prompt('Remove ' + self.path + '?'):
            os.remove(self.path)
            return True

    ################
    # Properties

    @Node.path.setter
    def path(self, path):
        """Sets the path."""
        # Check for None
        if path == None:
            return
        # File cannot end in '/'
        if path.endswith('/'):
            raise ValueError('"path" cannot end in "/" in a file.File class.')
        Node.path.fset(self, path)

    @property
    def parent_dir(self):
        return Dir(self.parent_node._atts_())
