import unittest

from saffy.generators.simple_sine import simple_sine


class TestSimpleSineGenerator(unittest.TestCase):
	@staticmethod
	def smoke_test():
		simple_sine()

	def return_structure_test(self):
		generator = simple_sine()
		self.assertEqual(list(generator.keys()), ['fs', 'num_channels', 'channel_names', 'epochs', 'data', 't', 'tags'])

	def data_param_test(self):
		generator = simple_sine(data={'fs': 100})
		self.assertEqual(generator['fs'], 100)


if __name__ == '__main__':
	unittest.main()
