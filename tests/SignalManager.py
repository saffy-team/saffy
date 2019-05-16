import unittest
import warnings
import numpy as np

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

        sig.remove_channels(['sine'])

        self.assertEqual(["remove_channels(['sine'], )"], sig.history)

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

    def samples_property_test(self):
        t = 20

        data = {
            'fs': 512,
            'num_channels': 1,
            'channel_names': ['sine1'],
            'epochs': 1
        }

        sig = SignalManager(T=t, generator=sine_wave(data=data))

        self.assertEqual(sig.samples, data['fs'] * t)

        t = 1
        sig.extract_time_range(0, t)
        self.assertEqual(sig.samples, data['fs'] * t)

    def set_tags_from_channel_test(self):
        data = {
            'fs': 512,
            'num_channels': 1,
            'channel_names': ['sine'],
            'epochs': 1
        }
        t = 1
        freq = 10

        sig = SignalManager(generator=sine_wave(freq=freq, T=t, data=data))
        sig.set_tags_from_channel('sine')

        self.assertEqual(len(sig.tags), t*freq)

    def set_epochs_from_tags_test(self):
        data = {
            'fs': 512,
            'num_channels': 1,
            'channel_names': ['sine'],
            'epochs': 1
        }
        t = 1
        freq = 10

        sig = SignalManager(generator=sine_wave(freq=freq, T=t, data=data))
        sig.set_tags_from_channel('sine')
        sig.set_epochs_from_tags(-.01, .01)

        self.assertEqual(len(sig.tags), 0)
        self.assertEqual(sig.epochs, t*freq)

        with warnings.catch_warnings(record=True) as w:
            sig = SignalManager(generator=sine_wave(freq=freq, T=t, data=data))
            sig.set_tags_from_channel('sine')
            sig.set_epochs_from_tags(-.1, .1)

            self.assertEqual(len(w), 1)

    def call_test(self):
        sig = SignalManager(generator=sine_wave())

        def divide(self):
            self.data /= 10

        before = np.max(sig.data)
        sig.call(divide)
        after = np.max(sig.data)

        self.assertEqual(after, before / 10)

    def copy_test(self):
        sig1 = SignalManager(generator=sine_wave())
        sig2 = sig1.copy()

        self.assertTrue(np.equal(sig1.data, sig2.data).all())

        sig1.data = sig1.data / 10

        self.assertFalse(np.equal(sig1.data, sig2.data).all())


if __name__ == '__main__':
    unittest.main()
