#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_password.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/07/2015
#
# pylint:           disable=invalid-name

"""
A unit test for ext_pylib module's password functions.
"""

import pytest

from ext_pylib.password import generate_pw
from ext_pylib.password.password import DEFAULT_CHAR_SET

@pytest.mark.parametrize(("length", "charset", "expected"), [
    (1, {'a' : 'a'}, 'a'),
    (1, {'a' : '$'}, '$'),
])
def test_generate_pw(length, charset, expected):
    """Tests generate_pw function."""
    assert generate_pw(length, charset) == expected

@pytest.mark.parametrize(("length", "charset", "expected"), [
    (1, DEFAULT_CHAR_SET, 1),
    (5, DEFAULT_CHAR_SET, 5),
    (10, {'set' : 'abc', 'set2' : 'ABC'}, 10),
    (20, {'set' : 'abc', 'set2' : 'ABC'}, 20),
])
def test_generate_pw_length(length, charset, expected):
    """Testsgenerate_pw_length function."""
    assert len(generate_pw(length, charset)) == expected

def test_generate_pw_no_dup_char_sets():
    """Tests that generate_pw doesn't use the same subset twice in a row."""
    for _ in range(50):
        password = generate_pw(2, {'a' : 'a', 'b' : 'b'})
        assert password != 'aa'
        assert password != 'bb'
