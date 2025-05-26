from jinja2 import Template, Environment


def test_no_extension():
    template = Template('foo {{ bar }}')
    result = template.render(bar="foo")
    assert result == "foo foo"


def test_extension1():
    env = Environment(extensions=["jinja2_shell_extension.ShellExtension"])
    template = env.from_string("test {{ \"whoami\"|shell }}")
    result = template.render()
    assert len(result) >= 6


def test_input():
    env = Environment(extensions=["jinja2_shell_extension.ShellExtension"])
    template = env.from_string("{{ 'cat' | shell(input='meow', text=true) }}")
    result = template.render()
    assert result == "meow"
