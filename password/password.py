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
        character = urandom(1)
        subset = choice(char_set.keys())  # Get a random subset of characters
                                          # from which to choose
        # Make sure character is in subset
        if character in char_set[subset]:
            # Make sure it isn't the same subset as the previous character
            if password and password[-1] in char_set[subset]:
                continue  # Try again
            else:
                password.append(character)

    return ''.join(password)
