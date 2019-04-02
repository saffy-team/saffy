## Welch

Is one of the methods for calculating the spectral density.

### welch_spectrum(self)
Calculates the Welch spectrum.
Adds the values to `self.spectrum` and `self.spectrum_freqs`.

### welch_mean_spectrum(self)
Calculates the Welch spectrum and then takes the mean value across epochs.
Adds the values to `self.spectrum` and `self.spectrum_freqs`