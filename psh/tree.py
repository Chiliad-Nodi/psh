class TreeNode(object):
	"""A tree node holds some data and has iterable children."""

	def __init__(self, data):
		"""Initializes a data. The data can be any type, but it usually
		is an ordered dictionary."""
		self.parent = None
		self.data = data
		self.children = []

	def add_child(self, child):
		"""Adds a child to the node."""
		child.parent = self
		self.children.apppend(child)

	def children(self):
		"""Returns an iterable generator for all the children nodes."""
		def children_generator():
			for child in self.children:
				yield child
		return children_generator()
