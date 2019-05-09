import unittest

from saffy import PluginManager
from saffy import SignalManager

from .mocks import sine_wave


class TestSignalManager(unittest.TestCase):
    @staticmethod
    def smoke_test():
        SignalManager(sine_wave())

    def register_plugin_test(self):
        class TestPlugin(PluginManager):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.custom = []

            def custom_function(self):
                return self.custom

        SignalManager.register_plugin(TestPlugin)

        self.assertTrue(TestPlugin in SignalManager.__bases__,
                        'TestPlugin should be a subclass of the PluginManager')

        sig = SignalManager(sine_wave())
        self.assertEqual([], sig.custom_function())

    def duplicate_register_plugin_test(self):
        class TestPlugin(PluginManager):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.custom = []

            def custom_function(self):
                return self.custom

        length_before = len(SignalManager.__bases__)
        SignalManager.register_plugin(TestPlugin)
        SignalManager.register_plugin(TestPlugin)
        length_after = len(SignalManager.__bases__)

        self.assertTrue(length_after - length_before == 1,
                        'Should not create duplicate plugins')

        sig = SignalManager(sine_wave())
        self.assertEqual([], sig.custom_function())

    def add_history_test(self):

        sig = SignalManager(sine_wave())

        sig.remove_channels('sine')

        self.assertEqual(["remove_channels('sine', )"], sig.history)

    def extract_channel_test(self):
        data = {
            'fs': 512,
            'num_channels': 3,
            'channel_names': ['sine1', 'sine2', 'sine3'],
            'epochs': 1
        }

        sig = SignalManager(generator=sine_wave(data=data))

        sig.extract_channels(['sine2', 'sine3'])

        self.assertEqual(sig.num_channels, 2)
        self.assertEqual(sig.channel_names, ['sine2', 'sine3'])
        self.assertEqual(sig.data.shape, (1, 2, 10240))

    def extract_time_range_test(self):
        data = {
            'fs': 512,
            'num_channels': 1,
            'channel_names': ['sine1'],
            'epochs': 1
        }

        sig = SignalManager(sine_wave(data=data))

        sig.extract_time_range(0, 1)

        self.assertEqual(sig.data.shape, (1, 1, 512))

    @staticmethod
    def chaining_test():
        data = {
            'fs': 512,
            'num_channels': 1,
            'channel_names': ['sine1'],
            'epochs': 1
        }

        sig = SignalManager(generator=sine_wave(data=data))

        sig.extract_time_range(0, 2)\
            .extract_time_range(0, 1)


if __name__ == '__main__':
    unittest.main()
