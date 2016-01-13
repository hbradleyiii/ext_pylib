#!/usr/bin/env python
#
# name:             user.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       01/13/2016
#
# description:      Functions for managing users.
#

import grp
import os
import pwd

def get_current_username():
    return pwd.getpwuid(os.getuid()).pw_name

def get_current_groupname():
    return grp.getgrgid(os.getgid()).gr_name
