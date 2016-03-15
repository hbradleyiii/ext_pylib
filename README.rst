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

It contains basic classes for files, directories, and domain names as well as
helpful functions for prompting and displaying terminal data. It also contains
some functions in the meta module for meta programming.

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
The domain module consists of the class ``Domain()``. It is used for binding an
IP and a domain name in one object. It requires one paramater at
initialization: the domain name as a string.

*Future*: There are tentative plans for including a wrapper for DNS API's such
as Rackspace's API.

Also included in this module is the function ``get_server_ip()``. This function
is designed to get the public IP of the server. It works by making an http
request to a url that returns only the IP address as a string. It takes one
parameter: ``get_ip_urls`` a list of one or more urls to use.

Files Module
------------
A class to manage and create files. Also includes three mixin classes Parsable,
Section, and Template.

Section Mixin
~~~~~~~~~~~~~
The Section mixin adds methods useful for processing template section files. A
section file is a template of a configuration file that only represents a
particular section of that file. It begins and ends with a delineator

For example:

.. code:: bash

    ## START:SECTION_NAME ##
    content here...
    ## END:SECTION_NAME ##

A use case would be how WordPress delineates a particular section of the
htaccess file in its root directory with a start line and an end line. This is
a section of the full htaccess file and could be managed by a Section mixin.

Template Mixin
~~~~~~~~~~~~~~
The Template mixin adds a method useful for processing a regular template file:
``apply_using()``. It assumes that the file contains placeholder text to be
replaced by actual data. The placeholders and actual data are passsed into the
method as a dict. The resulting data is returned (presumably to be saved in
another file.)

Parsable Mixin
~~~~~~~~~~~~~~
The Parsable mixin adds a method useful for parsing (presumably) configuration
files. It takes a dict of attribute names and regexes to be used. When
``setup_parsing()`` is called, a dynamic property is created for getting and
setting a value in self.data based on the regex.

Input Module
------------
The prompts module contains a number of helpful functions for prompting for
user input.

The ``prompt()`` function prints a prompt question and expects the user to type
a 'yes' or 'no' answer. It requires a string passed as the text to be
displayed.  The default response (just pressing enter) is 'yes' (true). This
default can be changed by passing the attribute ``default=False``. The function
returns a bool cooresponding to the appropriate value.

The ``prompt_str()`` function prints a prompt and expects the user to type a
string. It requires a string passed as the text to be displayed. It also takes
an optional ``default`` value that can be set to a default string. If the user
just presses enter the default string is used. The function returns the string
that the user typed (or the default string).

The ``warn_prompt()`` function is similar to the ``prompt_str()`` function.

Meta Module
-----------
The meta module is useful for meta programming. This module is experimental. It
has the object ``DynamicPropery`` which is a close reimplementation of Python's
native ``property()``. It allows creating a class property on the fly. It is
initialized with a getter function to return the property value and a setter
function can be initialized by calling ``create_setter()`` on the property
itself. Note that this must be done on the class *not* an instance of the class.

Credit for much of this object goes to:
http://eev.ee/blog/2012/05/23/python-faq-descriptors/

The best way to understand this object is to look at an example:

.. code:: python

    from ext_pylib.meta import DynamicProperty

    def getter_func(self):
        return self._property

    def setter_func(self, value):
        self._property = value

    class Cls(object): pass
    instance = Cls()
    instance.__class__.new_property = DynamicProperty(getter_func)
    instance.__class__.new_property = instance.__class__.new_propety.create_setter(setter_func)

    instance.new_property = 'value'
    print instance.new_property  # prints: 'value'

This module also has the function ``setdynattr()`` which is a convenient
wrapper around the ``DynamicProperty`` class. It takes an object, an attribute
(as a string), and optional getter and setter functions. If the getter and
setter functions are not supplied, default getter and setter functions are used
that merely get and set an attribute with the name '_' + attribute.

Password Module
---------------
The password module has the function ``generate_pw()`` for generating a
relatively strong pseudo-random password. This function takes two optional
parameters. The ``length`` parameter determines how long the password will be.
It defaults to 18 characters. The ``char_set`` is a dict of a string of
characters to use as a set. These are the set (as a python string) of
characters that will not appear twice in a row in the generated password. The
default character set has a set of numbers, lowercase letters, uppercase
letters, and special characters.  This prevents having a password with two
numbers in a row or two lowercase characters in a row and makes the password
stronger. Leaving the char_set as default is good for most circumstances,
although it may be necessary to change it for various password restrictions.

The default character set is:

.. code:: python

    DEFAULT_CHAR_SET = {
        'small': 'abcdefghijklmnopqrstuvwxyz',
        'nums': '0123456789',
        'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'special': '^!$%&=?{[]}+~#-_.:,;<>|'
    }

