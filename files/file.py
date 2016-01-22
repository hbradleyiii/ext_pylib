#!/usr/bin/env python
#
# name:             file.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/04/2015
#
# description:      A class to manage and create files. Also includes three
#                   mixin classes Parsable, Section, and Template.
#
#                   The Section mixin adds methods useful for processing
#                   template section files. A section file is a template of a
#                   configuration file that only represents a particular
#                   section of that file. It begins and ends with a delineator
#                   (for example: ## START:SECTION_NAME ## and ##
#                   END:SECTION_NAME ##). A use case would be how WordPress
#                   delineates a particular section of the htaccess file in its
#                   root directory with a start line and an end line. This is a
#                   section of the full htaccess file and could be managed by a
#                   Section mixin.
#
#                   The Template mixin adds a method useful for processing a
#                   regular template file: apply_using(). It assumes that the
#                   file contains placeholder text to be replaced by actual
#                   data. The placeholders and actual data are passsed into the
#                   method as a dict. The resulting data is returned
#                   (presumably to be saved in another file.)
#
#                   The Parsable mixin adds a method useful for parsing
#                   (presumably) configuration files. It takes a dict of
#                   attribute names and regexes to be used. When parse() is
#                   called, the regex is run on the data and the result (or
#                   None) is assigned to an attribute on the instance.
#                   TODO: how to keep from clobering important attributes?

from dir import Dir
from node import Node
import os
import re
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
        return self.write(data, True, handle)

    def overwrite(self, data, handle=None):
        """Overwrites the file with data. Just a wrapper."""
        return self.write(data, False, handle)

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


# Section()
#   A mixin class to work with a section template file.
#
#   methods:
#       apply_to(data)
class Section():
    def is_applied(self, data):
        """Returns true if data has this section applied exactly."""
        return self.read() in data

    def has_section(self, data):
        """Returns true if data has the section, whether or not it is applied
        exactly."""
        self._start_pos = data.find(self.start_section)
        self._end_pos = data.find(self.end_section)
        if self._start_pos < 0 and self._end_pos < 0:
            return False
        elif self._start_pos < self._end_pos:
            return True
        else:
            print '[WARN] Data not formatted properly.'
            return False

    def apply_to(self, data, overwrite=False):
        """Returns a string in which the section is applied to the data."""
        if self.is_applied(data):
            return data
        if self.has_section(data):
            if overwrite:
                return data[:self._start_pos] + self.read() + '\n' + \
                        data[self._end_pos + len(self.end_section) + 1:]
            else:
                # error ?
                return None
        else:
            return data + '\n' + self.read() + '\n'

    @property
    def start_section(self):
        """Returns the string that denotes the start of the section."""
        return self.readlines()[0]

    @property
    def end_section(self):
        """Returns the string that denotes the end of the section."""
        lines = self.readlines()
        if lines[len(lines)-1] != '':  # If the last line is blank, use the line before it.
            return lines[len(lines)-1]
        return lines[len(lines)-2]


# Template()
#   A mixin to work with a template file with placeholders.
#
#   methods:
#       apply_using(placeholders)
class Template():
    def apply_using(self, placeholders):
        _data = self.read() # temp, throw-away (after returning) data value
        for placeholder, value in placeholders.iteritems():
            _data = _data.replace(placeholder, value)
        return _data


# Parsable()
#   A mixin to be used with a File class to allow parsing.
#
#   methods:
#       parse(var)
class Parsable():
    def parse(self, regexes):
        for attribute, regex in regexes.iteritems():
            if hasattr(self, attribute):
                raise AttributeError('Cannot use "' + attribute + \
                        '" as parsable attribute of ' + str(self))
            setattr(self, attribute, re.findall(regex, self.read()))
