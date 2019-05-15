import unittest
import numpy as np

from saffy import SignalManager
from ..mocks import sine_wave


class TestFiltersPlugin(unittest.TestCase):
	@staticmethod
	def characteristics_test():
		sig = SignalManager(generator=sine_wave())
		sig.butter_lowpass_filter(10)
		sig.filter_characteristics()

	def butter_lowpass_filter_test(self):
		filter_cutoff = 10

		sig = SignalManager(generator=sine_wave())
		sig.butter_lowpass_filter(filter_cutoff)
		sig.filter_characteristics()

		transmittance_grad = abs(np.gradient(sig.filters['characteristics']['abs_transmittance']))
		max_trans_idx = np.where(transmittance_grad == transmittance_grad.max())
		max_freq = sig.filters['characteristics']['f'][max_trans_idx]

		diff = abs(max_freq - filter_cutoff)
		self.assertLessEqual(diff, 1)

	def butter_highpass_filter_test(self):
		filter_cutoff = 10

		sig = SignalManager(generator=sine_wave())
		sig.butter_highpass_filter(filter_cutoff)
		sig.filter_characteristics()

		transmittance_grad = abs(np.gradient(sig.filters['characteristics']['abs_transmittance']))
		max_trans_idx = np.where(transmittance_grad == transmittance_grad.max())
		max_freq = sig.filters['characteristics']['f'][max_trans_idx]

		diff = abs(max_freq - filter_cutoff)
		self.assertLessEqual(diff, 1)

	def cheb2_notch_filter_test(self):
		filter_cutoff = 10

		sig = SignalManager(generator=sine_wave())
		sig.cheb2_notch_filter(filter_cutoff)
		sig.filter_characteristics()

		transmittance_grad = abs(np.gradient(sig.filters['characteristics']['abs_transmittance']))
		max_trans_idx = np.where(transmittance_grad == transmittance_grad.max())
		max_freq = sig.filters['characteristics']['f'][max_trans_idx]

		diff = abs(max_freq - filter_cutoff)
		self.assertLessEqual(diff, 1)


if __name__ == '__main__':
	unittest.main()
