import unittest

from .. import PluginManager
from .. import SignalManager

from .mocks import sine_wave


class TestSignalManager(unittest.TestCase):
    @staticmethod
    def smoke_test():
        print('smoke_test')
        SignalManager()

    def register_plugin_test(self):
        print('custom_plugin_test')

        class TestPlugin(PluginManager):
            def __init__(self):
                super().__init__()
                self.custom = []

            def custom_function(self):
                return self.custom

        SignalManager.register_plugin(TestPlugin)

        self.assertTrue(TestPlugin in SignalManager.__bases__,
                        'TestPlugin should be a subclass of the PluginManager')

        sig = SignalManager()
        self.assertEqual([], sig.custom_function())

    def add_history_test(self):
        print('add_history_test')

        sig = SignalManager(generator=sine_wave())

        sig.remove_channel('sine', )

        self.assertEqual(["remove_channel('sine', )"], sig.history)


if __name__ == '__main__':
    unittest.main()
