import numpy as np

from .PluginManager import PluginManager


class FourierPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def fourier_transform(self):
		self.spectrum = np.fft.fft(self.data)
		self.spectrum_freqs = np.fft.fftfreq(self.data.shape[2], 1/self.fs)

	def __str__(self):
		return 'Fourier'

	def __repr__(self):
		return 'Fourier'
