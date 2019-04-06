import saffy

RAW_EEG = saffy.SignalManager(filename="path/to/file")

EEG = RAW_EEG\
	.extract_channels(['C3', 'C4', 'trig'])\
	.set_tags_from_channel('trig')\
	.remove_channel('trig')\
	.butter_highpass_filter(cutoff=1, order=2)\
	.cheb2_notch_filter(cutoff=50, order=1, rs=3, width=0.3, btype='bandstop')

PRE_EEG = EEG\
	.copy('pre')\
	.set_epochs_from_tags(-4, -2)\
	.welch_mean_spectrum()

POST_EEG = EEG\
	.copy('post')\
	.set_epochs_from_tags(0.5, 2.5)\
	.welch_mean_spectrum()
