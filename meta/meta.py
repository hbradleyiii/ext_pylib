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
#


class DynamicProperty(object):
    """A re-implementation of python's native property().
    most of this code from: http://eev.ee/blog/2012/05/23/python-faq-descriptors/"""

    def __init__(self, getter=None):
        self.getter = getter

    def __get__(self, instance, owner):
        self.owner = owner  # Not used
        if instance is None:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        self.set_func(instance, value)

    def setter(self, setter):
        self.set_func = setter
        return self

    @staticmethod
    def set_func(*args, **kwargs):
        raise TypeError("Cannot modify property.  It doesn't have a setter function.")

def setdynattr(obj, attribute, getter_func=None, setter_func=None):
    if not getter_func:
        def getter_func(self):
            return getattr(self, '_' + attribute, None)

    if not setter_func:
        def setter_func(self, value):
            return setattr(self, '_' + attribute, value)

    setattr(obj.__class__, attribute, DynamicProperty(getter_func))
    prop = getattr(obj.__class__, attribute)
    prop = prop.setter(setter_func)
