#!/usr/bin/env python
#
# name:             test_password.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/07/2014
#
# description:      A unit test for ext_pylib module's password functions.
#

from ext_pylib.password import generate_pw
from ext_pylib.password.password import is_like_previous_char
from ext_pylib.password.password import DEFAULT_CHAR_SET
import pytest

@pytest.mark.parametrize(("length", "charset", "expected"), [
    (1, {'a' : 'a'}, 'a'),
    (1, {'a' : '$'}, '$'),
])
def test_generate_pw(length, charset, expected):
    """Test generate_pw function"""
    assert generate_pw(length, charset) == expected

@pytest.mark.parametrize(("length", "charset", "expected"), [
    (1, DEFAULT_CHAR_SET, 1),
    (5, DEFAULT_CHAR_SET, 5),
    (10, {'set' : 'abc', 'set2' : 'ABC'}, 10),
    (20, {'set' : 'abc', 'set2' : 'ABC'}, 20),
])
def test_generate_pw_length(length, charset, expected):
    """Test initializing envi_file"""
    assert len(generate_pw(length, charset)) == expected


@pytest.mark.parametrize(("pw", "charset", "expected"), [
    ('', DEFAULT_CHAR_SET['big'], False),
    ('a', DEFAULT_CHAR_SET['small'], True),
    ('$', DEFAULT_CHAR_SET['special'], True),
    ('W1$z', DEFAULT_CHAR_SET['big'], False),
])
def test_is_like_previous_char(pw, charset, expected):
    """Test initializing envi_file"""
    assert is_like_previous_char(pw, charset) == expected
