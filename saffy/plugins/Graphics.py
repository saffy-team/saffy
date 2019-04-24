import matplotlib.pyplot as plt
import seaborn as sns

from .PluginManager import PluginManager

sns.set()
sns.set_context("talk", font_scale=1.4)


class GraphicsPlugin(PluginManager):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.style_templates = {
			'presentation': {
				'plot_background': '#ffedf1',
				'figure_background': '#ffffff',
				'show_grid': True,
				'grid_color': 'r',
				'ticks_size': 14,
				'label_size': 20,
				'plt_style': 'classic',
				'line_color': '#ff0641'
			},
			'paper': {
				'plot_background': '#ffffff',
				'figure_background': '#ffffff',
				'show_grid': True,
				'grid_color': 'k',
				'ticks_size': 14,
				'label_size': 20,
				'plt_style': 'classic',
				'line_color': '#000000'
			}
		}

		self.style = self.style_templates['presentation']

	def graphics_set_style(self, style):
		if isinstance(style, dict):
			self.style = {**self.style, **style}
		elif style in self.style_templates.keys():
			self.style = self.style_templates[style]
		else:
			raise ValueError('Unknown style')
		return self

	def graphics_spectrum_plot(
			self,
			fig=None,
			ax=None,
			title='',
			xlabel='',
			ylabel='',
			legend=True,
			color=None,
			*args,
			**kwargs
	):
		color = color if color else self.style['line_color']

		if 'plt_style' in self.style.keys():
			plt.style.use(self.style['plt_style'])

		show = False
		if fig is None or ax is None:
			show = True
			fig, ax = plt.subplots(nrows=self.num_channels, ncols=1)

		if self.num_channels == 1:
			ax = [ax]

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
				ax[idx].set_facecolor(self.style['plot_background'])
				ax[idx].tick_params(labelsize=self.style['ticks_size'])
				ax[idx].grid(self.style['show_grid'], color=self.style['grid_color'])

				fig.text(
					0.5,
					0.05,
					xlabel,
					ha='center',
					fontsize=self.style['label_size']
				)
				fig.text(
					0.5,
					0.95,
					title,
					ha='center',
					fontsize=self.style['label_size']
				)
				fig.text(
					0.04,
					0.5,
					ylabel,
					va='center',
					rotation='vertical',
					fontsize=self.style['label_size']
				)

				fig.patch.set_facecolor(self.style['figure_background'])

			# We only want the label to show once if multiple epochs
			if 'label' in kwargs:
				del kwargs['label']

		if legend:
			for a in ax:
				a.legend()

		if show:
			plt.show()
			plt.close()

	def graphics_time_plot(
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
		color = color if color else self.style['line_color']

		if 'plt_style' in self.style.keys():
			plt.style.use(self.style['plt_style'])

		# We will show the graph if no fig or ax is shown. Assuming that this is the desired action.
		show = False
		if fig is None or ax is None:
				show = True
				fig, ax = plt.subplots(nrows=self.num_channels, ncols=1)

		if self.num_channels == 1:
			ax = [ax]

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
				ax[idx].set_facecolor(self.style['plot_background'])
				ax[idx].tick_params(labelsize=self.style['ticks_size'])
				ax[idx].grid(self.style['show_grid'], color=self.style['grid_color'])

				fig.text(
					0.5,
					0.05,
					xlabel,
					ha='center',
					fontsize=self.style['label_size']
				)
				fig.text(
					0.5,
					0.95,
					title,
					ha='center',
					fontsize=self.style['label_size']
				)
				fig.text(
					0.04,
					0.5,
					ylabel,
					va='center',
					rotation='vertical',
					fontsize=self.style['label_size']
				)

				fig.patch.set_facecolor(self.style['figure_background'])

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
		return 'Graphics'

	def __repr__(self):
		return 'Graphics'
