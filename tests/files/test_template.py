#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_template.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/09/2016

"""
A unit test for ext_pylib file module's Template mixin class.
"""

from ext_pylib.files import Template
from . import utils


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

def test_templatefile_apply_using():
    """Test Section apply_using() method."""
    the_file = Template()
    the_file.read = utils.mock_read(TEMPLATE_FILE)
    assert EXPECTED_RESULT == the_file.apply_using({
        '#PLACEHOLDER#' : 'The placeholder text.',
        '#DATA#' : 'www.google.com',
        '#MISSING#' : 'Nothing here.',
    })
