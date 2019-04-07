## Graphics

Simple graphing functions to show the basic info about the signal

### graphics_spectrum_plot(self, fig, ax, title='', color='#ff0641', \*args, \*\*kwargs)

Plots the value of the calculated `spectrum` for each channel on a separate subplot.

##### Params

-   **fig**: A matplotlib figure object
-   **ax**: A matplotlib axis object. There must be the same amount of axies as channels.
-   **title**: The figure title
-   **color**: The color of the figure plot
-   **args & kwargs**: Other arguments to the `matplotlib.pyplot.plot` function

##### Example

```python
sig.fourier_transform()

fig, ax = plt.subplots(nrows=sig.num_channels, ncols=1)

sig.graphics_spectrum_plot(fig, ax, 'Custom Title', alpha=0.3)

plt.show()
plt.close()
```

### graphics_time_plot(self, fig, ax, title='', color='#ff0641', \*args, \*\*kwargs)

Plots the value of the `data` for each channel on a separate subplot.

##### Params

-   **fig**: A matplotlib figure object
-   **ax**: A matplotlib axis object
-   **title**: The figure title
-   **color**: The color of the figure plot
-   **args & kwargs**: Other arguments to the `matplotlib.pyplot.plot` function

##### Example

```python
fig, ax = plt.subplots(nrows=sig.num_channels, ncols=1)

sig.graphics_time_plot(fig, ax, 'Custom Title', alpha=0.3)

plt.show()
plt.close()
```
