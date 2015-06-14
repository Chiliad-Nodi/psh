from psh.commands.core import BaseCommand

from io import StringIO

class TestFormatter(BaseCommand):
    """Formatter useful for tests. Instead of printing to stdout, it
    stores any output inside a stringio buffer. This can be retrieved
    with the get_data method."""

    def __init__(self, *args, **kwargs):
        super(TestFormatter, self).__init__(*args, **kwargs)
        self.buffer = StringIO()

    def call(self):
        input_generator = self.get_input_generator()
        for line in input_generator:
            self.buffer.write(line.data.decode('utf-8'))
        return None

    def get_data(self):
        return self.buffer.getvalue()
