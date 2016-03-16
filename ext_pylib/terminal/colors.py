#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             colors.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/23/2016
#
# pylint:           disable=unused-argument

"""
ext_pylib.terminal.colors
~~~~~~~~~~~~~~~~~~~~~~~~~

Functions for text effects and colors using ANSI escape sequences.
They return strings wrapped with the codes.
"""

from __future__ import absolute_import

from . import ansi


def sgr_wrapper(string, *args):
    """Takes a string and wraps an ANSI SGR escape sequence around it.

    If a reset is found in the middle of the string, the attribute is set again
    immediately following the reset. The entire string is concluded with the
    reset. This allows for unlimited nesting. (Without this, the first reset
    would clear the sequence for the entire rest of the string.)

    :param string: the string around which to wrap the ANSI SGR escape sequence.
    :param *args: one or more escape args with which to put in one escape
        sequence.

    Usage::

        >>> print bg_white(black('This section of text is ' + red(bold('important')) + '.'))
        This section of text is important.

    """
    escape = ansi.sgr(*args)
    reset = ansi.sgr(ansi.RESET)
    _string = ''
    for _segment in string.split(reset):
        _string = _string + escape + _segment + reset
    return _string

def sgr_combiner(string, attribute, *funcs, **additional):
    """Combines multiple sgr attributes into one string using sgr_wrapper.

    This is called by individual attribute functions and allows either chaining
    multiple functions or passing attribute functions as arguments of other
    attribute functions.

    :param string: the string around which to wrap the SGR codes.
    :param attribute: the ansi attribute to be used and combined with optional
        additional attributes.
    :param *funcs: optional attribute functions to be applied.
    :param **additional: additional attributes to be combined with attribute.
        This parameter is intended for internal use for recursion.
        In **additional is additional['attributes'] which is a tuple of
        attributes to be ultimately combined with sgr_wrapper.

    Usage::

        >>> print(bold('The important string.' red, on_white))
        The important string.

        >>> print(bold(red(on_white('The important string.'))))
        The important string.

    Note that this allows for nonsensical combinations. There is no error
    checking, but a string cannot be both red and green, nor can it blink while
    being underlined. The last escape code is the one that applies. It is up to
    the user to make sure the attributes can be combined.
    """
    _attributes = additional['attributes'] + (attribute,) \
            if 'attributes' in additional else (attribute,)
    if funcs:
        _additional = {'attributes' : _attributes}
        _next_func, _funcs = funcs[0], funcs[1:]
        return _next_func(string, *_funcs, **_additional)
    else:
        return sgr_wrapper(string, *_attributes)


# Text effects

def normal(string, *funcs, **additional):
    """Text effect - normal. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RESET, *funcs, **additional)

def underline(string, *funcs, **additional):
    """Text effect - underline. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.UNDERLINE, *funcs, **additional)

def bold(string, *funcs, **additional):
    """Text effect - bold. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BOLD, *funcs, **additional)

def blink(string, *funcs, **additional):
    """Text effect - blink. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLINK, *funcs, **additional)

def rblink(string, *funcs, **additional):
    """Text effect - rblink. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RBLINK, *funcs, **additional)

def reverse(string, *funcs, **additional):
    """Text effect - reverse. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.REVERSE, *funcs, **additional)

def conceal(string, *funcs, **additional):
    """Text effect - conceal. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.CONCEAL, *funcs, **additional)


# Basic colors

def black(string, *funcs, **additional):
    """Text color - black. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLACK, *funcs, **additional)

def red(string, *funcs, **additional):
    """Text color - red. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RED, *funcs, **additional)

def green(string, *funcs, **additional):
    """Text color - green. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.GREEN, *funcs, **additional)

def yellow(string, *funcs, **additional):
    """Text color - yellow. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.YELLOW, *funcs, **additional)

def blue(string, *funcs, **additional):
    """Text color - blue. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLUE, *funcs, **additional)

def magenta(string, *funcs, **additional):
    """Text color - magenta. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.MAGENTA, *funcs, **additional)

def cyan(string, *funcs, **additional):
    """Text color - cyan. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.CYAN, *funcs, **additional)

def white(string, *funcs, **additional):
    """Text color - white. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.WHITE, *funcs, **additional)


# Basic background colors

def on_black(string, *funcs, **additional):
    """Text background color - black. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BG_BLACK, *funcs, **additional)

def on_red(string, *funcs, **additional):
    """Text background color - red. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BG_RED, *funcs, **additional)

def on_green(string, *funcs, **additional):
    """Text background color - green. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BG_GREEN, *funcs, **additional)

def on_yellow(string, *funcs, **additional):
    """Text background color - yellow. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BG_YELLOW, *funcs, **additional)

def on_blue(string, *funcs, **additional):
    """Text background color - blue. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BG_BLUE, *funcs, **additional)

