#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             prompt.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/03/2015
#
# description:      Functions for displaying and handling prompts on the
#                   terminal.
#

from __future__ import print_function, unicode_literals


def prompt(prompt_text, default = True):
    """Displays a yes/no prompt and returns the response as bool."""
    default_text = " [y] " if default else " [n] "
    while True:
        response = raw_input('[?] ' + prompt_text + default_text).lower()
        responses = {
                ''    : default,
                'y'   : True,
                'yes' : True,
                'n'   : False,
                'no'  : False,
                }
        if response in responses:
            return responses[response]
        else:
            print('Response not understood.')

def prompt_str(prompt_text, default_str=''):
    """Prompts for a string, returns the result."""
    add_text = " "
    if not default_str == '':
        add_text = " [" + default_str + "] "

    response = raw_input('[?] ' + prompt_text + add_text)
    if response == '':
        response = default_str
    return response

def warn_prompt(prompt_text, required_response):
    """Warning prompt that prompts for a specific text (required_response).
    This is useful for potentially dangerous actions."""
    while True:
        response = raw_input("[!!] " + prompt_text + " [type n or '" + required_response + "'] ")
        if response == required_response:
            return True
        elif response.lower() in ['n', 'no']:
            return False
        else:
            print('Response not understood. Please type "n" or "required_response"')
