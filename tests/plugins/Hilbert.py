import unittest
import numpy as np

from saffy import SignalManager
from ..mocks import sine_wave


class TestFourierPlugin(unittest.TestCase):
	@staticmethod
	def hilbert_transform_test():
		freq = 50
		phase = np.pi/2

		sig = SignalManager(generator=sine_wave(freq=freq, phase=phase))

		sig.hilbert_transform()

	@staticmethod
	def hilbert_mean_power_test():
		freq = 50
		phase = np.pi/2

		sig = SignalManager(generator=sine_wave(freq=freq, phase=phase))

		sig.hilbert_transform()\
			.hilbert_mean_power()

	def graphics_time_plot_test(self):
		freq = 10
		phase = np.pi/2

		data = {
			'fs': 512,
			'num_channels': 2,
			'channel_names': ['sine1', 'sine2'],
			'epochs': 2
		}

		sig = SignalManager(generator=sine_wave(freq=freq, phase=phase, data=data))

		sig.hilbert_transform() \
			.hilbert_mean_power()

		sig.graphics_set_style('paper')\
			.hilbert_power_plot()


if __name__ == '__main__':
	unittest.main()
