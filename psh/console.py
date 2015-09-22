import atexit
import code
import os
import readline
from psh.run import desugar, readall

from psh.commands.core import registered_cmds, shellvars

DEFAULT_HISTORY_FILE = "~/.psh_history"

def parse_cmd(potential_cmd):
    """Evaluates a potential command. If it exists in the list of
    registered commands, we return a string that would call the
    constructor for that command. If it does not exist, we wrap the
    name of the command with the RawCommand class.

    :return: A string that when evaluated by Python's `eval` feature
        would build an object of the correct type
    """
    """Begins by parsing shell and environment variables"""
    """Variable references must be wrapped in $(...)"""

    args = potential_cmd.strip().split(' ')
    #Test to see if it's a comment (line begins with #)
    #if it is, turn whole line into a command that echos nothing
    if args[0][0] == '#':
        return "echo";
    #Based on flags, it'll either 
    args = list(map(parse_var, args));
    print(args)
    cmd_name = args[0]
    args = args[1:]
    if cmd_name not in registered_cmds:
        return "RawCommand('{}')".format(potential_cmd)
    else:
        cls = registered_cmds[cmd_name].__name__
        return "{0}({1})".format(cls, str(args))


def parse_cmds(raw_input_line):
    """Parses command objects out of a single | separated string"""
    potential_cmds = raw_input_line.split('|')
    cmds = [parse_cmd(cmd) for cmd in potential_cmds]
    return cmds

def parse_var(arg):
    """Replaces shell or enviroment variable with its value"""
    global shellvars
    startindex = arg.find('$')
    #if there is a $ and it's not preceded by a \
    if startindex >= 0 and (startindex == 0 or not arg[startindex -1] == '\\'):
        endindex = arg.find(')', startindex)
        key = arg[startindex+2:endindex]
        location = arg[startindex: endindex +1]
        try:
            arg = arg.replace(location, shellvars[key])
        except(KeyError):
            arg = arg.replace(location, "");
    recurse = arg.find('$') #see if there are more variables in this block
    if(recurse > 0 and not arg[recurse - 1] == "\\"):
        return parse_var(arg)
    return arg



class HistoryConsole(code.InteractiveConsole):
    """Stolen from https://docs.python.org/2/library/readline.html

    Modified for the purposes of this project to handle special
    bash-like parsing"""

    def __init__(self, locals=None, filename="<console>",
                 histfile=os.path.expanduser(DEFAULT_HISTORY_FILE)):
        code.InteractiveConsole.__init__(self, locals, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except IOError:
                pass
            atexit.register(self.save_history, histfile)

    def raw_input(self, prompt=""):
        """Gets a single line of input for the REPL, and returns some valid
        Python for the rest of the REPL to evaluate. It's the "R" in REPL.
        If the line begins with ">", we just strip it and evaluate as valid
        Python."""
        raw_input_line = input(prompt)
        if raw_input_line == "":
            return raw_input_line
        if raw_input_line[0] == '>':
            return raw_input_line[1:]
        else:
            cmds = parse_cmds(raw_input_line)
            cmds.append("Printer()")
            mangled_input = cmds[0]
            for cmd in cmds[1:]:
                mangled_input += ".chain(" + cmd + ")"
            mangled_input += ".call()"
            print("[DEBUG]: evaluating Python: ", mangled_input)
            return mangled_input

    def parse_block():
        '''In this function, desugar if desugar is set, 
        then parse the desugared commands one at a time'''
        #TODO: DESUGAR
        return sys.stdin.readlines()


    def save_history(self, histfile):
        readline.write_history_file(histfile)
