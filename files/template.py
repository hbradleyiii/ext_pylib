#!/usr/bin/env python
#
# name:             template.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/07/2016
#
# description:      A file to process template files.
#

from file import File
from ext_pylib.prompt import prompt


# TemplateFile(atts)
#   An class to work with a template file. This class inherits from File, so
#   has all the methods and attributes of class File. It adds one primary
#   method: apply_using(). It assumes that the file contains placeholder text
#   to be replaced by actual data. The placeholders and actual data are passsed
#   into the method as a dict. The resulting data is returned (presumably to be
#   saved in another file.
#
#   methods:
#       apply_using(placeholders)
class TemplateFile(File):

    def __str__(self):
        """Returns a string with the path."""
        if not self.path:
            return '<file.TemplateFile:stub>'
        return self.path

    def apply_using(self, placeholders):
        _data = self.read()
        for placeholder in placeholders:
            pass  # Find and replace
        return _data
