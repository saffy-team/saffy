
class PluginManager(object):
	def __init__(self, *args, **kwargs):
		self.fs = 0
		self.num_channels = 0
		self.channel_names = []
		self.data = []
		self.t = []
		self.epochs = 0
		self.tags = []
		self.spectrum = []
		self.spectrum_freqs = []
		self.phase = []
		self.history = []
