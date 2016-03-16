#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             interactive_test.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/26/2016
#

"""
ext_pylib.terminal.interactive_test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is just an interactive test for the ansi and colors modules.
"""

from __future__ import absolute_import, print_function

from timeit import timeit

from ext_pylib.terminal import ansi, colors
from ext_pylib.input import prompt

def print_all_colors():  # pylint: disable=too-many-statements
    """Prints all text effects, basic colors, and background colors with a
    string of the function name."""
    print('\n\t----------------------------')
    print('\tPrinting All Color Functions')
    print('\t----------------------------')

    print('\tnormal: \t\t' + colors.normal('normal'))
    print('\tunderline: \t\t' + colors.underline('underline'))
    print('\tbold: \t\t\t' + colors.bold('bold'))
    print('\tblink: \t\t\t' + colors.blink('blink'))
    print('\trblink: \t\t' + colors.rblink('rblink'))
    print('\treverse: \t\t' + colors.reverse('reverse'))
    print('\tconceal: \t\t' + colors.conceal('conceal'))
    print('\tblack: \t\t' + colors.black('black'))
    print('\tred: \t\t\t' + colors.red('red'))
    print('\tgreen: \t\t\t' + colors.green('green'))
    print('\tyellow: \t\t' + colors.yellow('yellow'))
    print('\tblue: \t\t\t' + colors.blue('blue'))
    print('\tmagenta: \t\t' + colors.magenta('magenta'))
    print('\tcyan: \t\t\t' + colors.cyan('cyan'))
    print('\twhite: \t\t\t' + colors.white('white'))
    print('\ton_black: \t\t' + colors.on_black('on_black'))
    print('\ton_red: \t\t' + colors.on_red('on_red'))
    print('\ton_green: \t\t' + colors.on_green('on_green'))
    print('\ton_yellow: \t\t' + colors.on_yellow('on_yellow'))
    print('\ton_blue: \t\t' + colors.on_blue('on_blue'))
    print('\ton_magenta: \t\t' + colors.on_magenta('on_magenta'))
    print('\ton_cyan: \t\t' + colors.on_cyan('on_cyan'))
    print('\ton_white: \t\t' + colors.on_white('on_white'))
    print('\tred_on_black: \t\t' + colors.red_on_black('red_on_black'))
    print('\tgreen_on_black: \t' + colors.green_on_black('green_on_black'))
    print('\tyellow_on_black: \t' + colors.yellow_on_black('yellow_on_black'))
    print('\tblue_on_black: \t\t' + colors.blue_on_black('blue_on_black'))
    print('\tmagenta_on_black: \t' + colors.magenta_on_black('magenta_on_black'))
    print('\tcyan_on_black: \t\t' + colors.cyan_on_black('cyan_on_black'))
    print('\twhite_on_black: \t' + colors.white_on_black('white_on_black'))
    print('\tblack_on_red: \t\t' + colors.black_on_red('black_on_red'))
    print('\tgreen_on_red: \t\t' + colors.green_on_red('green_on_red'))
    print('\tyellow_on_red: \t\t' + colors.yellow_on_red('yellow_on_red'))
    print('\tblue_on_red: \t\t' + colors.blue_on_red('blue_on_red'))
    print('\tmagenta_on_red: \t' + colors.magenta_on_red('magenta_on_red'))
    print('\tcyan_on_red: \t\t' + colors.cyan_on_red('cyan_on_red'))
    print('\twhite_on_red: \t\t' + colors.white_on_red('white_on_red'))
    print('\tblack_on_green: \t' + colors.black_on_green('black_on_green'))
    print('\tred_on_green: \t\t' + colors.red_on_green('red_on_green'))
    print('\tyellow_on_green: \t' + colors.yellow_on_green('yellow_on_green'))
    print('\tblue_on_green: \t\t' + colors.blue_on_green('blue_on_green'))
    print('\tmagenta_on_green: \t' + colors.magenta_on_green('magenta_on_green'))
    print('\tcyan_on_green: \t\t' + colors.cyan_on_green('cyan_on_green'))
    print('\twhite_on_green: \t' + colors.white_on_green('white_on_green'))
    print('\tblack_on_yellow: \t' + colors.black_on_yellow('black_on_yellow'))
    print('\tred_on_yellow: \t\t' + colors.red_on_yellow('red_on_yellow'))
    print('\tgreen_on_yellow: \t' + colors.green_on_yellow('green_on_yellow'))
    print('\tblue_on_yellow: \t' + colors.blue_on_yellow('blue_on_yellow'))
    print('\tmagenta_on_yellow: \t' + colors.magenta_on_yellow('magenta_on_yellow'))
    print('\tcyan_on_yellow: \t' + colors.cyan_on_yellow('cyan_on_yellow'))
    print('\twhite_on_yellow: \t' + colors.white_on_yellow('white_on_yellow'))
    print('\tblack_on_blue: \t\t' + colors.black_on_blue('black_on_blue'))
    print('\tred_on_blue: \t\t' + colors.red_on_blue('red_on_blue'))
    print('\tgreen_on_blue: \t\t' + colors.green_on_blue('green_on_blue'))
    print('\tyellow_on_blue: \t' + colors.yellow_on_blue('yellow_on_blue'))
    print('\tmagenta_on_blue: \t' + colors.magenta_on_blue('magenta_on_blue'))
    print('\tcyan_on_blue: \t\t' + colors.cyan_on_blue('cyan_on_blue'))
    print('\twhite_on_blue: \t\t' + colors.white_on_blue('white_on_blue'))
    print('\tblack_on_magenta: \t' + colors.black_on_magenta('black_on_magenta'))
    print('\tred_on_magenta: \t' + colors.red_on_magenta('red_on_magenta'))
    print('\tgreen_on_magenta: \t' + colors.green_on_magenta('green_on_magenta'))
    print('\tyellow_on_magenta: \t' + colors.yellow_on_magenta('yellow_on_magenta'))
    print('\tblue_on_magenta: \t' + colors.blue_on_magenta('blue_on_magenta'))
    print('\tcyan_on_magenta: \t' + colors.cyan_on_magenta('cyan_on_magenta'))
    print('\twhite_on_magenta: \t' + colors.white_on_magenta('white_on_magenta'))
    print('\tblack_on_cyan: \t\t' + colors.black_on_cyan('black_on_cyan'))
    print('\tred_on_cyan: \t\t' + colors.red_on_cyan('red_on_cyan'))
    print('\tgreen_on_cyan: \t\t' + colors.green_on_cyan('green_on_cyan'))
    print('\tyellow_on_cyan: \t' + colors.yellow_on_cyan('yellow_on_cyan'))
    print('\tblue_on_cyan: \t\t' + colors.blue_on_cyan('blue_on_cyan'))
    print('\tmagenta_on_cyan: \t' + colors.magenta_on_cyan('magenta_on_cyan'))
    print('\twhite_on_cyan: \t\t' + colors.white_on_cyan('white_on_cyan'))
    print('\tblack_on_white: \t' + colors.black_on_white('black_on_white'))
    print('\tred_on_white: \t\t' + colors.red_on_white('red_on_white'))
    print('\tgreen_on_white: \t' + colors.green_on_white('green_on_white'))
    print('\tyellow_on_white: \t' + colors.yellow_on_white('yellow_on_white'))
    print('\tblue_on_white: \t\t' + colors.blue_on_white('blue_on_white'))
    print('\tmagenta_on_white: \t' + colors.magenta_on_white('magenta_on_white'))
    print('\tcyan_on_white: \t\t' + colors.cyan_on_white('cyan_on_white'))

