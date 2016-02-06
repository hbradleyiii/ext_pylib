#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             password.py
# adapted from:     http://code.activestate.com/recipes/578169-extremely-strong-password-generator/
# maintainer:       Harold Bradley III
# email:            harold@bradleystudio.net
#

"""
ext_pylib.password.password
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module helps with creating passwords.
"""

from random import choice
from os import urandom


# Defines the default characters for use in generating a password
DEFAULT_CHAR_SET = {
    'small': 'abcdefghijklmnopqrstuvwxyz',
    'nums': '0123456789',
    'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'special': '^!$%&=?{[]}+~#-_.:,;<>|'
}

def generate_pw(length=18, char_set=None):
    """Generates a pseudo-randomly generated password and returns it as a string."""
    char_set = char_set or DEFAULT_CHAR_SET
    password = []

    while len(password) < length:
        character = urandom(1)
        subset = choice(list(char_set.keys()))  # Get a random subset of characters
                                                # from which to choose
        # Make sure character is in subset
        if character in char_set[subset]:
            # Make sure it isn't the same subset as the previous character
            if password and password[-1] in char_set[subset]:
                continue  # Try again
            else:
                password.append(character)

    return ''.join(password)
