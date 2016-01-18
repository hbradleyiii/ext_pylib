#!/usr/bin/env python
#
# name:             test_parsable.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/16/2016
#
# description:      A unit test for ext_pylib file module's Parsable class and
#                   methods.
#

from ext_pylib.files.parsable import ParsableFile

def test_sectionfile_str_without_path():
    """Test ParsableFile __str__ without path."""
    file = ParsableFile()
    assert str(file) == '<file.ParsableFile:stub>'
