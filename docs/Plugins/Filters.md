## Filters

A set of filter designs to simplify the process of filtering data.

### cheb2_notch_filter(self, cutoff, order=5, rs=3, width=.1, method=None, btype='bandstop')

A notch filter using the cheby2 filter from scipy.

##### Params

-   **cutoff**: The frequency at which the filter is to act.
-   **order**: The order of the filter
-   **rs**: Minimum attenuation required in stop band. Specified in decibels.
-   **width**: How precise is the filter supposed to be. In Hz.
-   **method**: Method of filtering. By default `scipy.signal.filtfilt` is used
-   **btype**: Type of filter `bandstop` or `bandpass`

\###butter_highpass_filter(self, cutoff, order=5, method=None)
A highpass filter filter using the butterworth filter from scipy.

##### Params

-   **cutoff**: The frequency at which the filter is to act.
-   **order**: The order of the filter
-   **method**: Method of filtering. By default `scipy.signal.filtfilt` is used

\###butter_lowpass_filter(self, cutoff, order=5, method=None)
A lowpass filter filter using the butterworth filter from scipy.

##### Params

-   **cutoff**: The frequency at which the filter is to act.
-   **order**: The order of the filter
-   **method**: Method of filtering. By default `scipy.signal.filtfilt` is used

\###butter_bandpass_filter(self, lowcut, highcut, order=5, method=None)
A bandpass filter filter using the butterworth filter from scipy.

##### Params

-   **lowcut**: The lower frequency at which the filter is to act.
-   **highcut**: The higher frequency at which the filter is to act.
-   **order**: The order of the filter
-   **method**: Method of filtering. By default `scipy.signal.filtfilt` is used
