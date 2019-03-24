import matplotlib.pyplot as plt
import seaborn as sns

from .PluginManager import PluginManager

sns.set()
sns.set_context("talk", font_scale=1.4)


class GraphicsPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def graphics_spectrum_plot(self, fig, ax, title='', ylabel='', xlabel='', color='#ff0641', *args, **kwargs):
		plt.style.use('classic')

		for epoch in self.spectrum:
			for idx, channel in enumerate(epoch):
				ax[idx].plot(
					self.spectrum_freqs,
					channel,
					color=color,
					*args,
					**kwargs
				)

				ax[idx].margins(0.1, 0.1)

				ax[idx].set_title(
					self.channel_names[idx],
					fontsize=20
				)
				ax[idx].set_facecolor('#ffedf1')
				ax[idx].tick_params(labelsize=14)
				ax[idx].grid(True, color='r')

				fig.text(
					0.5,
					0.05,
					xlabel,
					ha='center',
					fontsize=20
				)
				fig.text(
					0.5,
					0.95,
					title,
					ha='center',
					fontsize=20
				)
				fig.text(
					0.04,
					0.5,
					ylabel,
					va='center',
					rotation='vertical',
					fontsize=20
				)

				fig.patch.set_facecolor('#ffffff')

	def graphics_time_plot(self, fig, ax, title='', ylabel='', xlabel='', color='#ff0641', *args, **kwargs):
		plt.style.use('classic')

		for epoch in self.data:
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
				ax[idx].set_facecolor('#ffedf1')
				ax[idx].tick_params(labelsize=14)
				ax[idx].grid(True, color='r')

				fig.text(
					0.5,
					0.05,
					xlabel,
					ha='center',
					fontsize=20
				)
				fig.text(
					0.5,
					0.95,
					title,
					ha='center',
					fontsize=20
				)
				fig.text(
					0.04,
					0.5,
					ylabel,
					va='center',
					rotation='vertical',
					fontsize=20
				)

				fig.patch.set_facecolor('#ffffff')

	def __str__(self):
		return 'Graphics'

	def __repr__(self):
		return 'Graphics'
