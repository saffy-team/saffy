import numpy as np


def sin(t, f, p):
	return np.sin(2 * np.pi * f * t + p)


def simple_sine(freq=10, phase=0, length=20, sampling_frequency=512, data=None):
	if not data:
		data = {
			'fs': sampling_frequency,
			'num_channels': 1,
			'channel_names': ['sine'],
			'epochs': 1
		}

	t = np.arange(0, length, 1 / data['fs'])

	data['data'] = np.zeros((data['epochs'], data['num_channels'], len(t)))

	for epoch in range(data['epochs']):
		for channel in range(data['num_channels']):
			data['data'][epoch][channel] += sin(t, freq, phase)

	data['t'] = t
	data['tags'] = []

	return data
