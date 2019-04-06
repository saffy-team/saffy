## Tutorial: Basics
An introductory tutorial to get you familiar with how easy it is to do analysis with saffy.

#### Setup

First we need to install the package using pip

`pip3 install saffy`

#### Simple Sine Generator.
Open up your favorite IDE and let's get going. We will first start off with writing a simple sine wave generator.
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
Let's add the sine function itself.

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
    
    return data
```
And this set's us up. We first created the time vector and then from the definition of a sine wave we created,
the data variable. Now the next step would be to load the signal into the [SignalManager](/SignalManager).

```python
import saffy

sig = saffy.SignalManager(generator=sine_wave_generator(10, 0, 1, 128))
```
We now have a sine signal of 10 Hz frequency, 0 phase shift, 1 second long and a sampling rate of 128.
Let's plot the signal and see.

```python
sig.graphics_time_plot()
```

![basic_sine_wave](https://res.cloudinary.com/ppierzc/image/upload/v1554563066/basics_ke2rbs.png)

Now let's calculate the real Fourier transform and plot the spectrum.

```python
sig.fourier_transform()
sig.graphics_spectrum_plot()
```

![basic_sine_spectrum](https://res.cloudinary.com/ppierzc/image/upload/v1554563611/spectrum_wmnunw.png)

And that is it you have done some basic Fourier signal analysis.
