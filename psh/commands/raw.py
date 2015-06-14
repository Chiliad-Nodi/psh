import shlex

from psh.commands.formatters import Printer
from psh.commands import BaseCommand
from psh.tree import TreeNode


class RawCommand(BaseCommand):
    """Fallback raw command that just invokes an existing Unix utility program
    with the builtin subprocess module. Each output object is just a tree node
    whose data is a simple string."""

    def __init__(self, cmd):
        super(RawCommand, self).__init__()
        self.cmd = cmd

    def call(self, *args, **kwargs):
        input_generator = self.get_input_generator()
        import subprocess
        try:
            p = subprocess.Popen(shlex.split(self.cmd), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            def make_output_generator():
                input_str = b""
                for node in input_generator:
                    line = node.data
                    input_str += line + b'\n'
                outs, errs = p.communicate(input_str)
                if outs:
                    yield TreeNode(outs)

            return make_output_generator
        except:
            import traceback
            traceback.print_exc()
        return []
