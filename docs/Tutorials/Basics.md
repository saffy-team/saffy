## Tutorial: Basics

An introductory tutorial to get you familiar with how easy it is to do analysis with saffy.

#### Setup

First we need to install the package using pip

`pip3 install saffy`

#### Loading some data

We first need to generate our data. For that we will use the built in generator [simple_sine_generator](<>). How generators
work will be discussed in a later tutorial for now let's concentrate on the latter parts.

```python
import saffy

sig = saffy.SignalManager(generator=saffy.generators.simple_sine_generator(10, 0, 1, 128))
```

We now have a sine signal of 10 Hz frequency, 0 phase shift, 1 second long and a sampling rate of 128.
We can now easily plot the signal and see what was loaded in.

#### Basic time plotting

```python
sig.graphics_time_plot()
```

![basic_sine_wave](https://res.cloudinary.com/ppierzc/image/upload/v1554563066/basics_ke2rbs.png)

#### Basic spectral plotting

Now let's calculate the real Fourier transform and plot the spectrum.

```python
sig.fourier_transform()
sig.graphics_spectrum_plot()
```

![basic_sine_spectrum](https://res.cloudinary.com/ppierzc/image/upload/v1554563611/spectrum_wmnunw.png)

And that is it you have done some basic Fourier signal analysis.
