from psh.commands.core import BaseCommand, register_cmd

from psh.tree import TreeNode


@register_cmd("reverse")
class Reverse(BaseCommand):
    """Reverses anything from the command line arguments as well as input
    from the previous command."""

    def __init__(self, args=[]):
        super(Reverse, self).__init__()
        self.args = args

    def call(self,*args,**kwargs):
        input_generator = self.get_input_generator()
        def output_generator():

            mapped_inputs = map(lambda node: node.data, input_generator)
            print "mapped_inputs ="
            print mapped_inputs
            mapped_args = map(lambda arg: arg.encode("utf-8"), self.args)
            print "mapped_args ="
            print mapped_args
            mapped_args.extend(mapped_inputs)
            print "After extend, mapped_args ="
            print mapped_args
            reverse_result = reversed(mapped_args);
            
            for arg in reverse_result:
                yield TreeNode(arg)
        return output_generator