def print_assorted_combinations():
    """Prints an assorted combination of selected color functions."""
    print('ext_pylib interactive terminal test')
    ansi.cursor_down(2)

    print('Testing colors...')
    print('Row 1:  | Row 2:   | ')
    print(colors.black_on_red('black'))
    print(colors.red('red'))
    print(colors.green('green'))
    print(colors.yellow('yellow'))
    print(colors.blue('blue'))
    print(colors.magenta('magenta'))
    print(colors.cyan('cyan'))
    print(colors.white('white'))

    ansi.cursor_up(8)
    ansi.cursor_right(10)

    print(colors.black_on_white('black'))
    ansi.cursor_right(10)
    print(colors.red_on_black('red'))
    ansi.cursor_right(10)
    print(colors.green_on_red('green'))
    ansi.cursor_right(10)
    print(colors.yellow_on_green('yellow'))
    ansi.cursor_right(10)
    print(colors.blue_on_yellow('blue'))
    ansi.cursor_right(10)
    print(colors.magenta_on_blue('magenta'))
    ansi.cursor_right(10)
    print(colors.cyan_on_magenta('cyan'))
    ansi.cursor_right(10)
    print(colors.white_on_cyan('white'))

    print('\n')
    print(colors.underline(colors.red('This is red text that is underlined')))
    print(colors.bold(colors.green('This is green text that is bold')))
    print(colors.reverse(colors.green_on_blue('This is green on blue text that is reversed')))

def main():
    """The main test suite."""
    ansi.reset()

    print(timeit(print_all_colors, number=1))

    if not prompt("Continue?"):
        return False

    ansi.reset()

    print(timeit(print_assorted_combinations, number=1))

    if not prompt("Continue?"):
        return False


if __name__ == '__main__':
    main()