Terminal Module
---------------
The terminal module is a collection of functions that aid in modifying the
terminal output and as well as adding color and text effects. It is made up of
two seperate modules, the ansi module and the colors module.

Because of the interactive nature of this module, the tests must be called
directly:

.. code:: bash

    $ cd <ext_pylib directory>/terminal
    $ python ./interactive_test.py

Ansi Module
~~~~~~~~~~~
The ansi module contains a number of constants representing ANSI excape codes
and functions for printing them to the screen. Most of the functions take an
optional parameter ``get_string`` which defaults to ``False`` and indicates
that the escape will be printed to the screen. When this is set to ``True``,
the function will return a string. Some of the functions, such as the cursor
functions, take optional integer parameters. These functions are relatively
straightforward.

Cursor Functions
................
 * ``cursor_hide(get_string=False)`` - hides the cursor
 * ``cursor_show(get_string=False)`` - shows the cursor
 * ``cursor_up(n=1, get_string=False)`` - moves your cursor up 'n' cells
 * ``cursor_down(n=1, get_string=False)`` - moves your cursor down 'n' cells
 * ``cursor_right(n=1, get_string=False)`` - moves your cursor right (forward)
   'n' cells
 * ``cursor_left(n=1, get_string=False)`` - moves your cursor left (backward)
   'n' cells
 * ``cursor_next_line(n=1, get_string=False)`` - moves your cursor to the next
   'n' lines
 * ``cursor_previous_line(n=1, get_string=False)`` - moves your cursor to the
   previous 'n' lines
 * ``cursor_horizontal_absolute(n=1, get_string=False)`` - moves your cursor to
   the 'n' column
 * ``cursor_position(x=0, y=0, get_string=False)`` - Moves youescape = cursor
   to position (x, y)  NOTE: This assumes starting at (0, 0) which is
   different than the ANSI standard; it also assumes (x, y) and not (y, x) per
   ANSI standard.
 * ``cursor_save(get_string=False)`` - save the current cursor position
 * ``cursor_restore(get_string=False)`` - restore the last saved cursor position
 * ``attributes_save(get_string=False)`` - save the current cursor position and
   attributes
 * ``attributes_restore(get_string=False)`` - restore the last saved cursor
   position and attributes
 * ``get_cursor_pos()`` - returns a tuple of (x, y) of current cursor position
   NOTE: this follows conventional (x, y) order and starts with (0, 0) and not
   the order according to the ANSI standard.

Clearing the Screen
...................
 * ``clear(get_string=False)`` - clears the entire screen
 * ``clear_down(get_string=False)`` - clears the screen from the cursor down
 * ``clear_up(get_string=False)`` - clears the screen from the cursor down
 * ``clear_line(get_string=False)`` - clears the entire line
 * ``clear_line_forward(get_string=False)`` - clears the entire line
 * ``clear_line_back(get_string=False)`` - clears the entire line
 * ``reset(get_string=False)`` - clears the entire screen and places cursor at
   top left corner

Terminal Settings
.................
 * ``reset_terminal(get_string=False)`` - resets the terminal
 * ``enable_line_wrap(get_string=False)`` - enables line wrapping
 * ``disable_line_wrap(get_string=False)`` - disables line wrapping
 * ``set_scroll_all(get_string=False)`` - enable scrolling for the entire screen
 * ``set_scroll(start_row, end_row, get_string=False)`` - enable scrolling from
   start_row to end_row
 * ``scroll_up(get_string=False)`` - scrolls up
 * ``scroll_down(get_string=False)`` - scrolls down

Colors Module
~~~~~~~~~~~~~
The colors module contains a number of functions for printing color to the
screen. These functions require a string to be colored and will return a string
with the appropriate color. The functions can be infinitely nested or passed as
optional additional arguments from any of the other functions. Note that it is
possible to mix combinations that don't make sense. A string cannot be both
green and red. The last (or innermost) escape sequence is the one that will
affect the display.

For example:

.. code:: python

    print bold('WARN:', red) + red_on_white('This is an example warning.')
    print underline(green(on_blue('This is an example of nesting color functions.')))
    print blue('This is an example of passing color functions to another function.', on_black, bold)

Text Effects
............
 * ``normal(string, *funcs, **additional)``
 * ``underline(string, *funcs, **additional)``
 * ``bold(string, *funcs, **additional)``
 * ``blink(string, *funcs, **additional)``
 * ``rblink(string, *funcs, **additional)``
 * ``reverse(string, *funcs, **additional)``
 * ``conceal(string, *funcs, **additional)``

