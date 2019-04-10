import numpy as np
import scipy.io as io


def eeglab(filepath):
	eeg = io.loadmat(f'{filepath}.set')['EEG']

	fdt = np.fromfile(f'./{filepath}.fdt', 'float32')

	num_channels = eeg['nbchan'][0][0][0][0]
	epochs = eeg['epoch'][0][0].shape[1]
	pnts = eeg['pnts'][0][0][0][0]
	srate = eeg['srate'][0][0][0][0]
	channel_names = list(map(lambda x: x[0][0], eeg['chanlocs'][0][0][0]))
	tags = list(set(map(lambda x: int(x[0][0][0] % pnts), eeg['event'][0][0][0])))
	t = eeg['times'][0][0][0] / 1000

	data = np.reshape(fdt, (pnts, epochs, num_channels))
	data = np.moveaxis(data, 0, -1)

	data = {
		'fs': srate,
		'num_channels': num_channels,
		'channel_names': channel_names,
		'epochs': epochs,
		'tags': tags,
		'data': data,
		't': t
	}

	return data
