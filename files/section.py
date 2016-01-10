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
#                   begins and ends with a delineator (by default: ##
#                   START:SECTION_NAME ## and ## END:SECTION_NAME ##). For
#                   example: WordPress delineates a particular section of the
#                   htaccess file in its root directory with a start line and
#                   an end line. This is a section of the full htaccess file. A
#                   file containing only this section with the first line as
#                   the start delineator and the last line as the end
#                   dilineatro is a template section file.
#

from file import File
from ext_pylib.prompt import prompt


# SectionFile(atts)
#   An class to work with a section template file.
#
#   methods:
#       apply_to(data)
class SectionFile(File):

    def __init__(self, atts):
        # Section must have a name (set to self.name in super(File))
        if 'name' not in atts:
            raise KeyError('A SectionFile must have a "name" set in atts.')
        # Set defaults, these can be overridden by:
        # atts = {'start_section' : '# Begin Section Name',
        #         'end_section' : '# End section' }
        # (along with all expected file atts)
        self.start_section = '# BEGIN ' + self.name
        self.end_section = '# END ' + self.name
        super(File, self).__init__(atts)

    def __str__(self):
        """Returns a string with the path."""
        if not self.path:
            return '<file.SectionFile:stub>'
        return self.path

    def apply_to(self, data):
        # TODO:
        # search for start and end line, if not there:
        return data + '\n' + self.start_section + self.read() + self.end_section + '\n'
