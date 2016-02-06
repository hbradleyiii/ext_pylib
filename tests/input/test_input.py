#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_input.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/07/2015
#

"""
A unit test for ext_pylib module's input functions.
"""

import mock
import pytest

from ext_pylib.input import prompt, prompt_str, warn_prompt

_INPUT = 'ext_pylib.input.prompts.INPUT'

@pytest.mark.parametrize(("prompt_text", "default", "response", "expected"), [
    ('Answer the question', True, [''], True),
    ('Answer the question', False, [''], False),
    ('Answer the question', True, ['y'], True),
    ('Answer the question', True, ['Y'], True),
    ('Answer the question', True, ['YES'], True),
    ('Answer the question', True, ['yEs'], True),
    ('Answer the question', True, ['n'], False),
    ('Answer the question', True, ['N'], False),
    ('Answer the question', False, ['y'], True),
    ('Answer the question', False, ['n'], False),
    ('', True, ['y'], True),
    ('', True, ['n'], False),
    ('Answer the question', True, ['x', 'Z', 'n'], False),
    ('Answer the question', True, ['asdyes', 'nno', 'yesno', 'y'], True),
])
def test_prompt(prompt_text, default, response, expected):
    """Test prompt function."""

    with mock.patch(_INPUT, side_effect=response):
        assert prompt(prompt_text, default) == expected

@pytest.mark.parametrize(("prompt_text", "response", "expected"), [
    ('Answer the question', 'y', True),
    ('Answer the question', 'n', False),
    ('Answer the question', '', True),
])
def test_prompt_no_default(prompt_text, response, expected):
    """Test prompt function with bad input."""
    with mock.patch(_INPUT, return_value=response):
        assert prompt(prompt_text) == expected

@pytest.mark.parametrize(("prompt_text", "default", "response", "expected"), [
    ('Answer the question', 'Answer', '', 'Answer'),
    ('Answer the question', 'Answer', 'Answer', 'Answer'),
    ('Answer the question', 'Answer', 'anotheranswer', 'anotheranswer'),
])
def test_prompt_str(prompt_text, default, response, expected):
    """Test prompt_str function."""
    with mock.patch(_INPUT, return_value=response):
        assert prompt_str(prompt_text, default) == expected

@pytest.mark.parametrize(("prompt_text", "default", "response", "expected"), [
    ('Delete all of your files?', 'DELETE', ['n'], False),
    ('Delete all of your files?', 'DELETE', ['x', 'asdf', 'DELETE'], True),
    ('Delete all of your files?', 'DELETE', ['delete', 'asdf', 'n'], False),
])
def test_warn_prompt(prompt_text, default, response, expected):
    """Test warn_prompt function."""
    with mock.patch(_INPUT, side_effect=response):
        assert warn_prompt(prompt_text, default) == expected
