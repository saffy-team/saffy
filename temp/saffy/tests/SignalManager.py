import unittest

from .. import PluginManager
from .. import SignalManager


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


if __name__ == '__main__':
    unittest.main()
