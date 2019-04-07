import unittest
import numpy as np

from saffy import SignalManager
from ..mocks import sine_wave


class TestFourierPlugin(unittest.TestCase):
	def fourier_transform_test(self):
		freq = 50
		phase = np.pi/2

		sig = SignalManager(generator=sine_wave(freq=freq, phase=phase))

		sig.fourier_transform()

		max_freq_idx = np.where(sig.spectrum == np.max(sig.spectrum))[2][0]

		self.assertAlmostEqual(freq, sig.spectrum_freqs[max_freq_idx])
		self.assertAlmostEqual(phase, sig.phase[:, :, max_freq_idx][0][0])


if __name__ == '__main__':
	unittest.main()
