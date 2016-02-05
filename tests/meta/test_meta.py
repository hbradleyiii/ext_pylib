#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_meta.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/29/2016
#
# description:      A unit test for ext_pylib's meta classes and functions.
#

from ext_pylib.meta import DynamicProperty, setdynattr
from mock import patch
import pytest


class DummyClass(object):
    """Just a dummy class."""

def addfive_getter(self):
    """A test getter function that just returns _value."""
    return getattr(self, '_value', None)

def addfive_setter(self, value):
    """A test setter function that adds 5 to the value passed before storing as _value."""
    self._value = value + 5  # Add 5 for testing

def test_dynamicproperty():
    """Tests DynamicProperty."""
    dummy = DummyClass()

    # Make sure property doesn't already exist
    assert not getattr(dummy, 'addfive', None)

    # Create it (It MUST be on the class, not the object(instance) )
    dummy.__class__.addfive = DynamicProperty(addfive_getter)
    dummy.__class__.addfive = dummy.__class__.addfive.create_setter(addfive_setter)

    assert not dummy.addfive
    dummy.addfive = 5
    assert dummy.addfive == 10

def test_setdynattr():
    """Tests setdynattr function."""
    dummy = DummyClass()

    assert not getattr(dummy, 'a_property', None)
    assert not getattr(dummy, 'addfive', None)

    setdynattr(dummy, 'a_property')
    assert not dummy.a_property
    dummy.a_property = 5
    assert dummy.a_property == 5

    setdynattr(dummy, 'addfive', addfive_getter, addfive_setter)
    assert not dummy.addfive
    dummy.addfive = 5
    assert dummy.addfive == 10