def on_magenta(string, *funcs, **additional):
    """Text background color - magenta. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BG_MAGENTA, *funcs, **additional)

def on_cyan(string, *funcs, **additional):
    """Text background color - cyan. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BG_CYAN, *funcs, **additional)

def on_white(string, *funcs, **additional):
    """Text background color - white. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BG_WHITE, *funcs, **additional)


# Colors on a black background
def red_on_black(string, *funcs, **additional):
    """Text color - red on background color - black. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RED, *funcs, attributes=(ansi.BG_BLACK,))

def green_on_black(string, *funcs, **additional):
    """Text color - green on background color - black. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.GREEN, *funcs, attributes=(ansi.BG_BLACK,))

def yellow_on_black(string, *funcs, **additional):
    """Text color - yellow on background color - black. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.YELLOW, *funcs, attributes=(ansi.BG_BLACK,))

def blue_on_black(string, *funcs, **additional):
    """Text color - blue on background color - black. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLUE, *funcs, attributes=(ansi.BG_BLACK,))

def magenta_on_black(string, *funcs, **additional):
    """Text color - magenta on background color - black. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.MAGENTA, *funcs, attributes=(ansi.BG_BLACK,))

def cyan_on_black(string, *funcs, **additional):
    """Text color - cyan on background color - black. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.CYAN, *funcs, attributes=(ansi.BG_BLACK,))

def white_on_black(string, *funcs, **additional):
    """Text color - white on background color - black. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.WHITE, *funcs, attributes=(ansi.BG_BLACK,))


# Colors on a red background

def black_on_red(string, *funcs, **additional):
    """Text color - black on background color - red. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLACK, *funcs, attributes=(ansi.BG_RED,))

def green_on_red(string, *funcs, **additional):
    """Text color - green on background color - red. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.GREEN, *funcs, attributes=(ansi.BG_RED,))

def yellow_on_red(string, *funcs, **additional):
    """Text color - yellow on background color - red. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.YELLOW, *funcs, attributes=(ansi.BG_RED,))

def blue_on_red(string, *funcs, **additional):
    """Text color - blue on background color - red. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLUE, *funcs, attributes=(ansi.BG_RED,))

def magenta_on_red(string, *funcs, **additional):
    """Text color - magenta on background color - red. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.MAGENTA, *funcs, attributes=(ansi.BG_RED,))

def cyan_on_red(string, *funcs, **additional):
    """Text color - cyan on background color - red. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.CYAN, *funcs, attributes=(ansi.BG_RED,))

def white_on_red(string, *funcs, **additional):
    """Text color - white on background color - red. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.WHITE, *funcs, attributes=(ansi.BG_RED,))


# Colors on a green background

def black_on_green(string, *funcs, **additional):
    """Text color - black on background color - green. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLACK, *funcs, attributes=(ansi.BG_GREEN,))

def red_on_green(string, *funcs, **additional):
    """Text color - red on background color - green. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RED, *funcs, attributes=(ansi.BG_GREEN,))

def yellow_on_green(string, *funcs, **additional):
    """Text color - yellow on background color - green. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.YELLOW, *funcs, attributes=(ansi.BG_GREEN,))

def blue_on_green(string, *funcs, **additional):
    """Text color - blue on background color - green. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLUE, *funcs, attributes=(ansi.BG_GREEN,))

def magenta_on_green(string, *funcs, **additional):
    """Text color - magenta on background color - green. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.MAGENTA, *funcs, attributes=(ansi.BG_GREEN,))

def cyan_on_green(string, *funcs, **additional):
    """Text color - cyan on background color - green. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.CYAN, *funcs, attributes=(ansi.BG_GREEN,))

def white_on_green(string, *funcs, **additional):
    """Text color - white on background color - green. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.WHITE, *funcs, attributes=(ansi.BG_GREEN,))


# Colors on a yellow background

def black_on_yellow(string, *func, **additional):
    """Text color - black on background color - yellow. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLACK, *func, attributes=(ansi.BG_YELLOW,))

def red_on_yellow(string, *funcs, **additional):
    """Text color - red on background color - yellow. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RED, *funcs, attributes=(ansi.BG_YELLOW,))

def green_on_yellow(string, *funcs, **additional):
    """Text color - green on background color - yellow. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.GREEN, *funcs, attributes=(ansi.BG_YELLOW,))

def blue_on_yellow(string, *funcs, **additional):
    """Text color - blue on background color - yellow. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLUE, *funcs, attributes=(ansi.BG_YELLOW,))

def magenta_on_yellow(string, *funcs, **additional):
    """Text color - magenta on background color - yellow. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.MAGENTA, *funcs, attributes=(ansi.BG_YELLOW,))

def cyan_on_yellow(string, *funcs, **additional):
    """Text color - cyan on background color - yellow. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.CYAN, *funcs, attributes=(ansi.BG_YELLOW,))

