from psh.commands.core import BaseCommand


class Printer(BaseCommand):
    """Simple formatter which accepts any object from the input
    generator and simply prints it as if it were a string."""

    def call(self):
        input_generator = self.get_input_generator()
        for node in input_generator:
            line = node.data
            print(str(line.decode('utf-8')))
        return None
