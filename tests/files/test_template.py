#!/usr/bin/env python
#
# name:             test_template.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/09/2016
#
# description:      A unit test for ext_pylib file module's Template mixin
#                   class.
#

from ext_pylib.files import Template
import pytest


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

# Monkey Patch function for read() method
def read():
    return TEMPLATE_FILE

def test_templatefile_apply_using():
    """Test Section apply_using() method."""
    file = Template()
    file.read = read
    assert EXPECTED_RESULT == file.apply_using({
        '#PLACEHOLDER#' : 'The placeholder text.',
         '#DATA#' : 'www.google.com',
         '#MISSING#' : 'Nothing here.',
        })
