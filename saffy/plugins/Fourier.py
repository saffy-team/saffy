import numpy as np

from .PluginManager import PluginManager


class FourierPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def fourier_transform(self):
		transform = np.fft.rfft(self.data)

		self.spectrum = abs(transform) ** 2
		self.phase = np.angle(transform) + np.pi / 2

		self.spectrum_freqs = np.fft.rfftfreq(self.data.shape[2], 1/self.fs)
