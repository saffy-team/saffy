import numpy as np


def ndarray(array, data={}):
	data = {
		'fs': 512,
		'num_channels': array.shape[1],
		'channel_names': ['array'],
		'epochs': array.shape[0],
		'tags': [],
		**data
	}

	t = np.arange(0, array.shape[2], 1 / data['fs'])

	data['data'] = np.zeros((data['epochs'], data['num_channels'], len(t)))

	data['t'] = t

	return data
