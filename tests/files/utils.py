#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_section.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/10/2016

"""
Mock functions and classes for testing.
"""

def mock_read(string):
    """Monkey patch read function."""
    def read(_=None):
        """Mock read function."""
        return string
    return read

def mock_read_data(self):
    """Monkey patch read function."""
    return self.data

def mock_readlines(self):
    """Monkey patch readlines function."""
    return self.read().split('\n')
