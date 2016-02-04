#!/usr/bin/env python
#
# name:             meta.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/28/2016
#
# description:      Classes and functions for meta-programming with python.
#                   This is mostly experimental stuff. For now, class
#                   DynamicProperty is merely a close reimplementation of
#                   python's native property().
#
#                   Credit for much of this goes to:
#                   http://eev.ee/blog/2012/05/23/python-faq-descriptors/


class DynamicProperty(object):
    """A re-implementation of python's native property().
    Most of this code derived from: http://eev.ee/blog/2012/05/23/python-faq-descriptors/."""

    def __init__(self, getter=None):
        """Initializes the DynamicProperty's getter function."""
        self.getter = getter

    def __get__(self, instance, owner):
        """Returns the result of running the getter function.
        This is a wrapper for the property's actual getter function."""
        self.owner = owner  # Not used
        if instance is None:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        """Calls the setter function.
        self.set_func(instance, value)

    def setter(self, setter):
        """Sets the setter function to the passed arg setter (a function).
        Returns self. (Composite Pattern)."""
        self.set_func = setter
        return self

    @staticmethod
    def set_func(*args, **kwargs):
        """A stub. If it isn't overwritten, the property is read-only."""
        raise TypeError("Cannot modify property.  It doesn't have a setter function.")

def setdynattr(obj, attribute, getter_func=None, setter_func=None):
    """Creates a dynamic property on an object using DynamicProperty class."""
    if not getter_func:
        def getter_func(self):
            """Default getter function.
            Uses '_' + attribute name as a private variable to hold the
            property's value."""
            return getattr(self, '_' + attribute, None)

    if not setter_func:
        def setter_func(self, value):
            """Default setter function.
            Uses '_' + attribute name as a private variable to hold the
            property's value."""
            return setattr(self, '_' + attribute, value)

    setattr(obj.__class__, attribute, DynamicProperty(getter_func))
    prop = getattr(obj.__class__, attribute)
    prop = prop.setter(setter_func)
