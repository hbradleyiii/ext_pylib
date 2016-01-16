#!/usr/bin/env python
#
# name:             section.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/16/2016
#
# description:      A
#

from file import File

# ParsableFile(atts)
#   An class to work with a configuration file in order to parse for use.
#
#   methods:
#       apply_to(data)
class ParsableFile(File):

    def __str__(self):
        """Returns a string with the path."""
        if not self.path:
            return '<file.ParsableFile:stub>'
        return self.path

    def parse(self, var):
        pass
