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
