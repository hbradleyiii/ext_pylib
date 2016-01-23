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

import re
import requests
import socket


# Domain(domain)
#   A class to describe and manage a domain name and corresponding ip address.
#
#   methods:
#       set_ip()  - not yet implemented
class Domain(object):

    def __init__(self, domain = ''):
        """Initializes a new Domain instance."""
        self.domain = domain

    def __repr__(self):
        """Returns a python string that evaluates to the object instance."""
        return 'Domain(' + self.domain + ')'

    def __str__(self):
        """Returns a string with the domain name."""
        return self.domain

    def __add__(self, other):
        """Allows concatenation."""
        return str(self) + other

    def __radd__(self, other):
        """Allows concatenation."""
        return other + str(self)

    def set_ip(self, ip = ''):
        """Points the domain's A record to this server -- not yet implemented."""
        print '[*] DNS API not yet implemented.'
        self.verify()

    ################
    # Properties

    @property
    def ip(self):
        """Returns the A Record IP of the domain."""
        return socket.gethostbyname(self.domain)

    @property
    def server_ip(self):
        """Return the IP of this server."""
        # TODO: Turn this into a list of values that can be passed in at init.
        server_ip = requests.get('http://mediamarketers.com/myip/').text
        if server_ip == '127.0.0.1':
            server_ip = requests.get('http://dev.mediamarketers.com/myip/').text
        return server_ip

    @property
    def domain(self):
        """Return the domain as a string."""
        return self.__domain

    @domain.setter
    def domain(self, domain):
        """Validate and set the domain, and, if necessary, prompt for correction."""
        while True:
            if domain == '' or domain == None:
                domain = raw_input("What is the site domain? [example.com] ")
            if domain[-1] == ".":
                domain = domain[:-1] # strip exactly one dot from the right, if present
            if len(domain) > 255:
                print 'Domain cannot be longer than 255 characters.'
                domain = '' # Forces reprompt and continues the loop
            allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
            if not all(allowed.match(x) for x in domain.split(".")):
                print 'Domain ' + domain + ' is not valid.'
                domain = '' # Forces reprompt and continues the loop
            if domain != '':
                break
        self.__domain = domain
