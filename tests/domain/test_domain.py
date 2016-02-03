#!/usr/bin/env python
#
# name:             test_domain.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       11/11/2015
#
# description:      A unit test for ext_pylib module's domain class and
#                   methods.
#

from ext_pylib.domain import Domain, get_server_ip
import pytest
import socket

def test_domain():
    """Tests initializing a domain class, __str__, __repr__ and domain name properties."""
    domain = Domain('example.com')
    assert domain.name == 'example.com'
    assert str(domain) == 'example.com'
    assert domain.__repr__() == 'Domain("example.com")'
    assert domain + '/example.html' == 'example.com/example.html'
    assert 'http://' + domain == 'http://example.com'

def test_domain_name():
    """Tests domain name property."""
    domain = Domain('example.com')
    domain.name = 'another.example.com'
    assert domain.name == 'another.example.com'
    domain.name = 'final.example.com.'
    assert domain.name == 'final.example.com'

bad_args = [ 'x' * 256, '#example.com', '.example.com', '', None,
            'example..com', 'bad_stuff.com']
@pytest.mark.parametrize(("args"), bad_args)
def test_domain_name_bad_values(args):
    with pytest.raises(ValueError):
        domain = Domain(args)

def test_domain_ip():
    """Tests domain ip property for validity. Assumes ip is correct."""
    assert socket.inet_aton(get_server_ip())

def test_domain_set_ip():
    """Tests domain's set_ip method. Not yet implemented."""
    # TODO: Write tests after implementing
    pass
