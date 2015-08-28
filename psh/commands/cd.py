from psh.commands.core import BaseCommand, register_cmd
import os;

from psh.tree import TreeNode


@register_cmd("cd")
class cd(BaseCommand):
    """Simple command that just changes directories to the specified path."""

    def __init__(self, args=[]):
        super(cd, self).__init__()
        self.args = args
    
    def call(self, *args, **kwargs):
        def output_generator():
            os.chdir(os.path.join(os.path.abspath(os.path.curdir),self.args[0]))
            yield TreeNode(b'')
        return output_generator
