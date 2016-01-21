#!/usr/bin/env python
#
# name:             test_template.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/09/2016
#
# description:      A unit test for ext_pylib file module's Template class and
#                   methods.
#

from ext_pylib.files import TemplateFile
from mock import patch
import pytest


def test_templatefile_str():
    """Test SectionFile __str__ without path."""
    file = TemplateFile()
    assert str(file) == '<file.TemplateFile:stub>'

TEMPLATE_FILE = """This is a test template file.
#PLACEHOLDER#
This is another #PLACEHOLDER#.
Sample {#DATA#} sample.
#DATA#, #DATA#, and #DATA#.
But not #DATA, DATA#, and DATA.
This is the last line.
"""

EXPECTED_RESULT = """This is a test template file.
The placeholder text.
This is another The placeholder text..
Sample {www.google.com} sample.
www.google.com, www.google.com, and www.google.com.
But not #DATA, DATA#, and DATA.
This is the last line.
"""

@patch('ext_pylib.files.file.File.read')
def test_templatefile_apply_using(mock_read):
    """Test SectionFile apply_using() method."""
    file = TemplateFile()
    mock_read.return_value = TEMPLATE_FILE
    assert EXPECTED_RESULT == file.apply_using({
        '#PLACEHOLDER#' : 'The placeholder text.',
         '#DATA#' : 'www.google.com',
         '#MISSING#' : 'Nothing here.',
        })
