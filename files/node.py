#!/usr/bin/env python
#
# name:             node.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/03/2015
#
# description:      An abstract class that describes a node to be extended by a
#                   directory and file class respectively.
#

import grp
import os
import pwd


# Node(atts)
#   An abstract class that is primarily a wrapper for directory and file
#   managment. This class is intended to be extended by file and directory
#   classes.
#
#   Node is initialized with a dict of attributes. Attributes that aren't
#   given are just initialized as None. If a path isn't given, the node is set
#   to path = None. This effectively makes the Node a "Stub", in which methods
#   do nothing but return True (except exists()) enabling a graceful fail.
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
#       chmod(perms)
#       chown(owner, group)
#       verify(repair)
#       repair()
#       exists()
class Node(object):

    def __init__(self, atts = {} ):
        """Initializes a new Node instance."""
        if 'path' not in atts:
            self.path = None # !! Make sure path is at least initialized
        for attribute in atts:
            setattr(self, attribute, atts[attribute])

    def __str__(self):
        """Returns a string with the path."""
        if not self.path:
            return '<files.Node:stub>'
        return self.path

    def __repr__(self):
        """Returns a python string that evaluates to the object instance."""
        return "%s(%s)" % (self.__class__.__name__, self._atts_())

    def __add__(self, other):
        """Allows string concatenation with the path."""
        return str(self) + other

    def __radd__(self, other):
        """Allows string concatenation with the path."""
        return other + str(self)

    def _atts_(self):
        """Returns a python string of attributes (as a dict) used to create this object."""
        # Note that any atts added later must be added here for this to work.
        atts = "{'path' : "
        if self.path:
            atts += "'" + self.path + "', "
        else:
            atts += 'None, '

        atts += "'perms' : "
        if self.perms:
            atts += self.perms + ", "
        else:
            atts += 'None, '

        atts += "'owner' : "
        if self.owner:
            atts += "'" + self.owner + "', "
        else:
            atts += 'None, '

        atts += "'group' : "
        if self.group:
            atts += "'" + self.group + "'}"
        else:
            atts += 'None}'

        return atts

    def create(self):
        raise NotImplementedError('[ERROR] Cannot call method on file.Node. It is an abstract class.')

    def remove(self, ask = True):
        raise NotImplementedError('[ERROR] Cannot call method on file.Node. It is an abstract class.')

    def verify(self, repair = False):
        """Verifies the existence, permissions, ownership, and group of the file/directory."""
        if not self.path:
            return True
        print ''
        print 'Checking ' + self.path + '...'
        if not self.exists():
            print '[!] ' + self.path + ' doesn\'t exist'
            if not repair:
                return False
            self.create()
            return self.verify(repair)

        # Assume the checks pass
        perms_check = owner_check = group_check = True

        if self.perms:
            print '--> Checking permissions for ' + self.path,
            perms_check = self.perms == self.actual_perms
            print ' (should be: ' + oct(self.perms) + ', actual: ' + oct(self.actual_perms) + ')',
            print '[OK]' if perms_check else '[ERROR]'
            if not perms_check and repair:
                perms_check = self.chmod()
                return self.verify(repair)

        if self.owner:
            print '--> Checking owner for ' + self.path,
            owner_check = self.owner == self.actual_owner
            print ' (should be: ' + self.owner + ', actual: ' + self.actual_owner + ')',
            print '[OK]' if owner_check else '[ERROR]'

        if self.group:
            print '--> Checking group for ' + self.path,
            group_check = self.group == self.actual_group
            print ' (should be: ' + self.group + ', actual: ' + self.actual_group + ')',
            print '[OK]' if group_check else '[ERROR]'
            if not (group_check or owner_check) and repair:
                group_check = owner_check = self.chown()
                return self.verify(repair)

        return perms_check and owner_check and group_check

    def repair(self):
        """Runs verify() with the repair flag set."""
        return self.verify(True)

    def chmod(self, perms = None):
        """Sets the permissions on the file/directory."""
        if not self.path:
            return True
        if not self.exists():
            raise IOError(self.path + ' does not exist. Cannot set owner and permissions. [!]')
        if not perms:
            perms = self.perms
        print('Setting permissions on ' + self.path + ' to "' + format(perms, '04o')  + '"...'),
        try:
            os.chmod(self.path, perms) # Be sure to use leading '0' as chmod takes an octal
            print('[OK]')
            return True
        except Exception as error:
            print '[ERROR]'
            print error

    def chown(self, owner = None, group = None):
        """Sets the owner and group of the directory."""
        if not self.path:
            return True
        if not self.exists():
            raise IOError(self.path + ' does not exist. Cannot set owner and permissions. [!]')
        if not owner:
            owner = self.owner
        if not group:
            group = self.group
        print('Setting owner on ' + self.path + ' to "' + owner  + ':' + group + '"...'),
        try:
            uid = pwd.getpwnam(owner).pw_uid
            gid = grp.getgrnam(group).gr_gid
            os.chown(self.path, uid, gid)
            print('[OK]')
            return True
        except Exception as error:
            print '[ERROR]'
            print error

    def exists(self):
        """Returns true if this directory exists on disk."""
        if not self.path:
            return False
        if os.path.exists(self.path):
            return True
        return False

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
        return None if not getattr(self, '_perms', None) else oct(getattr(self, '_perms', None))

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
