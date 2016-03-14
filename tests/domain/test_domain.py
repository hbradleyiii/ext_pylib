#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_domain.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/11/2015

"""
A unit test for ext_pylib module's domain class and methods.
"""

import socket
import pytest

from ext_pylib.domain import Domain, get_server_ip


def test_domain():
    """Tests initializing a domain class, __str__, __repr__ and domain name properties."""
    domain = Domain('example.com')
    assert domain.name == 'example.com'
    assert str(domain) == 'example.com'
    assert domain.__repr__() == 'Domain("example.com")'
    assert domain + '/example.html' == 'example.com/example.html'
    assert 'http://' + domain == 'http://example.com'

def test_domain_eq():
    """Tests domain comparison."""
    domain_1 = Domain('example.com')
    domain_2 = Domain('example.com')
    domain_3 = Domain('anotherexample.com')
    assert domain_1 == domain_2
    assert domain_1 != domain_3
    assert domain_1 == Domain('example.com')

def test_domain_name():
    """Tests domain name property."""
    domain = Domain('example.com')
    domain.name = 'another.example.com'
    assert domain.name == 'another.example.com'
    domain.name = 'final.example.com.'
    assert domain.name == 'final.example.com'

BAD_ARGS = ['x' * 256, '#example.com', '.example.com', '', None,
            'example..com', 'bad_stuff.com']
@pytest.mark.parametrize(("args"), BAD_ARGS)
def test_domain_name_bad_values(args):
    """Tests domain name given bad values."""
    with pytest.raises(ValueError):
        domain = Domain(args)  # pylint: disable=unused-variable

def test_domain_ip():
    """Tests get_server_ip(). Assumes ip is correct."""
    assert socket.inet_aton(get_server_ip())

def test_domain_ip_bad_urls():
    """Tests get_server_ip() passing bad urls. Assumes ip is correct."""
    with pytest.raises(LookupError):
        get_server_ip(['http://example.com', 'http://techterminal.net'])

    # Try 2 bad urls with one good url:
    assert socket.inet_aton(get_server_ip(['http://example.com',
                                           'http://techterminal.net',
                                           'http://techterminal.net/myip']))

def test_domain_set_ip():
    """Tests domain's set_ip method. Not yet implemented."""
    # TODO: Write tests after implementing
    pass
