import scipy.signal as ss
import numpy as np

from .PluginManager import PluginManager


class HilbertPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.hilbert = {}

	def hilbert_transform(self, phase_freq=0):
		self.hilbert['data'] = ss.hilbert(self.data)

		self.hilbert['amplitude'] = np.abs(self.hilbert['data'])
		self.hilbert['power'] = self.hilbert['amplitude']

		self.hilbert['phase'] = np.unwrap(np.angle(self.hilbert['data']))
		# Składa sie z czynników:
		# - pi/2 - pochodzące od przesunięcia sin/cos
		# - instantaneous_phase z sygnału
		# - w0 * t, gdzie w0 to 2 pi f (częstość dla, której sprawdzamy fazę)
		self.hilbert['phase'] = np.pi / 2 + self.hilbert[
			'phase'] - 2 * np.pi * phase_freq * self.t  # Wynika ze wzoru z brain.fuw.edu.pl
		self.hilbert['phase'] /= np.pi

	def hilbert_subtract_base(self, low, high):
		low_samp = np.where(self.t == low)[0][0]
		high_samp = np.where(self.t == high)[0][0]

		for epoch in range(self.epochs):
			for channel in range(self.num_channels):
				self.hilbert['power'][epoch, channel] -= np.mean(
					self.hilbert['power'][epoch, channel, low_samp: high_samp]
				)

	def hilbert_mean_power(self):
		self.hilbert['power'] = np.mean(self.hilbert['power'], axis=0)
		self.hilbert['power'] = np.reshape(self.hilbert['power'], (1, *self.hilbert['power'].shape))

	def __str__(self):
		return 'Hilbert'

	def __repr__(self):
		return 'Hilbert'
