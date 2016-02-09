#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_section.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/10/2016
#
# pylint:           disable=invalid-name,line-too-long

"""
A unit test for ext_pylib file module's Section mixin class.
"""

import pytest
from ext_pylib.files import Section
from ext_pylib.files.file import AlteredSectionFile


SECTION_STR = """## START SECTION Test
This is the second line.
This is the third line.
## END SECTION Test"""

FILE_WITH_SECTION_STR = """This string has the section.
## START SECTION Test
This is the second line.
This is the third line.
## END SECTION Test
This string has the section.
This string has the section.
"""

FILE_HAS_SECTION_STR = """This string has the section.
## START SECTION Test
But it has been changed...
## END SECTION Test
This string has the section.
This string has the section.
"""

FILE_WITHOUT_SECTION_STR = """This string does not have the section.
This string does not have the section.
This string does not have the section.
This string does not have the section.
"""

FILE_WITHOUT_SECTION_STR_APPLIED = """This string does not have the section.
This string does not have the section.
This string does not have the section.
This string does not have the section.
## START SECTION Test
This is the second line.
This is the third line.
## END SECTION Test
"""

# Monkey Patch function for read() method
def read():
    """Monkey Patch read function."""
    return SECTION_STR

# Monkey Patch function for readline() method
def readlines(self):
    """Monkey Patch readlines function."""
    return self.read().split('\n')

Section.readlines = readlines

def test_section_is_applied():
    """Test Section is_applied method."""
    file = Section()
    file.read = read
    assert file.is_applied(FILE_WITH_SECTION_STR)
    assert not file.is_applied(FILE_WITHOUT_SECTION_STR)

def test_section_has_section():
    """Test Section has_section method."""
    file = Section()
    file.read = read
    assert file.has_section(FILE_HAS_SECTION_STR)
    assert file.has_section(FILE_WITH_SECTION_STR)
    assert not file.has_section(FILE_WITHOUT_SECTION_STR)

def test_section_apply_to():
    """Test Section apply_to method."""
    file = Section()
    file.read = read
    assert file.apply_to(FILE_WITH_SECTION_STR) == FILE_WITH_SECTION_STR
    assert file.apply_to(FILE_WITHOUT_SECTION_STR) == FILE_WITHOUT_SECTION_STR + '\n' + SECTION_STR + '\n'
    with pytest.raises(AlteredSectionFile):
        file.apply_to(FILE_HAS_SECTION_STR, overwrite=False)
    assert file.apply_to(FILE_HAS_SECTION_STR, overwrite=True) == FILE_WITH_SECTION_STR

MULTILINE_STR = """This is the first line.
This is the second line.
This is the last line."""

MULTILINE_STR_WITH_RETURN = """This is the first line.
This is the second line.
This is the last line.
"""

# Monkey Patch function for read() method
def read_multiline_str():
    """Monkey Patch read function that returns a multiline string."""
    return MULTILINE_STR

# Monkey Patch function for read() method
def read_multiline_str_with_return():
    """Monkey Patch read function that returns a multiline string with a newline."""
    return MULTILINE_STR_WITH_RETURN

def test_section_start_section_property():
    """Test Section start_section property."""
    file = Section()
    file.read = read_multiline_str
    assert file.start_section == "This is the first line."
    file.read = read_multiline_str_with_return
    assert file.start_section == "This is the first line."

def test_section_end_section_property():
    """Test Section end_section property."""
    file = Section()
    file.read = read_multiline_str
    assert file.end_section == "This is the last line."
    file.read = read_multiline_str_with_return
    assert file.end_section == "This is the last line."
