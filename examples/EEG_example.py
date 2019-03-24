import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import Sappy


sns.set()
sns.set_context("talk", font_scale=1.4)


def sin(t, f):
	return np.sin(2 * np.pi * f * t)


def noise(t, loc=0, scale=1):
	return np.random.normal(loc=loc, scale=scale, size=len(t))


def generate_signal():
	data = {
		'fs': 512,
		'num_channels': 3,
		'channel_names': ['C3', 'C4', 'd1'],
		'epochs': 1
	}

	T = 20
	t = np.arange(0, T, 1 / data['fs'])

	mu_freq = 10
	beta_freq = 23
	net_freq = 50

	data['data'] = np.zeros((data['epochs'], data['num_channels'], len(t)))

	for epoch in range(data['epochs']):
		data['data'][epoch][0] += (0.1 * t + 0.1) * sin(t, mu_freq)
		data['data'][epoch][0] += (0.1 * t + 0.1) * sin(t, beta_freq)
		data['data'][epoch][0] += sin(t, net_freq)
		data['data'][epoch][0] += 0.3 * noise(t)

		data['data'][epoch][1] += (0.1 * t + 0.1) * sin(t, mu_freq)
		data['data'][epoch][1] += (0.1 * t + 0.1) * sin(t, beta_freq)
		data['data'][epoch][1] += sin(t, net_freq)
		data['data'][epoch][1] += 0.3 * noise(t)

		data['data'][epoch][2][::5 * data['fs']] = 1
		data['data'][epoch][2][0] = 0

	data['t'] = t
	data['tags'] = []

	return data


EEG = Sappy.SignalManager(generator=generate_signal())

EEG.set_tags_from_channel('d1')
EEG.remove_channel('d1')

PRE_EEG = EEG.copy('pre')
PRE_EEG.set_epochs_from_tags(-4, -2)

PRE_EEG.welch_spectrum()
PRE_EEG.spectrum = np.mean(PRE_EEG.spectrum, axis=0)
PRE_EEG.spectrum = np.reshape(PRE_EEG.spectrum, (1, *PRE_EEG.spectrum.shape))

POST_EEG = EEG.copy('post')
POST_EEG.set_epochs_from_tags(0.5, 2.5)

POST_EEG.welch_spectrum()
POST_EEG.spectrum = np.mean(POST_EEG.spectrum, axis=0)
POST_EEG.spectrum = np.reshape(POST_EEG.spectrum, (1, *POST_EEG.spectrum.shape))

fig, ax = plt.subplots(
	nrows=max([PRE_EEG.num_channels, POST_EEG.num_channels]),
	ncols=1,
	sharex=True,
	sharey=True,
	figsize=(10, 10)
)

PRE_EEG.spectrum_plot(
	fig,
	ax,
	'Change',
	label='Pre'
)

POST_EEG.spectrum_plot(
	fig,
	ax,
	color='#0000ff',
	label='Post'
)

for a in ax:
	a.legend()

plt.show()
plt.close()
