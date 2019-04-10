import numpy as np
from obci_readmanager.signal_processing.read_manager import ReadManager


def svarog(filename):
	data = {}

	mgr = ReadManager(
		"%s.xml" %
		filename,
		"%s.raw" %
		filename,
		"%s.tag" %
		filename)

	data['fs'] = int(float(mgr.get_param("sampling_frequency")))

	data['num_channels'] = int(mgr.get_param("number_of_channels"))
	data['channel_names'] = mgr.get_param("channels_names")

	data['data'] = mgr.get_microvolt_samples()
	data['data'] = np.reshape(data['data'], (1, *data['data'].shape))

	data['t'] = np.arange(data['data'].shape[1]) / data['fs']

	data['epochs'] = 1
	data['tags'] = []

	return data
