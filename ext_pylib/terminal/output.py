#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             output.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       03/24/2016
#
# pylint:           disable=invalid-name
#                   x and y are valid names.

"""
ext_pylib.terminal.output
~~~~~~~~~~~~~~~~~~~~~~~

Functions for pretty terminal output.
"""

from __future__ import absolute_import, print_function

from sys import stdout

from . import ansi
from . import colors as c

def indicate_ok():
    """Prints 'ok' message on previous line aligned to the right."""
    print_right('[' + c.green('OK') + ']', 5)

def indicate_error():
    """Prints 'error' message on previous line aligned to the right."""
    print_right('[' + c.red('ERROR') + ']', 8)

def indicate_warn():
    """Prints 'warn' message on previous line aligned to the right."""
    print_right('[' + c.yellow('WARN') + ']', 7)

def print_right(string, offset=None):
    """Prints a string to the previous line aligned to the right."""
    ansi.cursor_save()
    x, _ = ansi.get_window_size()
    string_length = offset if offset else len(string)
    ansi.cursor_previous_line()
    ansi.cursor_right(x - string_length)
    stdout.write(string)
    stdout.flush()
    ansi.cursor_restore()
