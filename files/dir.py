#!/usr/bin/env python
#
# name:             mm_dir.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/03/2015
#
# description:      A class that describes a directory and gives functions to
#                   create the directory. It extends Node.
#

from node import Node
import os
from ext_pylib.prompt import prompt
import shutil


# copytree(source, destination, symlinks, ignore)
#   allow copying into directories that already exist
#   adapted from: http://stackoverflow.com/questions/1868714
def copytree(source, destination, symlinks=False, ignore=None):
    for item in os.listdir(source):
        item_src = os.path.join(source, item)
        item_dst = os.path.join(destination, item)
        if os.path.isdir(item_src): # It's a directory
            if os.path.exists(item_dst): # It's a directory that already exists
                copytree(item_src, item_dst)
            else:
                shutil.copytree(item_src, item_dst, symlinks, ignore)
            return True
        else: # It's a file
            if os.path.exists(item_dst):
                if not prompt(item_dst + ' already exists. Replace with ' + item_src + '?'):
                    print 'Skipping.'
                    return True
                os.remove(item_dst) # It's a file that already exists; remove it, then copy
            shutil.copy2(item_src, item_dst)
            return True


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
            return True
        print('Creating directories "' + self.path + '"...'),
        try:
            os.makedirs(self.path)
            print '[OK]'
            return True
        except Exception as error:
            print '[ERROR]'
            print error
        return self.chmod() and self.chown()

    def remove(self, ask = True):
        """Removes the directory structure."""
        if not self.path:
            return True
        if not self.exists():
            print self.path + ' doesn\'t exist.'
            return True
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
        """Fills the directory with the contents of "fill_with" (a Dir instance)."""
        if not self.exists():
            print 'Copy failed. [ERROR]'
            raise IOError(self.path + 'does not exist')
        if not fill_with.exists(): # Requires a Dir object, NOT a string
            print 'Copy failed. [ERROR]'
            raise IOError(fill_with + 'does not exist')
        print('Filling "' + self.path + '" with contents of "' + fill_with + '"...')
        try:
            copytree(fill_with.path, self.path) # copytree(source, destination)
            print 'Copy complete. [OK]'
            return True
        except Exception as error:
            print 'Copy failed. [ERROR]'
            print error

    ################
    # Properties

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

    @property
    def parent_dir(self):
        return Dir(self.parent_node._atts_())
