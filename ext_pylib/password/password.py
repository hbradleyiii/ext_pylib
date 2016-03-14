#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             password.py
# maintainer:       Harold Bradley III
# email:            harold@bradleystudio.net
#

"""
ext_pylib.password.password
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A module to create passwords.
"""

from random import choice


# Defines the default characters for use in generating a password
DEFAULT_CHAR_SET = {
    'small': 'abcdefghijklmnopqrstuvwxyz',
    'nums': '0123456789',
    'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'special': '^!$%&=?{[]}+~#-_.:,;<>|'
}

def generate_pw(length=18, char_set=None):
    """Generates a pseudo-randomly generated password and returns it as a string.
    Adapted from: http://code.activestate.com/recipes/578169-extremely-strong-password-generator/

    :param length: the length of the password to generate
    :param char_set: a dict of a string of characters to use as a set. These
        are the set (as a python string) of characters that will not appear
        twice in a row. The default character set has a set of numbers,
        lowercase letters, uppercase letters, and special characters. This
        prevents having a password with two numbers in a row, or two lowercase
        characters in a row and makes the password stronger. Leaving this as
        default is good for most circumstances.
    """
    char_set = char_set or DEFAULT_CHAR_SET
    password = []

    while len(password) < length:
        subset = choice(list(char_set.keys()))  # Get a random subset of characters
                                                # from which to choose
        # Ensure it isn't the same subset as the previous character in the password.
        if password and password[-1] in char_set[subset]:
            continue
        else:
            password.append(choice(char_set[subset]))

    return ''.join(password)
