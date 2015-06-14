from psh.commands.core import registered_cmds

# Import the exported commands
from psh.commands import *

# Instantiate the registered commands
for name, cls in registered_cmds.items():
	globals()[name] = cls()

# Only export the names of registered commands
__all__ = registered_cmds.keys()
