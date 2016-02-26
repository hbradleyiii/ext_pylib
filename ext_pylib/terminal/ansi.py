#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             ansi.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/23/2016
#

"""
ext_pylib.terminal.ansi
~~~~~~~~~~~~~~~~~~~~~~~

Ansi escape codes.
"""


CSI = '\033['
OSC = '\033]'
BEL = '\007'

CUU = CSI + '{0}A'  # Cursor up
CUD = CSI + '{0}B'  # Cursor down
CUF = CSI + '{0}C'  # Cursor down
CUB = CSI + '{0}D'  # Cursor down
CNL = CSI + '{0}E'  # Cursor down
CPL = CSI + '{0}F'  # Cursor down
CHA = CSI + '{0}G'  # Cursor Horizontal Absolute
CUP = CSI + '{0};{1}H'  # Cursor Horizontal Absolute

ED = CSI + '{0}J'  # Erase part of the screen

SCP = CSI + 's'  # Save Cursor Position
RCP = CSI + 'u'  # Restore Cursor Position

SGR = CSI + '{0}m'
SGR_RESET = CSI + '0m'
SGR_SEP = ';'  # SGR separator (delimiter)

ATT_RESET = '0'
BOLD = '1'
UNDERLINE = '4'
BLINK = '5'
REVERSE = '7'
CONCEAL = '8'

BLACK = '30'
RED = '31'
GREEN = '32'
YELLOW = '33'
BLUE = '34'
MAGENTA = '35'
CYAN = '36'
WHITE = '37'

BG_BLACK = '40'
BG_RED = '41'
BG_GREEN = '42'
BG_YELLOW = '43'
BG_BLUE = '44'
BG_MAGENTA = '45'
BG_CYAN = '46'
BG_WHITE = '47'
