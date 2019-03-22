import scipy.signal as ss
import numpy as np

from .PluginManager import PluginManager


class HilbertPlugin(PluginManager):
	def __init__(self):
		super().__init__()
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

	def __str__(self):
		return 'Hilbert'

	def __repr__(self):
		return 'Hilbert'
