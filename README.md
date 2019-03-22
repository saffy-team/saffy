# Sappy
Signal Analysis &amp; Processing in Python

## Usage
```python
import Sappy
sig = Sappy.SignalManager(generator=signal_data)
```

#### Basic SignalManager instance structure
| field | description |
|--------|------|
| fs   | sampling frequency  |
| num_channels | number of channels |
| channel_names | name for each channel |
| data | the signal in the structure of (epoch x channel x signal) |
| t | time vector |
| epochs | number of epochs |
| tags | position of tags in signal |

## Plugins
Additional functions are added by creating a plugin.
Some plugins are provided out of the box, however if you might want to add some custom.

```python
import Sappy

class CustomPlugin(Sappy.PluginManager):
    def __init__(self):
        super().__init__()
        self.custom_param = 'some value'
        
    def custom_function(self):
        # do something
        pass

sig = Sappy.SignalManager(generator=signal_data)

sig.custom_function()
```