Basic Colors
............
 * ``black(string, *funcs, **additional)``
 * ``red(string, *funcs, **additional)``
 * ``green(string, *funcs, **additional)``
 * ``yellow(string, *funcs, **additional)``
 * ``blue(string, *funcs, **additional)``
 * ``magenta(string, *funcs, **additional)``
 * ``cyan(string, *funcs, **additional)``
 * ``white(string, *funcs, **additional)``

Basic Backgrounds
.................

 * ``on_black(string, *funcs, **additional)``
 * ``on_red(string, *funcs, **additional)``
 * ``on_green(string, *funcs, **additional)``
 * ``on_yellow(string, *funcs, **additional)``
 * ``on_blue(string, *funcs, **additional)``
 * ``on_magenta(string, *funcs, **additional)``
 * ``on_cyan(string, *funcs, **additional)``
 * ``on_white(string, *funcs, **additional)``

Combined Foreground Color on Background Color
.............................................

 * ``red_on_black(string, *funcs, **additional)``
 * ``green_on_black(string, *funcs, **additional)``
 * ``yellow_on_black(string, *funcs, **additional)``
 * ``blue_on_black(string, *funcs, **additional)``
 * ``magenta_on_black(string, *funcs, **additional)``
 * ``cyan_on_black(string, *funcs, **additional)``
 * ``white_on_black(string, *funcs, **additional)``
 * ``black_on_red(string, *funcs, **additional)``
 * ``green_on_red(string, *funcs, **additional)``
 * ``yellow_on_red(string, *funcs, **additional)``
 * ``blue_on_red(string, *funcs, **additional)``
 * ``magenta_on_red(string, *funcs, **additional)``
 * ``cyan_on_red(string, *funcs, **additional)``
 * ``white_on_red(string, *funcs, **additional)``
 * ``black_on_green(string, *funcs, **additional)``
 * ``red_on_green(string, *funcs, **additional)``
 * ``yellow_on_green(string, *funcs, **additional)``
 * ``blue_on_green(string, *funcs, **additional)``
 * ``magenta_on_green(string, *funcs, **additional)``
 * ``cyan_on_green(string, *funcs, **additional)``
 * ``white_on_green(string, *funcs, **additional)``
 * ``black_on_yellow(string, *funcs, **additional)``
 * ``red_on_yellow(string, *funcs, **additional)``
 * ``green_on_yellow(string, *funcs, **additional)``
 * ``blue_on_yellow(string, *funcs, **additional)``
 * ``magenta_on_yellow(string, *funcs, **additional)``
 * ``cyan_on_yellow(string, *funcs, **additional)``
 * ``white_on_yellow(string, *funcs, **additional)``
 * ``black_on_blue(string, *funcs, **additional)``
 * ``red_on_blue(string, *funcs, **additional)``
 * ``green_on_blue(string, *funcs, **additional)``
 * ``yellow_on_blue(string, *funcs, **additional)``
 * ``magenta_on_blue(string, *funcs, **additional)``
 * ``cyan_on_blue(string, *funcs, **additional)``
 * ``white_on_blue(string, *funcs, **additional)``
 * ``black_on_magenta(string, *funcs, **additional)``
 * ``red_on_magenta(string, *funcs, **additional)``
 * ``green_on_magenta(string, *funcs, **additional)``
 * ``yellow_on_magenta(string, *funcs, **additional)``
 * ``blue_on_magenta(string, *funcs, **additional)``
 * ``cyan_on_magenta(string, *funcs, **additional)``
 * ``white_on_magenta(string, *funcs, **additional)``
 * ``black_on_cyan(string, *funcs, **additional)``
 * ``red_on_cyan(string, *funcs, **additional)``
 * ``green_on_cyan(string, *funcs, **additional)``
 * ``yellow_on_cyan(string, *funcs, **additional)``
 * ``blue_on_cyan(string, *funcs, **additional)``
 * ``magenta_on_cyan(string, *funcs, **additional)``
 * ``white_on_cyan(string, *funcs, **additional)``
 * ``black_on_white(string, *funcs, **additional)``
 * ``red_on_white(string, *funcs, **additional)``
 * ``green_on_white(string, *funcs, **additional)``
 * ``yellow_on_white(string, *funcs, **additional)``
 * ``blue_on_white(string, *funcs, **additional)``
 * ``magenta_on_white(string, *funcs, **additional)``
 * ``cyan_on_white(string, *funcs, **additional)``

User Module
-----------
The usermodule consists of two wrapper functions. ``get_current_username()``
returns the current user as a string. ``get_current_groupname()`` likewise
returns the current user's group as a string.

----

Soli Deo gloria.
