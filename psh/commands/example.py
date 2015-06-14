from psh.commands.core import BaseCommand, register_cmd

from psh.tree import TreeNode


@register_cmd("example")
class Example(BaseCommand):
    """Simple command that just returns 'example' and 'command'. Does
    nothing at all with the input."""

    def call(self, *args, **kwargs):
        def output_generator():
            yield TreeNode(b'example')
            yield TreeNode(b'command')
        return output_generator
