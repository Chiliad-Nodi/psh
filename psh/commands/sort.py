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

            mapped_inputs = map(lambda node: node.data, input_generator)
            #print "mapped_inputs ="
            #print mapped_inputs
            mapped_args = list(map(lambda arg: arg.encode("utf-8"), self.args))
            #print "mapped_args ="
            #print mapped_args
            mapped_args.extend(list(mapped_inputs))
            #print "After extend, mapped_args ="
            #print mapped_args
            sort_result = sorted(mapped_args);
            
            for arg in sort_result:
                yield TreeNode(arg)
        return output_generator
