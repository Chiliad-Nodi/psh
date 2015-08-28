from __future__ import print_function
from io import StringIO
import os
import sys

from psh.tree import TreeNode

ERROR_LOG = "~/.error"

shellvars = {"SHELL":"psh"}

class BaseCommand(object):
    """Commands can be used to chain the execution of multiple programs
    together. You can chain multiple commands together using commands

    For example:
    ls = RawCommand(["ls"])
    grep = RawCommand(["grep", "potato"])
    printer = Printer()
    ls.chain(grep).chain(printer).call()
    """

    def __init__(self, args=None, errorlog=os.path.expanduser(ERROR_LOG)):
        self.cmd_args = args
        self.prev_cmd = None
        self.errorlog = errorlog

    def call(self, *args, **kwargs):
        """Implicitly calls any chained commands, returning a function
        to make an input generator."""
        raise NotImplementedError("Must implement call")

    def get_input_generator(self):
        """Gets the input generator from the previous command, if it
        exists. If it doesn't exist, we just return an empy list so that
        when you iterate over it, it does nothing."""
        if self.prev_cmd is not None:
            make_input_generator = self.prev_cmd.call()
            input_generator = make_input_generator()
        else:
           input_generator = []
        return input_generator

    def chain(self, cmd):
        """Chains a command to another command, returning the other command"""
        cmd.prev_cmd = self
        return cmd

    def estream(self, msg):
            print(msg, file=sys.stderr)


registered_cmds = {}

def register_cmd(name):
    def decorator(cls):
        """Decorator for putting all of the commands in one nice place."""
        registered_cmds[name] = cls
        return cls
    return decorator
