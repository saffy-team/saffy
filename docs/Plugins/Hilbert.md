## Hilbert

The plugin for calculating Hilbert Transform

### hilbert: dict
The data structure which stores all the calculated values, like the power, amplitude, phase.

| field | description |
|--------|------|
| data   | hilbert transform  |
| amplitude | the instantaneous amplitude |
| power | the instantaneous power |
| phase | the instantaneous phase |

### hilbert_transform(self, phase_freq=0)
Calculates the Hilbert Transform. The `phase_freq` is used to determine for which frequency is the instantaneous phase 
to be calculated. It populates all the values of the `hilbert` dictionary.

##### Params
- **phase_freq**: when calculating the instantaneous phase, we need to know for which frequency to calculate it. 

### hilbert_subtract_base(self, low, high)
Calculates the mean power from the power between `low` and `high`, then subtracts the mean value from the entire power vector.
Calculates for each channel separately.

##### Params
- **low**: the start time (in seconds) from where to calculate the mean.
- **high**: the end time (in seconds) from where to calculate the mean.

### hilbert_mean_power(self)
Calculates the mean power across epochs.