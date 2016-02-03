#!/usr/bin/env python
#
# name:             domain.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/03/2015
#
# description:      A class to describe and manage a domain name and
#                   corresponding ip address.
#
#                   TODO: add DNS API capabilities

try:
    import requests
except ImportError:
    raise ImportError('ext_pylib\'s domain module requires module requests.')

import re
import socket


def get_server_ip(self):
    """Return the IP of this server."""
    # TODO: Turn this into a list of values that can be passed in at init.
    server_ip = requests.get('http://mediamarketers.com/myip/').text
    if server_ip == '127.0.0.1':
        server_ip = requests.get('http://dev.mediamarketers.com/myip/').text
    return server_ip


SERVER_IP = get_server_ip


# Domain(domain)
#   A class to describe and manage a domain name and corresponding ip address.
#
#   methods:
#       set_ip()  - not yet implemented
class Domain(object):

    def __init__(self, name='', getip_urls=None):
        """Initializes a new Domain instance."""
        getip_urls = getip_urls or []
        self.name = name
        self.getip_urls = getip_urls

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
        print '[*] DNS API not yet implemented.'
        print '[*] Cannot set to IP: ' + ip
        print '[*] DNS API not yet implemented.'
        self.verify()

    ################
    # Properties

    @property
    def ip(self):
        """Returns the A Record IP of the domain."""
        return socket.gethostbyname(self.name)

    @property
    def name(self):
        """Return the domain name as a string."""
        return self.__name

    @name.setter
    def name(self, name):
        """Validate and set the domain name, and, if necessary, prompt for correction."""
        while True:
            if name in ['', None]:
                name = raw_input("What is the site name? [example.com] ")
            if name[-1] == ".":
                name = name[:-1] # strip exactly one dot from the right, if present
            if len(name) > 255:
                print 'name cannot be longer than 255 characters.'
                name = '' # Forces reprompt and continues the loop
            allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
            if not all(allowed.match(x) for x in name.split(".")):
                print 'Domain name ' + name + ' is not valid.'
                name = '' # Forces reprompt and continues the loop
            if name != '':
                break
        self.__name = name
