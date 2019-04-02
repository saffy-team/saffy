import scipy.signal as ss
import numpy as np

from .PluginManager import PluginManager


class WelchPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def welch_spectrum(self):
		spectrum_freqs, spectrum = ss.welch(self.data, self.fs)

		self.spectrum = spectrum
		self.spectrum_freqs = spectrum_freqs

	def welch_mean_spectrum(self):
		spectrum_freqs, spectrum = ss.welch(self.data, self.fs)

		self.spectrum = spectrum
		self.spectrum_freqs = spectrum_freqs

		self.spectrum = np.mean(self.spectrum, axis=0)
		self.spectrum = np.reshape(self.spectrum, (1, *self.spectrum.shape))

	def __str__(self):
		return 'Welch'

	def __repr__(self):
		return 'Welch'
