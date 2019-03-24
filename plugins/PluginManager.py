import sys
from importlib import reload


class PluginManager(object):
	def __init__(self):
		self.fs = 0
		self.num_channels = 0
		self.channel_names = []
		self.data = []
		self.t = []
		self.epochs = 0
		self.tags = []

	@classmethod
	def register_plugin(cls):
		reload(sys.modules['Sappy.SignalManager'])
		return sys.modules['Sappy.SignalManager'].SignalManager

	def __repr__(self):
		return 'Plugin'
