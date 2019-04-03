import saffy

EEG = saffy.SignalManager(filename="path/to/file")

EEG.extract_channels(['C3', 'C4', 'trig'])

EEG.set_tags_from_channel('trig')

EEG.remove_channel('trig')

EEG.butter_highpass_filter(cutoff=1, order=2)
EEG.cheb2_notch_filter(cutoff=50, order=1, rs=3, width=0.3, btype='bandstop')

PRE_EEG = EEG.copy('pre')
PRE_EEG.set_epochs_from_tags(-4, -2)

PRE_EEG.welch_mean_spectrum()

POST_EEG = EEG.copy('post')
POST_EEG.set_epochs_from_tags(0.5, 2.5)

POST_EEG.welch_mean_spectrum()