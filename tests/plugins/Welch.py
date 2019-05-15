import unittest
from saffy import SignalManager
from ..mocks import sine_wave
import scipy.signal as ss
import numpy as np


class TestWelchPlugin(unittest.TestCase):
	def welch_spectrum_test(self):
		freq = 50
		phase = np.pi/2

		generator = sine_wave(freq=freq, phase=phase)
		sig = SignalManager(generator=generator)

		sig.welch_spectrum()

		freq, spec = ss.welch(generator['data'], generator['fs'])

		self.assertTrue(np.allclose(sig.spectrum, spec))
		self.assertTrue(np.allclose(sig.spectrum_freqs, freq))

	def welch_mean_spectrum_test(self):
		freq = 50
		phase = np.pi / 2

		data = {
			'fs': 512,
			'num_channels': 1,
			'channel_names': ['sine'],
			'epochs': 10
		}

		generator = sine_wave(freq=freq, phase=phase, data=data)
		sig = SignalManager(generator=generator)

		sig.welch_mean_spectrum()

		freq, spec = ss.welch(generator['data'], generator['fs'])

		mean_spec = np.mean(spec, 0)

		self.assertTrue(np.allclose(sig.spectrum, mean_spec))


if __name__ == '__main__':
	unittest.main()
