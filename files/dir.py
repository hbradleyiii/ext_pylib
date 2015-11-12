#!/usr/bin/env python
#
# name:             mm_dir.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/03/2014
#
# description:      A class that describes a directory and gives functions to
#                   create the directory. It extends Node.
#

from node import Node
import os
from ext_pylib import prompt
import shutil


# Dir(path, atts)
#   A class that describes a directory and gives functions to create the
#   directory. This is primarily a wrapper for directory managment.
#
#   methods:
#       create()
#       remove(ask)
#       fill(fill_with)
class Dir(Node):

    def __str__(self):
        """Returns a string with the path."""
        if not self.path:
            return '<files.Dir:stub>'
        return self.path

    def create(self):
        """Creates the directory structure."""
        if self.exists():
            print self.path + ' already exists.'
            return
        print('Creating directories "' + self.path + '"...'),
        try:
            os.makedirs(self.path)
            print '[OK]'
            return True
        except Exception as error: 
            print '[ERROR]'
            print error
        self.chmod()
        self.chown()

    def remove(self, ask = True):
        """Removes the directory structure."""
        if not self.exists():
            print self.path + ' doesn\'t exist.'
            return
        if not ask or prompt('Completely remove ' + self.path + ' and all containing files and folders?'):
            print('Removing "' + self.path + '"...'),
            try:
                shutil.rmtree(self.path)
                print '[OK]'
                return True
            except Exception as error: 
                print '[ERROR]'
                print error

    def fill(self, fill_with):
        """Fills the directory with the contents of "fill_with" path."""
        if not self.exists():
            pass
        if not os.path.exists(fill_with):
            pass
        print('Filling "' + self.path + '" with contents of "' + fill_with + '"...')
        try:
            copytree(fill_with, self.path) # copytree(source, destination)
            print 'Copy complete. [OK]'
            return True
        except Exception as error: 
            print 'Copy failed. [ERROR]'
            print error

    ################
    # Properties

    @property
    def path(self):
        """Returns the path."""
        return self.__path

    @Node.path.setter
    def path(self, path):
        """Sets the path."""
        # Check for None
        if path == None:
            return
        # Force directory to end in '/'
        if not path.endswith('/'):
            path = path + '/'
        Node.path.fset(self, path)
