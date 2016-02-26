#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             colors.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/23/2016

from . import ansi


def colorize(string, color):
    """Takes a string and wraps an ansi color escape sequence around it."""
    colorized = ''
    for segment in string.split(ansi.SGR_RESET):
        colorized = colorized + ansi.SGR.format(color) + segment + ansi.SGR_RESET
    return colorized


# Basic colors

def black(string):
    return colorize(string, ansi.BLACK)

def red(string):
    return colorize(string, ansi.RED)

def green(string):
    return colorize(string, ansi.GREEN)

def yellow(string):
    return colorize(string, ansi.YELLOW)

def blue(string):
    return colorize(string, ansi.BLUE)

def magenta(string):
    return colorize(string, ansi.MAGENTA)

def cyan(string):
    return colorize(string, ansi.CYAN)

def white(string):
    return colorize(string, ansi.WHITE)


# Basic background colors

def on_black(string):
    return colorize(string, ansi.BG_BLACK)

def on_red(string):
    return colorize(string, ansi.BG_RED)

def on_green(string):
    return colorize(string, ansi.BG_GREEN)

def on_yellow(string):
    return colorize(string, ansi.BG_YELLOW)

def on_blue(string):
    return colorize(string, ansi.BG_BLUE)

def on_magenta(string):
    return colorize(string, ansi.BG_MAGENTA)

def on_cyan(string):
    return colorize(string, ansi.BG_CYAN)

def on_white(string):
    return colorize(string, ansi.BG_WHITE)


# Combinations

def combine(color, bg_color):
    return color + ansi.SGR_SEP + bg_color


# Colors on a black background

def red_on_black(string):
    return colorize(string, combine(ansi.RED, ansi.BG_BLACK))

def green_on_black(string):
    return colorize(string, combine(ansi.GREEN, ansi.BG_BLACK))

def yellow_on_black(string):
    return colorize(string, combine(ansi.YELLOW, ansi.BG_BLACK))

def blue_on_black(string):
    return colorize(string, combine(ansi.BLUE, ansi.BG_BLACK))

def magenta_on_black(string):
    return colorize(string, combine(ansi.MAGENTA, ansi.BG_BLACK))

def cyan_on_black(string):
    return colorize(string, combine(ansi.CYAN, ansi.BG_BLACK))

def white_on_black(string):
    return colorize(string, combine(ansi.WHITE, ansi.BG_BLACK))


# Colors on a red background

def black_on_red(string):
    return colorize(string, combine(ansi.BLACK, ansi.BG_RED))

def green_on_red(string):
    return colorize(string, combine(ansi.GREEN, ansi.BG_RED))

def yellow_on_red(string):
    return colorize(string, combine(ansi.YELLOW, ansi.BG_RED))

def blue_on_red(string):
    return colorize(string, combine(ansi.BLUE, ansi.BG_RED))

def magenta_on_red(string):
    return colorize(string, combine(ansi.MAGENTA, ansi.BG_RED))

def cyan_on_red(string):
    return colorize(string, combine(ansi.CYAN, ansi.BG_RED))

def white_on_red(string):
    return colorize(string, combine(ansi.WHITE, ansi.BG_RED))



# Colors on a green background

def black_on_green(string):
    return colorize(string, combine(ansi.BLACK, ansi.BG_GREEN))

def red_on_green(string):
    return colorize(string, combine(ansi.RED, ansi.BG_GREEN))

def yellow_on_green(string):
    return colorize(string, combine(ansi.YELLOW, ansi.BG_GREEN))

def blue_on_green(string):
    return colorize(string, combine(ansi.BLUE, ansi.BG_GREEN))

def magenta_on_green(string):
    return colorize(string, combine(ansi.MAGENTA, ansi.BG_GREEN))

def cyan_on_green(string):
    return colorize(string, combine(ansi.CYAN, ansi.BG_GREEN))

def white_on_green(string):
    return colorize(string, combine(ansi.WHITE, ansi.BG_GREEN))

# Colors on a yellow background

def black_on_yellow(string):
    return colorize(string, combine(ansi.BLACK, ansi.BG_YELLOW))

