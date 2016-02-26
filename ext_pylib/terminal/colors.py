#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             colors.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/23/2016

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
    would clear the unset the sequence for the rest of the string.)

    For example:

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
    """
    asdf

    For example:

        >>> print bold('The important string.' red, on_white)

    Note that this allows for nonsensical combinations. A string cannot be
    both red and green, nor can it blink while being underlined. It is up to
    the user to make sure the attributes can be combined.
    """
    _attributes = additional['attributes'] + (attribute,) if 'attributes' in additional else (attribute,)
    if funcs:
        _additional = { 'attributes' : _attributes }
        _next_func, _funcs = funcs[0], funcs[1:]
        return _next_func(string, *_funcs, **_additional)
    else:
        return sgr_wrapper(string, *_attributes)


# Text effects

def normal(string, *funcs, **additional):
    return sgr_combiner(string, ansi.NORMAL, *funcs, **additional)

def underline(string, *funcs, **additional):
    return sgr_combiner(string, ansi.UNDERLINE, *funcs, **additional)

def bold(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BOLD, *funcs, **additional)

def blink(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BLINK, *funcs, **additional)

def rblink(string, *funcs, **additional):
    return sgr_combiner(string, ansi.RBLINK, *funcs, **additional)

def reverse(string, *funcs, **additional):
    return sgr_combiner(string, ansi.REVERSE, *funcs, **additional)

def conceal(string, *funcs, **additional):
    return sgr_combiner(string, ansi.CONCEAL, *funcs, **additional)


# Basic colors

def black(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BLACK, *funcs, **additional)

def red(string, *funcs, **additional):
    return sgr_combiner(string, ansi.RED, *funcs, **additional)

def green(string, *funcs, **additional):
    return sgr_combiner(string, ansi.GREEN, *funcs, **additional)

def yellow(string, *funcs, **additional):
    return sgr_combiner(string, ansi.YELLOW, *funcs, **additional)

def blue(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BLUE, *funcs, **additional)

def magenta(string, *funcs, **additional):
    return sgr_combiner(string, ansi.MAGENTA, *funcs, **additional)

def cyan(string, *funcs, **additional):
    return sgr_combiner(string, ansi.CYAN, *funcs, **additional)

def white(string, *funcs, **additional):
    return sgr_combiner(string, ansi.WHITE, *funcs, **additional)


# Basic background colors

def on_black(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BG_BLACK, *funcs, **additional)

def on_red(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BG_RED, *funcs, **additional)

def on_green(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BG_GREEN, *funcs, **additional)

def on_yellow(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BG_YELLOW, *funcs, **additional)

def on_blue(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BG_BLUE, *funcs, **additional)

def on_magenta(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BG_MAGENTA, *funcs, **additional)

def on_cyan(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BG_CYAN, *funcs, **additional)

def on_white(string, *funcs, **additional):
    return sgr_combiner(string, ansi.BG_WHITE, *funcs, **additional)


# Colors on a black background

def red_on_black(string):
    return sgr_wrapper(string, ansi.RED, ansi.BG_BLACK)

def green_on_black(string):
    return sgr_wrapper(string, ansi.GREEN, ansi.BG_BLACK)

def yellow_on_black(string):
    return sgr_wrapper(string, ansi.YELLOW, ansi.BG_BLACK)

def blue_on_black(string):
    return sgr_wrapper(string, ansi.BLUE, ansi.BG_BLACK)

def magenta_on_black(string):
    return sgr_wrapper(string, ansi.MAGENTA, ansi.BG_BLACK)

def cyan_on_black(string):
    return sgr_wrapper(string, ansi.CYAN, ansi.BG_BLACK)

def white_on_black(string):
    return sgr_wrapper(string, ansi.WHITE, ansi.BG_BLACK)


# Colors on a red background

def black_on_red(string):
    return sgr_wrapper(string, ansi.BLACK, ansi.BG_RED)

def green_on_red(string):
    return sgr_wrapper(string, ansi.GREEN, ansi.BG_RED)

def yellow_on_red(string):
    return sgr_wrapper(string, ansi.YELLOW, ansi.BG_RED)

def blue_on_red(string):
    return sgr_wrapper(string, ansi.BLUE, ansi.BG_RED)

def magenta_on_red(string):
    return sgr_wrapper(string, ansi.MAGENTA, ansi.BG_RED)

def cyan_on_red(string):
    return sgr_wrapper(string, ansi.CYAN, ansi.BG_RED)

def white_on_red(string):
    return sgr_wrapper(string, ansi.WHITE, ansi.BG_RED)



# Colors on a green background

def black_on_green(string):
    return sgr_wrapper(string, ansi.BLACK, ansi.BG_GREEN)

def red_on_green(string):
    return sgr_wrapper(string, ansi.RED, ansi.BG_GREEN)

def yellow_on_green(string):
    return sgr_wrapper(string, ansi.YELLOW, ansi.BG_GREEN)

