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


def test_sectionfile_initialization_without_name():
    """Test initialize SectionFile without a name."""
    with pytest.raises(KeyError):
        file = SectionFile()

def test_sectionfile_initialization_with_name():
    """Test initialize SectionFile with a name."""
    file = SectionFile({ 'name' : 'the_name' })
    assert file.name == 'the_name'

def test_sectionfile_str_without_path():
    """Test SectionFile __str__ without path."""
    file = SectionFile({ 'name' : 'the_name' })
    assert str(file) == '<file.SectionFile:stub>'

def test_sectionfile_str_with_path():
    """Test SectionFile __str__ with path."""
    file = SectionFile({ 'name' : 'the_name', 'path' : '/the/path'  })
    assert str(file) == '/the/path'

def test_sectionfile_apply_to():
    """TODO: Test initialize SectionFile."""
    pass
