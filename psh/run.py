import os
import os.path
import sys

from psh.commands.formatters import Printer

#No autodetection, all recognized commands must be listed here:
from psh.commands import Sort, Reverse, Echo, Example, Cat, RawCommand, Resplit, Setenv, cd, Unsetenv, Set, Unset



# Load all of the commands in the path into the global namespace as raw
# commands.
for path in os.environ['PATH'].split(':'):
    if os.path.exists(path):
        binaries = os.listdir(path)
        for binary in binaries:
            if binary not in globals():
                globals()[binary] = RawCommand(binary)


global desugar
global readall
                
def main():
    from psh.console import HistoryConsole
    console = HistoryConsole(globals())
    '''Script mode: Reads entire file in at once, skipping the interaction'''
    if sys.argv[1] = '-s':
        desugar = true
        readall = true
    '''test or "practice" mode: Reads entire file, and executes it as python'''
    elif sys.argv[1] = '-p':
        desugar = false
        readall = true
    '''interactive mode: Reads one line at a time interactively'''
    else
        desugar = true
        readall = false
    if(!readall):
        console.interact("Augmented Unix Userland")
    else:
        parse_block()

if __name__ == '__main__':
    main()
