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
template = env.from_string("{{ 'date --rfc-2822'|shell() }}")
result = template.render()

# example: result == "Fri, 31 Jan 2020 13:35:56 +0100"
# [...]

```
