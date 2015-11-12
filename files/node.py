#!/usr/bin/env python
#
# name:             node.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/03/2014
#
# description:      An abstract class that describes a node to be extended by a
#                   directory and file class respectively.
#

import grp
import os
from ext_pylib import prompt
import pwd
import shutil


# Node(atts)
#   An abstract class that is primarily a wrapper for directory and file
#   managment. This class is intended to be extended by file and directory
#   classes.
#
#   Node is initialized with a dict of attributes. Attributes that aren't
#   given are just initialized as None. If a path isn't given, the node is set
#   to path = None. This effectively makes the Node a "Stub". Methods do
#   nothing but return True (except exists()) enabling a graceful fail.
#
#   atts dict can have the following values:
#       path: the full (NOT relative) path of the node
#       perms: the (int) permissions of the node
#       owner: the (string) owner of the node
#       group: the (string) group of the node
#
#   methods:
#       create()
#       remove(ask)
#       fill(fill_with)
class Node(object):

    def __init__(self, atts = {} ):
        """Initializes a new Node instance."""
        self.path = None # !! Make sure path is at least initialized
        for attribute in atts:
            setattr(self, attribute, atts[attribute])

    def __str__(self):
        """Returns a string with the path."""
        if not self.path:
            return '<file.Node:stub>'
        return self.path

    def __repr__(self):
        """Returns a string with the path."""
        return self.__str__()

    def __add__(self, other):
        """Allows string concatenation with the path."""
        return str(self) + other

    def __radd__(self, other):
        """Allows string concatenation with the path."""
        return other + str(self)

    def create(self):
        raise NotImplementedError('[ERROR] Cannot call method on file.Node. It is an abstract class.')

    def remove(self, ask = True):
        raise NotImplementedError('[ERROR] Cannot call method on file.Node. It is an abstract class.')

    ################
    # Properties

    @property
    def path(self):
        """Returns the path, if it exists."""
        return getattr(self, '_path', None)

    @path.setter
    def path(self, path):
        """Validates, then sets the path."""
        # Check for None
        if path == None:
            print '[Notice] file.Node was initialized with an empty path. Continuing as a stub.'
            self._path = None
            return
        # Check for empty string
        if path == '':
            raise ValueError('"path" cannot be set to an empty string in an file.Node class.')
        # Check for valid characters
        for char in path:
            if char not in '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/':
                raise ValueError('"' + path + '" is not allowed as an file.Node.')
        # Directory must start with '/'
        if not path.startswith('/'):
            raise ValueError('Relative paths (' + path + ') are not allowed as an file.Node.')
        # Clean path of extra slashes
        while "//" in path:
            path = path.replace('//', '/')
        self._path = path

    @property
    def parent_dirs(self):
        """Returns the parent directories."""
        if not self.path:
            return None
        path = self.path
        if not path.endswith('/'):
            path = path + '/'
        return path.rsplit('/', 2)[0] + '/'

    @property
    def actual_perms(self):
        """Returns the perms as it is on disk."""
        if not self.path:
            return None
        return os.stat(self.path).st_mode & 511 

    @property
    def perms(self):
        """Returns the perms (string)."""
        return getattr(self, '_perms', None)

    @perms.setter
    def perms(self, perms):
        """Sets the perms (string)."""
        try:
            perms = int(perms)
        except ValueError as e: 
            print e
            print '[ERROR] ' + perms + ' must be set to an int.'
            raise
        # Check for empty string
        # if perms == '':
        #     raise ValueError('"perms" cannot be set to an empty string in an file.Node class.')
        if perms < 0 or 511 < perms:
            raise ValueError('"perms" cannot be set to ' + str(perms) + '.')
        self._perms = perms

    @property
    def actual_owner(self):
        """Returns the owner (string) as it is on disk."""
        if not self.path:
            return None
        return pwd.getpwuid(os.stat(self.path).st_uid).pw_name

    @property
    def owner(self):
        """Returns the owner (string)."""
        return getattr(self, '_owner', None)

    @owner.setter
    def owner(self, owner):
        """Sets the owner (string)."""
        if owner == None:
            owner = 'nobody'
        else:
            try:
                # Is this a valid user?
                uid = pwd.getpwnam(owner)
            except KeyError: 
                print '[ERROR] ' + owner + ' is not a valid user.'
                raise
        self._owner = owner

    @property
    def actual_group(self):
        """Returns the group (string) as it is on disk."""
        if not self.path:
            return None
        return grp.getgrgid(os.stat(self.path).st_gid).gr_name

    @property
    def group(self):
        """Returns the group (string)."""
        return getattr(self, '_group', None)

    @group.setter
    def group(self, group):
        """Sets the group (string)."""
        # Check for empty string
        if group == None:
            group = 'nobody'
        else:
            try:
                # Is this a valid group?
                gid = grp.getgrnam(group)
            except KeyError: 
                print '[ERROR] ' + group + ' is not a valid group.'
                raise
        self._group = group
