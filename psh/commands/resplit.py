from functools import reduce

from psh.commands.core import BaseCommand, register_cmd

from psh.tree import TreeNode


@register_cmd("resplit")
class Resplit(BaseCommand):
    """takes a list of strigns delimted by oldsep, glues it back together, and splits it along seperator"""

    def __init__(self, args=[]):
        super(Resplit, self).__init__()
        self.args = args

    def call(self,*args,**kwargs):
        input_generator = self.get_input_generator()
        def output_generator():
            seperator = " " #What to spilt by
            oldsep = " " #What to insert before seperation
            #Parse flags:
            for arg in filter(lambda arg:arg[0] == '-', self.args):
                if(arg[0:2] == '-s'): #separator
                    seperator = arg[2:]
                elif(arg[0:2] == '-o'): #oldsep
                    oldsep = arg;
                else:
                    self.estream("Invalid argument: Ignoring " + arg)

            #remove flags from inputs, get proper encoding
            filtered_args = filter(lambda arg: arg[0] != '-', self.args)
            #mapped_args = map(lambda arg: arg.encode("utf-8"), filtered_args)
            mapped_inputs = list(map(lambda node: node.data, input_generator))
            mapped_inputs.extend(list(filtered_args))

            #perform the respliting
            mapped_inputs = reduce(lambda x, y: str(x) + str(oldsep) + str(y), list(mapped_inputs))
            mapped_inputs = mapped_inputs.split(seperator)
            
            
            for piece in mapped_inputs:
                 yield TreeNode(piece.encode("utf-8"))
        return output_generator
