
class PluginManager(object):
	def __init__(self):
		self.fs = 0
		self.num_channels = 0
		self.channel_names = []
		self.data = []
		self.t = []
		self.epochs = 0
		self.tags = []

	def __repr__(self):
		return 'Plugin'
