import unittest
import numpy as np

from saffy import SignalManager
from ..mocks import sine_wave

import matplotlib.pyplot as plt


class TestGraphicsPlugin(unittest.TestCase):
	@staticmethod
	def graphics_set_style_test():
		freq = 10
		phase = np.pi / 2

		data = {
			'fs': 512,
			'num_channels': 2,
			'channel_names': ['sine1', 'sine2'],
			'epochs': 2
		}

		sig = SignalManager(generator=sine_wave(freq=freq, phase=phase, data=data))
		sig.graphics_set_style('paper')

		sig.graphics_time_plot()

	@staticmethod
	def graphics_time_plot_test():
		freq = 10
		phase = np.pi/2

		data = {
			'fs': 512,
			'num_channels': 2,
			'channel_names': ['sine1', 'sine2'],
			'epochs': 2
		}

		sig = SignalManager(generator=sine_wave(freq=freq, phase=phase, data=data))

		sig.graphics_time_plot()

		fig, ax = plt.subplots(
			nrows=sig.num_channels,
			ncols=1,
			figsize=(10, 10)
		)

		sig.graphics_time_plot(fig, ax)

		plt.show()


if __name__ == '__main__':
	unittest.main()
