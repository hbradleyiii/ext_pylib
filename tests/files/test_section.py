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
from . import utils


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

FILE_BAD_SECTION_STR = """This string has the section.
## END SECTION Test
But in the wrong order...
## START SECTION Test
This string has the section.
This string has the section.
"""

FILE_BAD_SECTION2_STR = """This string has the section.
## START SECTION Test
But in the no end section...
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

MULTILINE_STR = """This is the first line.
This is the second line.
This is the last line."""

MULTILINE_STR_WITH_RETURN = """This is the first line.
This is the second line.
This is the last line.
"""

# Use mock readlines on Section class
Section.readlines = utils.mock_readlines

def test_section_is_applied():
    """Test Section is_applied method."""
    section_file = Section()
    section_file.read = utils.mock_read(SECTION_STR)
    assert section_file.is_applied(FILE_WITH_SECTION_STR)
    assert not section_file.is_applied(FILE_WITHOUT_SECTION_STR)

def test_section_is_in():
    """Test Section is_in method."""
    section_file = Section()
    section_file.read = utils.mock_read(SECTION_STR)
    assert section_file.is_in(FILE_HAS_SECTION_STR)
    assert section_file.is_in(FILE_WITH_SECTION_STR)
    assert not section_file.is_in(FILE_WITHOUT_SECTION_STR)

def test_section_is_in_bad_data():
    """Test Section is_in method passing in bad data."""
    section_file = Section()
    section_file.read = utils.mock_read(SECTION_STR)
    with pytest.raises(ValueError):
        assert section_file.is_in(FILE_BAD_SECTION_STR)
    with pytest.raises(ValueError):
        assert section_file.is_in(FILE_BAD_SECTION2_STR)

def test_section_apply_to():
    """Test Section apply_to method."""
    section_file = Section()
    section_file.read = utils.mock_read(SECTION_STR)
    assert section_file.apply_to(FILE_WITH_SECTION_STR) == FILE_WITH_SECTION_STR
    assert section_file.apply_to(FILE_WITHOUT_SECTION_STR) == FILE_WITHOUT_SECTION_STR + '\n' + SECTION_STR + '\n'
    with pytest.raises(ValueError):
        section_file.apply_to(FILE_HAS_SECTION_STR, overwrite=False)
    assert section_file.apply_to(FILE_HAS_SECTION_STR, overwrite=True) == FILE_WITH_SECTION_STR

def test_section_start_section_property():
    """Test Section start_section property."""
    section_file = Section()
    section_file.read = utils.mock_read(MULTILINE_STR)
    assert section_file.start_section == "This is the first line."
    section_file.read = utils.mock_read(MULTILINE_STR_WITH_RETURN)
    assert section_file.start_section == "This is the first line."

def test_section_start_section_property_bad_section():
    """Test Section start_section property with invalid section data."""
    section_file = Section()
    section_file.read = utils.mock_read('')
    with pytest.raises(EOFError):
        assert section_file.start_section
    with pytest.raises(EOFError):
        assert section_file.end_section

def test_section_end_section_property():
    """Test Section end_section property."""
    section_file = Section()
    section_file.read = utils.mock_read(MULTILINE_STR)
    assert section_file.end_section == "This is the last line."
    section_file.read = utils.mock_read(MULTILINE_STR_WITH_RETURN)
    assert section_file.end_section == "This is the last line."
