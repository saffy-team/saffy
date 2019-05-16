import unittest
import numpy as np

from saffy.generators.ndarray import ndarray


class TestNdArrayGenerator(unittest.TestCase):
	@staticmethod
	def smoke_test():
		arr = np.ones((1, 1, 512))
		ndarray(arr)

	def return_structure_test(self):
		arr = np.ones((1, 1, 512))

		generator = ndarray(arr)
		self.assertEqual(set(generator.keys()), {'fs', 'num_channels', 'channel_names', 'epochs', 'data', 't', 'tags'})

	def data_param_test(self):
		arr = np.ones((1, 1, 512))

		generator = ndarray(arr, data={'fs': 100})
		self.assertEqual(generator['fs'], 100)


if __name__ == '__main__':
	unittest.main()
