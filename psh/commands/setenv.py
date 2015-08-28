from psh.commands.core import BaseCommand, register_cmd
import os

from psh.tree import TreeNode

from psh.commands.core import shellvars

@register_cmd("setenv")
class Setenv(BaseCommand):
    """Sets an environment or shell variable and returns nothing."""

    def __init__(self, args=[]):
        super(Setenv, self).__init__()
        self.args = args

        
    def call(self,*args,**kwargs):
        input_generator = self.get_input_generator()
        def output_generator():
            print (len(self.args))
            if(len(self.args) < 2):
                self.estream("Usage: setenv [-e] varname value");
                return output_generator
            enviromnent = False;
            for arg in filter(lambda arg:arg[0] == '-', self.args):
                if(arg[0:2] == '-e'): #export to enviroment (as opposed to shell)
                    environment = True;
                else:
                    self.estream("Invalid argument: Ignoring " + arg)

            #Get the new variable name and value
            newvar = list(filter(lambda arg: arg[0] != '-', self.args))
            global shellvars
            shellvars [newvar[0]] = newvar[1]
            """export var to os.evironment"""
            yield TreeNode(b"")
        return output_generator
