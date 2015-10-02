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

'''These are to define shell interactivity level on startup'''
desugar = True
readall = False

def main():
    '''interactive mode: Reads one line at a time interactively
    this is the default'''
    global desugar
    global readall
    desugar = True
    readall = False
   
    if len(sys.argv) >= 2:
        '''Script mode: Reads entire file in at once, skipping the interaction'''
        if sys.argv[1] == '-s':
            desugar = True
            readall = True
            '''test or "practice" mode: Reads entire file, and executes it as python'''
        elif sys.argv[1] == '-p':
            desugar = False
            readall = True
        else:
            #print help message
            pass
    from psh.console import HistoryConsole
    console = HistoryConsole(globals())
    if(not readall):
        console.interact("Augmented Unix Userland")
    else:
        console.parse_block()

if __name__ == '__main__':
    main()
