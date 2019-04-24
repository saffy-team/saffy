import scipy.signal as ss
import matplotlib.pyplot as plt
import numpy as np

from .PluginManager import PluginManager


class HilbertPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.hilbert = {}

	def hilbert_transform(self, phase_freq=0):
		self.hilbert['data'] = ss.hilbert(self.data)

		self.hilbert['amplitude'] = np.abs(self.hilbert['data'])
		self.hilbert['power'] = self.hilbert['amplitude']**2

		self.hilbert['phase'] = np.unwrap(np.angle(self.hilbert['data']))
		# Składa sie z czynników:
		# - pi/2 - pochodzące od przesunięcia sin/cos
		# - instantaneous_phase z sygnału
		# - w0 * t, gdzie w0 to 2 pi f (częstość dla, której sprawdzamy fazę)
		self.hilbert['phase'] = np.pi / 2 + self.hilbert[
			'phase'] - 2 * np.pi * phase_freq * self.t  # Wynika ze wzoru z brain.fuw.edu.pl
		self.hilbert['phase'] /= np.pi

		return self

	def hilbert_subtract_base(self, low, high):
		low_samp = np.where(self.t == low)[0][0]
		high_samp = np.where(self.t == high)[0][0]

		for epoch in range(self.epochs):
			for channel in range(self.num_channels):
				base = np.mean(self.hilbert['power'][epoch, channel, low_samp: high_samp])
				self.hilbert['power'][epoch, channel] -= base
				self.hilbert['power'][epoch, channel] /= base

		return self

	def hilbert_mean_power(self):
		self.hilbert['power'] = np.mean(self.hilbert['power'], axis=0)
		self.hilbert['power'] = np.reshape(self.hilbert['power'], (1, *self.hilbert['power'].shape))

		return self

	def hilbert_power_plot(
			self,
			fig=None,
			ax=None,
			title='',
			xlabel='',
			ylabel='',
			legend=True,
			color=None,
			*args,
			**kwargs):
		color = color if color else self.graphics_style['line_color']

		if 'plt_style' in self.graphics_style.keys():
			plt.style.use(self.graphics_style['plt_style'])

		# We will show the graph if no fig or ax is shown. Assuming that this is the desired action.
		show = False
		if fig is None or ax is None:
				show = True
				fig, ax = plt.subplots(nrows=self.num_channels, ncols=1)

		if self.num_channels == 1:
			ax = [ax]

		for epoch in self.hilbert['power']:
			for idx, channel in enumerate(epoch):
				ax[idx].plot(
					self.t,
					channel,
					color=color,
					*args,
					**kwargs
				)

				for tag in self.tags:
					ax[idx].axvline(
						tag / self.fs,
						color='#000000',
						ls='--'
					)

				ax[idx].margins(0.1, 0.1)

				ax[idx].set_title(
					self.channel_names[idx],
					fontsize=20
				)
				ax[idx].set_facecolor(self.graphics_style['plot_background'])
				ax[idx].tick_params(labelsize=self.graphics_style['ticks_size'])
				ax[idx].grid(self.graphics_style['show_grid'], color=self.graphics_style['grid_color'])

				fig.text(
					0.5,
					0.05,
					xlabel,
					ha='center',
					fontsize=self.graphics_style['label_size']
				)
				fig.text(
					0.5,
					0.95,
					title,
					ha='center',
					fontsize=self.graphics_style['label_size']
				)
				fig.text(
					0.04,
					0.5,
					ylabel,
					va='center',
					rotation='vertical',
					fontsize=self.graphics_style['label_size']
				)

				fig.patch.set_facecolor(self.graphics_style['figure_background'])

			# We only want the label to show once if multiple epochs
			if 'label' in kwargs:
				del kwargs['label']

		if legend:
			for a in ax:
				a.legend()

		if show:
			plt.show()
			plt.close()

	def __str__(self):
		return 'Hilbert'

	def __repr__(self):
		return 'Hilbert'
