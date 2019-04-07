## Tutorial: Custom Generators

In the last tutorial we used a generator to provide us some data to work with. Now we will look at what it takes
to create a custom generator.

#### Simple Sine Generator.

We will first start off with writing a simple sine wave generator.
We will build a single epoch and single channeled sine wave.

```python
def sine_wave_generator(frequency, phase, length, sampling_rate):
    data = {
			'fs': sampling_rate,
			'num_channels': 1,
			'channel_names': ['sine'],
			'epochs': 1
		}
```

We first need to define our data holding dictionary. It is the constructing element of our signal.
Let's add the sine function itself. The `data` dictionary can hold any of the values specified in the [SignalManger](/SignalManager)
documentation.

The next step is to add the signal itself. This is done in the classical way like you would normally create a sine wave.

```python
import numpy as np

def sine_wave_generator(frequency, phase, length, sampling_rate):
    data = {
			'fs': sampling_rate,
			'num_channels': 1,
			'channel_names': ['sine'],
			'epochs': 1
		}
	
    data['t'] = np.arange(0, length, 1 / data['fs'])
    data['data'] = np.sin(2 * np.pi * frequency * data['t'] + phase)
    data['data'] = np.reshape(data['data'], (data['epochs'], data['num_channels'], *data['data'].shape))
    
    return data
```

And this set's us up. We first created the time vector and then from the definition of a sine wave we created,
the data variable.
We need to reshape the data however to account for the number of epochs and channels. 
We have to then return it so that the SignalManager will be able to read the specifications of our signal.

With this principle you can load in any format of data you will need.