def white_on_yellow(string, *funcs, **additional):
    """Text color - white on background color - yellow. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.WHITE, *funcs, attributes=(ansi.BG_YELLOW,))


# Colors on a blue background

def black_on_blue(string, *funcs, **additional):
    """Text color - black on background color - blue. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLACK, *funcs, attributes=(ansi.BG_BLUE,))

def red_on_blue(string, *funcs, **additional):
    """Text color - red on background color - blue. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RED, *funcs, attributes=(ansi.BG_BLUE,))

def green_on_blue(string, *funcs, **additional):
    """Text color - green on background color - blue. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.GREEN, *funcs, attributes=(ansi.BG_BLUE,))

def yellow_on_blue(string, *funcs, **additional):
    """Text color - yellow on background color - blue. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.YELLOW, *funcs, attributes=(ansi.BG_BLUE,))

def magenta_on_blue(string, *funcs, **additional):
    """Text color - magenta on background color - blue. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.MAGENTA, *funcs, attributes=(ansi.BG_BLUE,))

def cyan_on_blue(string, *funcs, **additional):
    """Text color - cyan on background color - blue. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.CYAN, *funcs, attributes=(ansi.BG_BLUE,))

def white_on_blue(string, *funcs, **additional):
    """Text color - white on background color - blue. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.WHITE, *funcs, attributes=(ansi.BG_BLUE,))


# Colors on a magenta background

def black_on_magenta(string, *funcs, **additional):
    """Text color - black on background color - magenta. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLACK, *funcs, attributes=(ansi.BG_MAGENTA,))

def red_on_magenta(string, *funcs, **additional):
    """Text color - red on background color - magenta. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RED, *funcs, attributes=(ansi.BG_MAGENTA,))

def green_on_magenta(string, *funcs, **additional):
    """Text color - green on background color - magenta. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.GREEN, *funcs, attributes=(ansi.BG_MAGENTA,))

def yellow_on_magenta(string, *funcs, **additional):
    """Text color - yellow on background color - magenta. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.YELLOW, *funcs, attributes=(ansi.BG_MAGENTA,))

def blue_on_magenta(string, *funcs, **additional):
    """Text color - blue on background color - magenta. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLUE, *funcs, attributes=(ansi.BG_MAGENTA,))

def cyan_on_magenta(string, *funcs, **additional):
    """Text color - cyan on background color - magenta. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.CYAN, *funcs, attributes=(ansi.BG_MAGENTA,))

def white_on_magenta(string, *funcs, **additional):
    """Text color - white on background color - magenta. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.WHITE, *funcs, attributes=(ansi.BG_MAGENTA,))


# Colors on a cyan background

def black_on_cyan(string, *funcs, **additional):
    """Text color - black on background color - cyan. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLACK, *funcs, attributes=(ansi.BG_CYAN,))

def red_on_cyan(string, *funcs, **additional):
    """Text color - red on background color - cyan. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RED, *funcs, attributes=(ansi.BG_CYAN,))

def green_on_cyan(string, *funcs, **additional):
    """Text color - green on background color - cyan. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.GREEN, *funcs, attributes=(ansi.BG_CYAN,))

def yellow_on_cyan(string, *funcs, **additional):
    """Text color - yellow on background color - cyan. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.YELLOW, *funcs, attributes=(ansi.BG_CYAN,))

def blue_on_cyan(string, *funcs, **additional):
    """Text color - blue on background color - cyan. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLUE, *funcs, attributes=(ansi.BG_CYAN,))

def magenta_on_cyan(string, *funcs, **additional):
    """Text color - magenta on background color - cyan. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.MAGENTA, *funcs, attributes=(ansi.BG_CYAN,))

def white_on_cyan(string, *funcs, **additional):
    """Text color - white on background color - cyan. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.WHITE, *funcs, attributes=(ansi.BG_CYAN,))


# Colors on a white background

def black_on_white(string, *funcs, **additional):
    """Text color - black on background color - white. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLACK, *funcs, attributes=(ansi.BG_WHITE,))

def red_on_white(string, *funcs, **additional):
    """Text color - red on background color - white. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.RED, *funcs, attributes=(ansi.BG_WHITE,))

def green_on_white(string, *funcs, **additional):
    """Text color - green on background color - white. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.GREEN, *funcs, attributes=(ansi.BG_WHITE,))

def yellow_on_white(string, *funcs, **additional):
    """Text color - yellow on background color - white. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.YELLOW, *funcs, attributes=(ansi.BG_WHITE,))

def blue_on_white(string, *funcs, **additional):
    """Text color - blue on background color - white. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.BLUE, *funcs, attributes=(ansi.BG_WHITE,))

def magenta_on_white(string, *funcs, **additional):
    """Text color - magenta on background color - white. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.MAGENTA, *funcs, attributes=(ansi.BG_WHITE,))

def cyan_on_white(string, *funcs, **additional):
    """Text color - cyan on background color - white. (see sgr_combiner())."""
    return sgr_combiner(string, ansi.CYAN, *funcs, attributes=(ansi.BG_WHITE,))
