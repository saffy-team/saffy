from scipy.signal import butter, filtfilt, cheby2, freqz
import numpy as np
import matplotlib.pyplot as plt

from .PluginManager import PluginManager


class FiltersPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.filters = {
			'a': 0,
			'b': 0,
			'characteristics': {
				'f': [],
				'abs_transmittance': [],
				'phase_latency': [],
				'group_latency': [],
				'impulse_response': np.array([]),
				'step_response': np.array([])
			}
		}

	def filter_characteristics(self):
		t = np.arange(-1, 1, 1/self.fs)
		f = np.arange(0.01, self.fs / 2, 0.01)
		w = 2 * np.pi * f / self.fs
		w, transmittance = freqz(self.filters['b'], self.filters['a'], w)

		self.filters['characteristics']['f'] = f
		self.filters['characteristics']['abs_transmittance'] = np.abs(transmittance)

		phase = np.unwrap(np.angle(transmittance))
		self.filters['characteristics']['phase_latency'] = - phase / w

		df = np.diff(phase)
		idx, = np.where(np.abs(df - np.pi) < 0.05)
		df[idx] = (df[idx + 1] + df[idx - 1]) / 2
		self.filters['characteristics']['group_latency'] = - df / np.diff(w)

		impulse = np.zeros(len(t))
		impulse[len(t) // 2] = 1
		self.filters['characteristics']['impulse_response'] = filtfilt(self.filters['b'], self.filters['a'], impulse)

		step = np.zeros(len(t))
		step[len(t) // 2:] = 1
		self.filters['characteristics']['step_response'] = filtfilt(self.filters['b'], self.filters['a'], step)

		fig = plt.figure(figsize=(10, 10))
		plt.subplot(3, 2, 1)
		plt.title('Absolute Transmittance')
		plt.plot(f, 20 * np.log10(self.filters['characteristics']['abs_transmittance']))
		plt.ylabel('[dB]')

		plt.subplot(3, 2, 2)
		plt.title('Impulse Response')
		plt.plot(t, impulse)
		plt.plot(t, self.filters['characteristics']['impulse_response'])
		plt.xlim([-1 / 2, 1])

		plt.subplot(3, 2, 3)
		plt.title('Phase Latency')
		plt.plot(f, self.filters['characteristics']['phase_latency'])
		plt.ylabel('Samples')

		plt.subplot(3, 2, 4)
		plt.title('Step Response')
		plt.plot(t, step)
		plt.plot(t, self.filters['characteristics']['step_response'])
		plt.xlim([-1 / 2, 1])
		plt.xlabel('Time [s]')

		plt.subplot(3, 2, 5)
		plt.title('Group Latency')
		plt.plot(f[:-1], self.filters['characteristics']['group_latency'])
		plt.ylabel('Samples')
		plt.xlabel('Frequency [Hz]')
		plt.ylim([0, np.max(self.filters['characteristics']['group_latency']) + 1])

		fig.subplots_adjust(hspace=.5)
		plt.show()

	def _butter_lowpass(
			self,
			cutoff,
			*,
			order=5
	):
		nyq = 0.5 * self.fs
		normal_cutoff = cutoff / nyq
		self.filters['b'], self.filters['a'] = butter(order, normal_cutoff, btype='low', analog=False)

	def butter_lowpass_filter(
			self,
			cutoff,
			*,
			order=5,
			method=None
	):

		self._butter_lowpass(cutoff, order=order)

		if method:
			self.data = method(self.filters['b'], self.filters['a'], self.data)
		else:
			self.data = filtfilt(self.filters['b'], self.filters['a'], self.data)

	def _cheb2_notch(
			self,
			cutoff,
			*,
			order=5,
			rs=3,
			width=.1,
			btype='bandstop'
	):

		nq = 0.5 * self.fs
		Wn_min, Wn_max = (cutoff - width) / nq, (cutoff + width) / nq
		Wn = [Wn_min, Wn_max]

		self.filters['b'], self.filters['a'] = cheby2(
			N=order,
			rs=rs,
			Wn=Wn,
			btype=btype,
			analog=False,
			output='ba'
		)

	def cheb2_notch_filter(
			self,
			cutoff,
			*,
			order=5,
			rs=3,
			width=.1,
			method=None,
			btype='bandstop'
	):

		self._cheb2_notch(cutoff, order=order, rs=rs, width=width,\
								btype=btype)

		if method:
			self.data = method(self.filters['b'], self.filters['a'], self.data)
		else:
			self.data = filtfilt(self.filters['b'], self.filters['a'], self.data)

	def _butter_highpass(
			self,
			cutoff,
			*,
			order=5
	):

		nyq = 0.5 * self.fs
		normal_cutoff = cutoff / nyq
		self.filters['b'], self.filters['a'] = butter(order, normal_cutoff, btype='high', analog=False)

	def butter_highpass_filter(
			self,
			cutoff,
			*,
			order=5,
			method=None
	):

		self._butter_highpass(cutoff, order=order)

		if method:
			self.data = method(self.filters['b'], self.filters['a'], self.data)
		else:
			self.data = filtfilt(self.filters['b'], self.filters['a'], self.data)

	def _butter_bandpass(
			self,
			lowcut,
			highcut,
			*,
			order=5
	):

		nyq = 0.5 * self.fs
		low = lowcut / nyq
		high = highcut / nyq
		self.filters['b'], self.filters['a'] = butter(order, [low, high], btype='band')

	def butter_bandpass_filter(
			self,
			lowcut,
			highcut,
			*,
			order=5,
			method=None
	):

		self._butter_bandpass(lowcut, highcut, order=order)

		if method:
			self.data = method(self.filters['b'], self.filters['a'], self.data)
		else:
			self.data = filtfilt(self.filters['b'], self.filters['a'], self.data)
