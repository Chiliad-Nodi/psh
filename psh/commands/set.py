from psh.commands.core import BaseCommand, register_cmd
import os

from psh.tree import TreeNode

from psh.commands.core import shellvars

@register_cmd("set")
class Set(BaseCommand):
    """Sets a shell variable and returns nothing."""

    def __init__(self, args=[]):
        super(Set, self).__init__()
        self.args = args

        
    def call(self,*args,**kwargs):
        input_generator = self.get_input_generator()
        def output_generator():
            print (len(self.args))
            if(len(self.args) != 2):
                self.estream("Usage: set varname value");
                return output_generator
            #Get the new variable name and value
            newvar = list(filter(lambda arg: arg[0] != '-', self.args))
            global shellvars
            shellvars [newvar[0]] = newvar[1]
            yield TreeNode(b"")
        return output_generator
