# jinja2_shell_extension

[//]: # (automatically generated from https://github.com/metwork-framework/github_organization_management/blob/master/common_files/README.md)

**Status (master branch)**

[![GitHub CI](https://github.com/metwork-framework/jinja2_shell_extension/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/metwork-framework/jinja2_shell_extension/actions?query=workflow%3ACI+branch%3Amaster)
[![Maintenance](https://raw.githubusercontent.com/metwork-framework/resources/master/badges/maintained.svg)](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)




## What is it ?

This is a [jinja2](http://jinja.pocoo.org/) extension to execute system/shell
commands from a template.

**WARNING: be sure to valid any string submitted to this filter as you can
open security holes with it**

## Syntax

The syntax is `'full_command_with_args'|shell([die_on_error_boolean_flag], [encoding])`.

## Example

```python

from jinja2 import Template, Environment

# We load the extension in a jinja2 Environment
env = Environment(extensions=["jinja2_shell_extension.ShellExtension"])

# For the example, we use a template from a simple string
template = env.from_string("Wed, 21 May 2025 22:04:33 +0000
")
result = template.render()

# example: result == "Fri, 31 Jan 2020 13:35:56 +0100"
# [...]

```






## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.



## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.



## Sponsors

*(If you are officially paid to work on MetWork Framework, please contact us to add your company logo here!)*

[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/sponsors/meteofrance-small.jpeg)](http://www.meteofrance.com)
