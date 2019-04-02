## Hilbert

The plugin for calculating Hilbert Transform

### hilbert: dict
The data structure which stores all the calculated values, like the power, amplitude, phase.
```python
    "data": hilbert transform,
    "amplitude": the instantaneous amplitude,
    "power": the instantaneous power,
    "phase": the instantaneous phase
```

### hilbert_transform(self, phase_freq=0)
Calculates the Hilbert Transform. The `phase_freq` is used to determine for which frequency is the instantaneous phase 
to be calculated. It populates all the values of the `hilbert` dictionary.

### hilbert_subtract_base(self, low, high)
Subtracts the mean of the power between the low high params from the power.

### hilbert_mean_power(self)
Calculates the mean power across epochs.