import subprocess
import jinja2
from jinja2.ext import Extension


@jinja2.evalcontextfilter
def shell(eval_ctx, value, die_on_error=False, encoding="utf8"):
    if die_on_error:
        cmd = value
    else:
        cmd = "%s ; exit 0" % value
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    return output.decode(encoding)


class ShellExtension(Extension):

    def __init__(self, environment):
        super(ShellExtension, self).__init__(environment)
        environment.filters['shell'] = shell
