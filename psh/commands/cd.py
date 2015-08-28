from psh.commands.core import BaseCommand, register_cmd

from psh.tree import TreeNode


@register_cmd("cd")
class cd(BaseCommand):
    """Simple command that just changes directories to the specified path."""

    def call(self, *args, **kwargs):
        def output_generator():
            os.chdir(os.path.join(os.path.abspath(os.path.curdir),args[1]))
            yield TreeNode(b'')
        return output_generator
