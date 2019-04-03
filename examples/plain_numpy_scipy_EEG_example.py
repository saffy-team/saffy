import numpy as np
from obci_readmanager.signal_processing.read_manager import ReadManager
from scipy.signal import butter, filtfilt, cheby2, welch

filename = 'path/to/files'

mgr = ReadManager("%s.xml" % filename, "%s.raw" % filename, "%s.tag" % filename)

fs = int(float(mgr.get_param("sampling_frequency")))
num_channels = int(mgr.get_param("number_of_channels"))
channel_names = mgr.get_param("channels_names")

data = mgr.get_microvolt_samples()
data = np.reshape(data, (1, data.shape))

t = np.arange(data.shape[1]) / fs

channel_ids = [channel_names.index(channel_name) for channel_name in ['C3', 'C4', 'trig']]

data = data[:, channel_ids, :]
num_channels = len(channel_ids)
channel_names = list(filter(
	lambda x: channel_names.index(x) in channel_ids,
	channel_names
))

tag_channel = data[:, channel_names.index('trig')]
tag_channel = tag_channel / np.max(tag_channel)

tags = np.where(tag_channel > 0.9)[1]
tags = tags[np.concatenate(([0], np.where(np.diff(tags) > 1)[0] + 1))]

channel_id = channel_names.index('trig')
data = np.delete(data, channel_id, 1)
del channel_names[channel_id]
num_channels -= 1

nyq = 0.5 * fs
normal_cutoff = 1 / nyq
b, a = butter(2, normal_cutoff, btype='low', analog=False)
data = filtfilt(b, a, data)

nq = fs / 2
Wn_min, Wn_max = (50 - 0.3) / nq, (50 + 0.3) / nq
Wn = [Wn_min, Wn_max]
b, a = cheby2(N=order, rs=rs, Wn=Wn, btype=btype, analog=False, output='ba')
data = filtfilt(b, a, data)

pre_data = data.copy()
t = np.arange(-4, -2, 1 / fs)

low = int(-4 * fs)
high = int(-2 * fs)

length = high - low
pre_data = np.zeros((len(tags), num_channels, length))

epochs = len(tags)

for idx, tag in enumerate(tags):
	pre_data[idx] = data[:, :, tag + low: tag + high]

spectrum_freqs, spectrum = welch(data, fs)

pre_spectrum = np.mean(spectrum, axis=0)
pre_spectrum = np.reshape(spectrum, (1, *spectrum.shape))

post_data = data.copy()
t = np.arange(0.5, 2.5, 1 / fs)

low = int(0.5 * fs)
high = int(2.5 * fs)

length = high - low
post_data = np.zeros((len(tags), num_channels, length))

epochs = len(tags)

for idx, tag in enumerate(tags):
	post_data[idx] = data[:, :, tag + low: tag + high]

spectrum_freqs, spectrum = welch(data, fs)

post_spectrum = np.mean(spectrum, axis=0)
post_spectrum = np.reshape(spectrum, (1, *spectrum.shape))
