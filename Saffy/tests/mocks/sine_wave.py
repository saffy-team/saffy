import numpy as np


def sin(t, f, p):
	return np.sin(2 * np.pi * f * t + p)


def sine_wave(freq=10, phase=0, T=20):
	data = {
		'fs': 512,
		'num_channels': 1,
		'channel_names': ['sine'],
		'epochs': 1
	}

	t = np.arange(0, T, 1 / data['fs'])

	data['data'] = np.zeros((data['epochs'], data['num_channels'], len(t)))

	for epoch in range(data['epochs']):
		data['data'][epoch][0] += sin(t, freq, phase)

	data['t'] = t
	data['tags'] = []

	return data
