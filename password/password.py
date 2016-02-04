#!/usr/bin/env python
#
# name:             password.py
# adapted from:     http://code.activestate.com/recipes/578169-extremely-strong-password-generator/
# maintainer:       Harold Bradley III
# email:            harold@bradleystudio.net
#
# description:      A script that generates an arbitrary length string of
#                   random characters to be used as a password.
#

from random import choice
from os import urandom

# Defines the default characters for use in generating a password
DEFAULT_CHAR_SET = {
    'small': 'abcdefghijklmnopqrstuvwxyz',
    'nums': '0123456789',
    'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'special': '^!$%&=?{[]}+~#-_.:,;<>|'
}

def generate_pw(length=18, char_set=DEFAULT_CHAR_SET):
    """Generates a pseudo-randomly generated password and returns it as a string."""
    password = []

    while len(password) < length:
        key = choice(char_set.keys())
        a_char = urandom(1)
        if a_char in char_set[key]:
            if is_like_previous_char(password, char_set[key]):
                continue
            else:
                password.append(a_char)
    return ''.join(password)

def is_like_previous_char(password, current_char_set):
    """Function to ensure that there are no consecutive
    UPPERCASE/lowercase/numbers/special-characters."""

    num_of_chars = len(password)
    if num_of_chars == 0:
        return False
    else:
        prev_char = password[num_of_chars - 1]
        if prev_char in current_char_set:
            return True
        else:
            return False