def blue_on_green(string):
    return sgr_wrapper(string, ansi.BLUE, ansi.BG_GREEN)

def magenta_on_green(string):
    return sgr_wrapper(string, ansi.MAGENTA, ansi.BG_GREEN)

def cyan_on_green(string):
    return sgr_wrapper(string, ansi.CYAN, ansi.BG_GREEN)

def white_on_green(string):
    return sgr_wrapper(string, ansi.WHITE, ansi.BG_GREEN)

# Colors on a yellow background

def black_on_yellow(string):
    return sgr_wrapper(string, ansi.BLACK, ansi.BG_YELLOW)

def red_on_yellow(string):
    return sgr_wrapper(string, ansi.RED, ansi.BG_YELLOW)

def green_on_yellow(string):
    return sgr_wrapper(string, ansi.GREEN, ansi.BG_YELLOW)

def blue_on_yellow(string):
    return sgr_wrapper(string, ansi.BLUE, ansi.BG_YELLOW)

def magenta_on_yellow(string):
    return sgr_wrapper(string, ansi.MAGENTA, ansi.BG_YELLOW)

def cyan_on_yellow(string):
    return sgr_wrapper(string, ansi.CYAN, ansi.BG_YELLOW)

def white_on_yellow(string):
    return sgr_wrapper(string, ansi.WHITE, ansi.BG_YELLOW)

# Colors on a blue background

def black_on_blue(string):
    return sgr_wrapper(string, ansi.BLACK, ansi.BG_BLUE)

def red_on_blue(string):
    return sgr_wrapper(string, ansi.RED, ansi.BG_BLUE)

def green_on_blue(string):
    return sgr_wrapper(string, ansi.GREEN, ansi.BG_BLUE)

def yellow_on_blue(string):
    return sgr_wrapper(string, ansi.YELLOW, ansi.BG_BLUE)

def magenta_on_blue(string):
    return sgr_wrapper(string, ansi.MAGENTA, ansi.BG_BLUE)

def cyan_on_blue(string):
    return sgr_wrapper(string, ansi.CYAN, ansi.BG_BLUE)

def white_on_blue(string):
    return sgr_wrapper(string, ansi.WHITE, ansi.BG_BLUE)

# Colors on a magenta background

def black_on_magenta(string):
    return sgr_wrapper(string, ansi.BLACK, ansi.BG_MAGENTA)

def red_on_magenta(string):
    return sgr_wrapper(string, ansi.RED, ansi.BG_MAGENTA)

def green_on_magenta(string):
    return sgr_wrapper(string, ansi.GREEN, ansi.BG_MAGENTA)

def yellow_on_magenta(string):
    return sgr_wrapper(string, ansi.YELLOW, ansi.BG_MAGENTA)

def blue_on_magenta(string):
    return sgr_wrapper(string, ansi.BLUE, ansi.BG_MAGENTA)

def cyan_on_magenta(string):
    return sgr_wrapper(string, ansi.CYAN, ansi.BG_MAGENTA)

def white_on_magenta(string):
    return sgr_wrapper(string, ansi.WHITE, ansi.BG_MAGENTA)

# Colors on a cyan background

def black_on_cyan(string):
    return sgr_wrapper(string, ansi.BLACK, ansi.BG_CYAN)

def red_on_cyan(string):
    return sgr_wrapper(string, ansi.RED, ansi.BG_CYAN)

def green_on_cyan(string):
    return sgr_wrapper(string, ansi.GREEN, ansi.BG_CYAN)

def yellow_on_cyan(string):
    return sgr_wrapper(string, ansi.YELLOW, ansi.BG_CYAN)

def blue_on_cyan(string):
    return sgr_wrapper(string, ansi.BLUE, ansi.BG_CYAN)

def magenta_on_cyan(string):
    return sgr_wrapper(string, ansi.MAGENTA, ansi.BG_CYAN)

def white_on_cyan(string):
    return sgr_wrapper(string, ansi.WHITE, ansi.BG_CYAN)

# Colors on a white background

def black_on_white(string):
    return sgr_wrapper(string, ansi.BLACK, ansi.BG_WHITE)

def red_on_white(string):
    return sgr_wrapper(string, ansi.RED, ansi.BG_WHITE)

def green_on_white(string):
    return sgr_wrapper(string, ansi.GREEN, ansi.BG_WHITE)

def yellow_on_white(string):
    return sgr_wrapper(string, ansi.YELLOW, ansi.BG_WHITE)

def blue_on_white(string):
    return sgr_wrapper(string, ansi.BLUE, ansi.BG_WHITE)

def magenta_on_white(string):
    return sgr_wrapper(string, ansi.MAGENTA, ansi.BG_WHITE)

def cyan_on_white(string):
    return sgr_wrapper(string, ansi.CYAN, ansi.BG_WHITE)
