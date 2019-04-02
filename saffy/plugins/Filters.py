from scipy.signal import butter, filtfilt, iirnotch, cheby2

from .PluginManager import PluginManager


class FiltersPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def _butter_lowpass(self, cutoff, order=5):
		nyq = 0.5 * self.fs
		normal_cutoff = cutoff / nyq
		b, a = butter(order, normal_cutoff, btype='low', analog=False)
		return b, a

	def butter_lowpass_filter(self, cutoff, order=5, method=None):
		b, a = self._butter_lowpass(cutoff, order=order)

		if method:
			self.data = method(b, a, self.data)
		else:
			self.data = filtfilt(b, a, self.data)

	def _cheb2_notch(
			self,
			cutoff,
			order=5,
			rs=3,
			width=.1,
			btype='bandstop'
	):
		nq = self.fs / 2

		Wn_min, Wn_max = (cutoff - width) / nq, (cutoff + width) / nq
		Wn = [Wn_min, Wn_max]

		b, a = cheby2(
			N=order,
			rs=rs,
			Wn=Wn,
			btype=btype,
			analog=False,
			output='ba'
		)

		return b, a

	def cheb2_notch_filter(
			self,
			cutoff,
			order=5,
			rs=3,
			width=.1,
			method=None,
			btype='bandstop'
	):
		b, a = self._cheb2_notch(cutoff, order, rs, width, btype=btype)

		if method:
			self.data = method(b, a, self.data)
		else:
			self.data = filtfilt(b, a, self.data)

	def _butter_highpass(
			self,
			cutoff,
			order=5
	):
		nyq = 0.5 * self.fs
		normal_cutoff = cutoff / nyq
		b, a = butter(order, normal_cutoff, btype='high', analog=False)
		return b, a

	def butter_highpass_filter(
			self,
			cutoff,
			order=5,
			method=None
	):
		b, a = self._butter_highpass(cutoff, order=order)

		if method:
			self.data = method(b, a, self.data)
		else:
			self.data = filtfilt(b, a, self.data)

	def _butter_bandpass(lowcut, highcut, fs, order=5):
		nyq = 0.5 * fs
		low = lowcut / nyq
		high = highcut / nyq
		b, a = butter(order, [low, high], btype='band')
		return b, a

	def butter_bandpass_filter(data, lowcut, highcut, fs, order=5, method=None):
		b, a = _butter_bandpass(lowcut, highcut, fs, order=order)
		if method:
			y = method(b, a, data)
		else:
			y = filtfilt(b, a, data)
		return y

	def __str__(self):
		return 'Filters'

	def __repr__(self):
		return 'Filters'
