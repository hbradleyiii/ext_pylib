#!/usr/bin/env python
#
# name:             test_section.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/10/2016
#
# description:      A unit test for ext_pylib file module's Section class.
#

from ext_pylib.files import SectionFile
from mock import patch
import pytest


def test_sectionfile_str_without_path():
    """Test SectionFile __str__ without path."""
    file = SectionFile()
    assert str(file) == '<file.SectionFile:stub>'

def test_sectionfile_str_with_path():
    """Test SectionFile __str__ with path."""
    file = SectionFile({ 'path' : '/the/path'  })
    assert str(file) == '/the/path'

SECTION_STR = """## START Section Test
This is the second line.
This is the third line.
## END Section Test"""

FILE_WITH_SECTION_STR = """This string has the section.
## START Section Test
This is the second line.
This is the third line.
## END Section Test
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
## START Section Test
This is the second line.
This is the third line.
## END Section Test
"""


@patch('ext_pylib.files.file.File.read')
def test_sectionfile_is_applied(mock_read):
    """Test SectionFile is_applied method."""
    file = SectionFile()
    mock_read.return_value = SECTION_STR
    assert file.is_applied(FILE_WITH_SECTION_STR)
    assert not file.is_applied(FILE_WITHOUT_SECTION_STR)

def test_sectionfile_has_section():
    """TODO: Test initialize SectionFile."""
    pass

def test_sectionfile_apply_to():
    """TODO: Test initialize SectionFile."""
    pass

MULTILINE_STR = """This is the first line.
This is the second line.
This is the last line."""

MULTILINE_STR_WITH_RETURN = """This is the first line.
This is the second line.
This is the last line.
"""

@patch('ext_pylib.files.file.File.read')
def test_sectionfile_start_section_property(mock_read):
    """Test SectionFile start_section property."""
    mock_read.return_value = MULTILINE_STR
    file = SectionFile()
    assert file.start_section == "This is the first line."
    mock_read.return_value = MULTILINE_STR_WITH_RETURN
    assert file.start_section == "This is the first line."

@patch('ext_pylib.files.file.File.read')
def test_sectionfile_end_section_property(mock_read):
    """Test SectionFile end_section property."""
    mock_read.return_value = MULTILINE_STR
    file = SectionFile()
    assert file.end_section == "This is the last line."
    mock_read.return_value = MULTILINE_STR_WITH_RETURN
    assert file.end_section == "This is the last line."
