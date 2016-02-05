#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_integration.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       12/17/2015
#
# description:      Integration tests for ext_pylib's file module.
#

from __future__ import print_function, unicode_literals
from datetime import datetime
from ext_pylib.files import Dir, File, Section
import pytest


@pytest.fixture()
def root(request):
    """Sets up a root directory to use for testing."""
    root_dir = Dir({'path' : '/tmp/ext_pylib/' + datetime.now().strftime('%Y-%m-%d--%H-%M-%S')})
    assert root_dir.remove(False) # If it already exists, remove it.
    assert root_dir.create()
    assert root_dir.exists()

    def cleanup():
        # Cleanup
        assert root_dir.remove(False)
        assert not root_dir.exists()

    request.addfinalizer(cleanup)

    return root_dir


#@root
def test_copytree(root):
    """TODO:"""
    root
    # assert root.exists

def test_dir_actual_create_and_remove():
    """[Integration Test] Test actual creation and removal of directory."""
    # Setup a root dir to use to test
    root_dir = Dir({'path' : '/tmp/ext_pylib/'})
    assert root_dir.remove(False) # If it already exists, remove it.
    assert root_dir.create()
    assert root_dir.exists()

    # Perform a (redundant) creation test
    dir = Dir({'path' : '/tmp/ext_pylib/' + datetime.now().strftime('%Y-%m-%d--%H-%M-%S') + '/path/dir'})
    assert not dir.exists()
    assert dir.create()
    assert dir.exists()

    # Perform a removal test
    assert dir.remove(False)
    assert not dir.exists()

    # Cleanup
    assert root_dir.remove(False)
    assert not root_dir.exists()

def test_file_actual_creation_write_and_removal(tmpdir):
    """[Integration Test] Test actual creation, writing, and removal of file."""
    tmpdir


    ## Strings for Section template file integration tests. ##

SECTION_FILE_CONTENTS = """## START: Testing Section Template

This is just a section for integration tests.

It is used in tests for ext_pylib.files.section.SectionFile.

## END: Testing Section Template
"""

FILE_CONTENTS_WITH_SECTION = """This is a test file that does not contain the contents of section.

It is used for integration tests.

## START: Testing Section Template

This is just a section for integration tests.

It is used in tests for ext_pylib.files.section.SectionFile.

## END: Testing Section Template

"""

FILE_CONTENTS_WITH_SECTION_ALTERED = """file_with_template_altered

This is a test file that contains the contents of template, but the contents
are altered.

It is used for integration tests.

## START: Testing Template

This is just a template for integration tests.

It is altered for testing purposes.

It is used in tests for ext_pylib.files.section.SectionFile.

## END: Testing Template

This is a test file that contains the contents of template, but the contents
are altered.

It is used for integration tests.

"""

FILE_CONTENTS_WITHOUT_SECTION = """This is a test file that does not contain the contents of section.

It is used for integration tests.
"""

def test_section_file_apply_to_file():
    """[Integration Test] Test apply_to_file() method of Section class."""
    # Setup a root dir to use to test
    root_dir = Dir({'path' : '/tmp/ext_pylib/'})
    assert root_dir.remove(False) # If it already exists, remove it.
    assert root_dir.create()
    assert root_dir.exists()

    file_without_section = File({'path' : '/tmp/ext_pylib/file'})
    assert file_without_section.create()
    assert file_without_section.overwrite(FILE_CONTENTS_WITHOUT_SECTION)
    assert file_without_section.exists()

    class SectionFile(Section, File):
        """Dummy Class extending Section and File."""

    section = SectionFile({'path' : '/tmp/ext_pylib/section'})
    assert section.create()
    assert section.overwrite(SECTION_FILE_CONTENTS)
    assert section.exists()

    file_with_section = File({'path' : '/tmp/ext_pylib/file_with_section'})
    assert file_with_section.create()
    assert file_with_section.overwrite(FILE_CONTENTS_WITH_SECTION)
    assert file_with_section.exists()

    assert section.has_section(file_with_section.read())
    print('Without:')
    print(file_without_section.read())
    print('Without (Applied):')
    print(section.apply_to(file_without_section.read()))
    print('With:')
    print(file_with_section.read())
    assert section.apply_to(file_without_section.read()) == file_with_section.read()

    # Cleanup
    assert root_dir.remove(False)
    assert not root_dir.exists()
