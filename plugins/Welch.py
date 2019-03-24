import scipy.signal as ss

from .PluginManager import PluginManager


class WelchPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.welch = {}

	def welch_spectrum(self):
		spectrum_freqs, spectrum = ss.welch(self.data, self.fs)

		self.welch['spectrum'] = spectrum
		self.welch['spectrum_freqs'] = spectrum_freqs

	def __str__(self):
		return 'Welch'

	def __repr__(self):
		return 'Welch'
