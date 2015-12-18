#!/usr/bin/env python
#
# name:             test_integration.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       12/17/2015
#
# description:      Integration tests for ext_pylib's file module.
#

from datetime import datetime
from ext_pylib.files import Dir
import pytest


@pytest.fixture()
def root(request):
    # Setup a root dir to use to test
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
def xtest_copytree(root):
    """TODO:"""
    # assert root.exists
    pass

