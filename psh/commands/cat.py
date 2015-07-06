from psh.commands.core import BaseCommand, register_cmd

from psh.tree import TreeNode


@register_cmd("cat")
class Cat(BaseCommand):
    """Concatenates files"""

    def __init__(self, args=[]):
        super(Cat, self).__init__()
        self.args = args

    def call(self,*args,**kwargs):
        input_generator = self.get_input_generator()
        def output_generator():
            mapped_args = map(lambda arg: arg.encode("utf-8"), self.args)
            for arg in mapped_args:
                if arg == '-':
                    for node in input_generator:
                        line = node.data
                        yield TreeNode(line)
                else:
                    f = open(arg, 'r')
                    yield TreeNode(f.read())
        return output_generator