def red_on_yellow(string):
    return colorize(string, combine(ansi.RED, ansi.BG_YELLOW))

def green_on_yellow(string):
    return colorize(string, combine(ansi.GREEN, ansi.BG_YELLOW))

def blue_on_yellow(string):
    return colorize(string, combine(ansi.BLUE, ansi.BG_YELLOW))

def magenta_on_yellow(string):
    return colorize(string, combine(ansi.MAGENTA, ansi.BG_YELLOW))

def cyan_on_yellow(string):
    return colorize(string, combine(ansi.CYAN, ansi.BG_YELLOW))

def white_on_yellow(string):
    return colorize(string, combine(ansi.WHITE, ansi.BG_YELLOW))

# Colors on a blue background

def black_on_blue(string):
    return colorize(string, combine(ansi.BLACK, ansi.BG_BLUE))

def red_on_blue(string):
    return colorize(string, combine(ansi.RED, ansi.BG_BLUE))

def green_on_blue(string):
    return colorize(string, combine(ansi.GREEN, ansi.BG_BLUE))

def yellow_on_blue(string):
    return colorize(string, combine(ansi.YELLOW, ansi.BG_BLUE))

def magenta_on_blue(string):
    return colorize(string, combine(ansi.MAGENTA, ansi.BG_BLUE))

def cyan_on_blue(string):
    return colorize(string, combine(ansi.CYAN, ansi.BG_BLUE))

def white_on_blue(string):
    return colorize(string, combine(ansi.WHITE, ansi.BG_BLUE))

# Colors on a magenta background

def black_on_magenta(string):
    return colorize(string, combine(ansi.BLACK, ansi.BG_MAGENTA))

def red_on_magenta(string):
    return colorize(string, combine(ansi.RED, ansi.BG_MAGENTA))

def green_on_magenta(string):
    return colorize(string, combine(ansi.GREEN, ansi.BG_MAGENTA))

def yellow_on_magenta(string):
    return colorize(string, combine(ansi.YELLOW, ansi.BG_MAGENTA))

def blue_on_magenta(string):
    return colorize(string, combine(ansi.BLUE, ansi.BG_MAGENTA))

def cyan_on_magenta(string):
    return colorize(string, combine(ansi.CYAN, ansi.BG_MAGENTA))

def white_on_magenta(string):
    return colorize(string, combine(ansi.WHITE, ansi.BG_MAGENTA))

# Colors on a cyan background

def black_on_cyan(string):
    return colorize(string, combine(ansi.BLACK, ansi.BG_CYAN))

def red_on_cyan(string):
    return colorize(string, combine(ansi.RED, ansi.BG_CYAN))

def green_on_cyan(string):
    return colorize(string, combine(ansi.GREEN, ansi.BG_CYAN))

def yellow_on_cyan(string):
    return colorize(string, combine(ansi.YELLOW, ansi.BG_CYAN))

def blue_on_cyan(string):
    return colorize(string, combine(ansi.BLUE, ansi.BG_CYAN))

def magenta_on_cyan(string):
    return colorize(string, combine(ansi.MAGENTA, ansi.BG_CYAN))

def white_on_cyan(string):
    return colorize(string, combine(ansi.WHITE, ansi.BG_CYAN))

# Colors on a white background

def black_on_white(string):
    return colorize(string, combine(ansi.BLACK, ansi.BG_WHITE))

def red_on_white(string):
    return colorize(string, combine(ansi.RED, ansi.BG_WHITE))

def green_on_white(string):
    return colorize(string, combine(ansi.GREEN, ansi.BG_WHITE))

def yellow_on_white(string):
    return colorize(string, combine(ansi.YELLOW, ansi.BG_WHITE))

def blue_on_white(string):
    return colorize(string, combine(ansi.BLUE, ansi.BG_WHITE))

def magenta_on_white(string):
    return colorize(string, combine(ansi.MAGENTA, ansi.BG_WHITE))

def cyan_on_white(string):
    return colorize(string, combine(ansi.CYAN, ansi.BG_WHITE))
