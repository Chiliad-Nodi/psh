from psh.commands.core import BaseCommand, register_cmd

from psh.tree import TreeNode


@register_cmd("sort")
class Sort(BaseCommand):
    """Sorts anything from the command line arguments as well as input
    from the previous command."""

    def __init__(self, args=[]):
        super(Sort, self).__init__()
        self.args = args

    def call(self,*args,**kwargs):
        input_generator = self.get_input_generator()
        def output_generator():
            sort_result = sorted(map(lambda arg: arg.encode("utf-8", self.args)).extend(map(lambda node: node.data, input_generator)))
            for args in sort_result:
                yeild TreeNode(arg)
        return output_generator

            """for args in sorted(self.args):
                yield TreeNode(args.encode("utf-8"))
            for node in input_generator:
                line = node.data
                yield TreeNode(line)
        return output_generator"""
