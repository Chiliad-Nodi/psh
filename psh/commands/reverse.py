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
            #Parse flags:
            for arg in filter(lambda arg:arg[0] == '-', self.args):
                if(arg == '-s'): #separator
                    #resplit(s, args) TODO: IMPLEMENT RESPLIT
                    pass;
                else:
                    self.estream("Invalid argument: Ignoring " + arg)
            
            mapped_inputs = map(lambda node: node.data, input_generator)
            #remove all flags
            mapped_args = filter(lambda arg: arg[0] != '-', self.args)
            mapped_args = map(lambda arg: arg.encode("utf-8"), mapped_args)
            mapped_args.extend(mapped_inputs)
            #reverse arguments
            reverse_result = reversed(mapped_args);
            #return results
            for arg in reverse_result:
                yield TreeNode(arg)
        return output_generator
