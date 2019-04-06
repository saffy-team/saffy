import saffy

sig = saffy.SignalManager(generator=saffy.generators.simple_sine_generator(10, 0, 1, 128))\
	.graphics_time_plot()\
	.fourier_transform()\
	.graphics_spectrum_plot()
