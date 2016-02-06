#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             domain.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/03/2015
#
#                   TODO: add DNS API capabilities

"""
ext_pylib.domain.domain
~~~~~~~~~~~~~~~~~~~~~~~

A class to describe and manage a domain name and it's corresponding ip address.
"""

from __future__ import print_function

import re
import socket

try:
    import requests
except ImportError:
    raise ImportError("ext_pylib's domain module requires module requests.")

from builtins import object, str


def get_server_ip(get_ip_urls = None):
    """Return the IP of this server."""
    get_ip_urls = get_ip_urls or ['http://mediamarketers.com/myip/',
                                  'http://dev.mediamarketers.com/myip/']
    for url in get_ip_urls:
        ip = requests.get(url).text
        if not ip == '127.0.0.1':
            return ip
    else:  # No IP found
        raise LookupError('Could not successfully retrieve ip of server.')


class Domain(object):
    """An interface for a Domain object.

    Used for binding an IP and a domain name in one object. Also provides a
    method for setting the IP using a DNS API. Note that this is yet to be
    implemented.

    :param name: The domain name the Domain() object represents.

    Usage::

        >>> from ext_pylib.domain import Domain
        >>> domain = Domain('example.com')
        >>> domain.name
        'example.com'
    """

    def __init__(self, name=''):
        """Initializes a new Domain instance."""
        self.name = name

    def __repr__(self):
        """Returns a python string that evaluates to the object instance."""
        return 'Domain("' + self.name + '")'

    def __str__(self):
        """Returns a string with the domain name."""
        return self.name

    def __add__(self, other):
        """Allows concatenation."""
        return str(self) + other

    def __radd__(self, other):
        """Allows concatenation."""
        return other + str(self)

    def set_ip(self, ip = ''):
        """Points the domain's A record to this server -- not yet implemented."""
        # TODO: Implement DNS API
        print('Current serverip: ' + self.ip)
        print('[*] DNS API not yet implemented.')
        print('[*] Cannot set to IP: ' + ip)
        print('[*] DNS API not yet implemented.')

    @property
    def ip(self):
        """Returns the A Record IP of the domain."""
        try:
            return self._ip
        except AttributeError:
            self._ip = socket.gethostbyname(self.name)
            return self._ip

    @property
    def name(self):
        """Return the domain name as a string."""
        return self._name

    @name.setter
    def name(self, name):
        """Validate and set the domain name."""
        if name in ['', None]:
            raise ValueError('Domain name cannot be an empty string.')
        if name[-1] == ".":
            name = name[:-1]  # strip exactly one dot from the right, if present
        if len(name) > 255:
            raise ValueError('Domain Name cannot be longer than 255 characters.')
        allowed_chars = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
        if not all(allowed_chars.match(x) for x in name.split(".")):
            raise ValueError('Domain Name ' + name + ' is not valid.')
        self._name = name
