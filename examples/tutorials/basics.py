import numpy as np
import saffy


def sine_wave_generator(frequency, phase, length, sampling_rate):
	data = {
		'fs': sampling_rate,
		'num_channels': 1,
		'channel_names': ['sine'],
		'epochs': 1
	}

	data['t'] = np.arange(0, length, 1 / data['fs'])
	data['data'] = np.sin(2 * np.pi * frequency * data['t'] + phase)
	data['data'] = np.reshape(data['data'], (data['epochs'], data['num_channels'], *data['data'].shape))

	return data


sig = saffy.SignalManager(generator=sine_wave_generator(10, 0, 1, 128))\
	.graphics_time_plot()\
	.fourier_transform()\
	.graphics_spectrum_plot()
