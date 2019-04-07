## Create Custom Plugin

There will most definitely be a case, where you will want to create a custom plugin.

The proposed convention for plugin development is the following.
All data that is to be stored extra, should be stored in the form of a dictionary assigned to a variable of the same name
as the plugin.

Plugin functions should be preceded by the plugin name. 

### Class Implementation

```python
import saffy

class CustomPlugin(saffy.PluginManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.custom = {
            'param': 'some value'
        }
        
    def custom_function(self):
        # do something
        pass
        
saffy.SignalManager.register_plugin(CustomPlugin)

sig = saffy.SignalManager(generator=signal_data)

sig.custom_function()
```

### Functional Plugin

In other cases when it is only one function you want to use you can use the `call` function

```python
sig = saffy.SignalManager(generator=signal_data)

def custom_function(self):
    print(self.data)

sig.call(custom_function)
```
