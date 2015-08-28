import os
import os.path


from psh.commands.formatters import Printer

#No autodetection, all recognized commands must be listed here:
from psh.commands import Sort, Reverse, Echo, Example, Cat, RawCommand, Resplit, Setenv, cd, Unsetenv

# Load all of the commands in the path into the global namespace as raw
# commands.
for path in os.environ['PATH'].split(':'):
    if os.path.exists(path):
        binaries = os.listdir(path)
        for binary in binaries:
            if binary not in globals():
                globals()[binary] = RawCommand(binary)


def main():
    from psh.console import HistoryConsole
    console = HistoryConsole(globals())
    console.interact("Augmented Unix Userland")


if __name__ == '__main__':
    main()
