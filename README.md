# ext_pylib
Extra Python Libraries

This is a work in progress. Use at your own risk.

ext_pylib is a group of submodules that are useful scaffolding for other larger
projects. I began developing it after noticing how often I was repeating
several patterns for server scripts. It works well for building server scripts.

## Installing and Including in projects
TODO

### Running Tests
```
$ cd <project directory>
$ py.test
```

## Modules
TODO

### Domain Module
TODO
### Files Module
A class to manage and create files. Also includes three
mixin classes Parsable, Section, and Template.

#### Section Mixin

The Section mixin adds methods useful for processing
template section files. A section file is a template of a
configuration file that only represents a particular
section of that file. It begins and ends with a delineator
(for example: ## START:SECTION_NAME ## and ##
END:SECTION_NAME ##). A use case would be how WordPress
delineates a particular section of the htaccess file in its
root directory with a start line and an end line. This is a
section of the full htaccess file and could be managed by a
Section mixin.
#### Template Mixin

The Template mixin adds a method useful for processing a
regular template file: apply_using(). It assumes that the
file contains placeholder text to be replaced by actual
data. The placeholders and actual data are passsed into the
method as a dict. The resulting data is returned
(presumably to be saved in another file.)
#### Parsable Mixin

The Parsable mixin adds a method useful for parsing
(presumably) configuration files. It takes a dict of
attribute names and regexes to be used. When parse() is
called, the regex is run on the data and the result (or
None) is assigned to an attribute on the instance.
TODO: how to keep from clobering important attributes?

### Password Module
TODO
### Prompt Module
TODO
### User Module
TODO

