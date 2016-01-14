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

def test_sectionfile_is_applied():
    """TODO: Test initialize SectionFile."""
    pass

def test_sectionfile_has_section():
    """TODO: Test initialize SectionFile."""
    pass

def test_sectionfile_apply_to():
    """TODO: Test initialize SectionFile."""
    pass

def test_sectionfile_start_section_property():
    """TODO: Test initialize SectionFile."""
    pass

def test_sectionfile_end_section_property():
    """TODO: Test initialize SectionFile."""
    pass
