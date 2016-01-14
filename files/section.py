#!/usr/bin/env python
#
# name:             section.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/09/2016
#
# description:      A file to process template section files. A template
#                   section file is a template of a configuration file that
#                   only represents a particular section of that file. It
#                   begins and ends with a delineator (for example:
#                   ## START:SECTION_NAME ## and ## END:SECTION_NAME ##). A Use
#                   case would be how WordPress delineates a particular section of
#                   the htaccess file in its root directory with a start line
#                   and an end line. This is a section of the full htaccess
#                   file and could be managed by a SectionFile.
#

from file import File
from ext_pylib.prompt import prompt


# SectionFile(atts)
#   An class to work with a section template file.
#
#   methods:
#       apply_to(data)
class SectionFile(File):

    def __str__(self):
        """Returns a string with the path."""
        if not self.path:
            return '<file.SectionFile:stub>'
        return self.path

    def is_applied(self, data):
        return self.read() in data

    def has_section(self, data):
        self._start_pos = data.find(self.start_section)
        self._end_pos = data.find(self.start_section)
        if start_pos < 0 and end_pos < 0:
            return false
        elif start_pos < end_pos:
            return true
        else:
            print '[WARN] Data not formatted properly.'
            return false

    def apply_to(self, data, overwrite=False):
        if is_applied(data):
            return data
        if has_section(data):
            if overwrite:
                return data[:self._start_pos] + self.read() + \
                        data[self._end_pos + len(self.end_section) + 1:]
            else:
                # error ?
                return None
        else:
            return data + '\n' + self.read() + '\n'

    @property
    def start_section(self):
        return self.readlines()[0]

    @property
    def end_section(self):
        return self.readlines()[len(self.readlines())-1]
