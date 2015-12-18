#!/usr/bin/env python
#
# name:             file.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/04/2015
#
# description:      A class to manage and create files.
#

from node import Node
import os
from ext_pylib import prompt


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

    def create(self, data = None):
        """Creates the file/directory."""
        # TODO: What if the directory doesn't yet exist?
        if not self.path:
            return True
        if self.exists():
            print self.path + ' already exists.'
            if not prompt('Replace it?', False):
                return True
        print('Creating ' + self.path + '... '),

        # Create parent directorys
        if not self.parent_node.exists:
            try:
                self.parent_node.create()
            except Exception as error:
                print '[ERROR]'
                print error

        # Use passed data
        if data:
            # TODO: Write data to file
            pass

        # Or just create the file
        else:
            try:
                open(self.path, 'w+').close()
                print('[OK]')
            except Exception as error:
                print '[ERROR]'
                print error
                return False
        return self.chmod() and self.chown()

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
