#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ext_pylib.input
~~~~~~~~~~~~~~~~

Functions for displaying and handling input on the terminal.
"""

from __future__ import absolute_import

# Use Python 3 input if possible
try:
    INPUT = input
except NameError:
    INPUT = raw_input

# pylint: disable=wrong-import-position
# this import MUST be after INPUT is defined
from .prompts import prompt, prompt_str, warn_prompt
