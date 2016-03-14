ext_pylib
#########
extra python modules for server script scaffolding
==================================================

.. image:: https://travis-ci.org/hbradleyiii/ext_pylib.svg?branch=master
    :target: https://travis-ci.org/hbradleyiii/ext_pylib

.. image:: https://www.quantifiedcode.com/api/v1/project/b9f8a6c7f3724ee4896e7cd8d2a865aa/badge.svg
    :target: https://www.quantifiedcode.com/app/project/b9f8a6c7f3724ee4896e7cd8d2a865aa :alt: Code issues

----

This is a work in progress. Use at your own risk.

ext_pylib is a group of submodules that are useful scaffolding for other larger
projects. I began developing it after noticing how often I was repeating
several patterns for server scripts. It works well for building server scripts.

Installing and Including in projects
====================================

Installing ext_pylib
--------------------

.. code:: bash

    $ pip install ext_pylib

Running Tests
-------------

.. code:: bash

    $ cd <ext_pylib directory>
    $ py.test

Modules
=======

Domain Module
-------------
TODO

Files Module
------------
A class to manage and create files. Also includes three
mixin classes Parsable, Section, and Template.

Section Mixin
~~~~~~~~~~~~~
The Section mixin adds methods useful for processing
template section files. A section file is a template of a
configuration file that only represents a particular
section of that file. It begins and ends with a delineator

For example:

.. code:: bash

    ## START:SECTION_NAME ##
    content here...
    ## END:SECTION_NAME ##

A use case would be how WordPress
delineates a particular section of the htaccess file in its
root directory with a start line and an end line. This is a
section of the full htaccess file and could be managed by a
Section mixin.

Template Mixin
~~~~~~~~~~~~~~
The Template mixin adds a method useful for processing a
regular template file: ``apply_using()``. It assumes that the
file contains placeholder text to be replaced by actual
data. The placeholders and actual data are passsed into the
method as a dict. The resulting data is returned
(presumably to be saved in another file.)
#### Parsable Mixin

The Parsable mixin adds a method useful for parsing
(presumably) configuration files. It takes a dict of
attribute names and regexes to be used. When
``setup_parsing()`` is called, a dynamic property is created
for getting and setting a value in self.data based on the
regex.

Password Module
---------------
The password module has the function ``generate_pw()`` for generating a
relatively strong pseudo-random password. This function takes two optional
parameters. The ``length`` parameter determines how long the password will be.
It defaults to 18 characters. The ``char_set`` is a dict of a string of
characters to use as a set. These are the set (as a python string) of
characters that will not appear twice in a row. The default character set has a
set of numbers, lowercase letters, uppercase letters, and special characters.
This prevents having a password with two numbers in a row, or two lowercase
characters in a row and makes the password stronger. Leaving this as default is
good for most circumstances, although it may be necessary to change it for
various password restrictions.

The default character set is:

.. code:: python

    DEFAULT_CHAR_SET = {
        'small': 'abcdefghijklmnopqrstuvwxyz',
        'nums': '0123456789',
        'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'special': '^!$%&=?{[]}+~#-_.:,;<>|'
    }

Prompt Module
---------------
TODO

User Module
-----------
TODO

----

Soli Deo gloria.
