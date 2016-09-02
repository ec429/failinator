#! /usr/bin/python

import failfast
import matplotlib.pyplot as plt

def setup_plot():
	fig = plt.figure()
	ax_lr = fig.add_subplot(2,1,1)
	ax_lr.set_xticks(xrange(21))
	ax_lr.set_ylabel('PDF')
	ax_clr = fig.add_subplot(2,1,2)
	ax_clr.hlines([0.025, 0.05, 0.5, 0.95, 0.975], 0, 20)
	ax_clr.set_ylim(0, 1)
	ax_clr.set_xticks(xrange(21))
	ax_clr.set_xlabel('parameter p')
	ax_clr.set_ylabel('CDF')
	return ax_lr, ax_clr

def plot_ij(axes, i, j, prior=0.5, fmt=None, label=None):
	i += prior
	j += prior
	ax_lr, ax_clr = axes
	percents = [p / 4.0 for p in xrange(81)]
	ax_lr.plot(percents, failfast.series_LR([p / 100.0 for p in percents], i, j), fmt, label=label)
	ax_clr.plot(percents, failfast.series_CLR([p / 100.0 for p in percents], i, j), fmt, label=label)

if __name__ == "__main__":
	axes = setup_plot()
	plot_ij(axes, 2, 29, fmt='b', label='Falcon 9')
	plot_ij(axes, 2, 135, fmt='g', label='Shuttle')
	plot_ij(axes, 10, 98, fmt='r', label='Proton-M')
	plot_ij(axes, 5, 62, fmt='m', label='Soyuz-2')
	plot_ij(axes, 0, 56, fmt='k', label='Soyuz FG')
	plot_ij(axes, 20, 784, fmt='c', label='Soyuz U')
	plot_ij(axes, 1, 64, fmt='y', label='Atlas V')
	plot_ij(axes, 4, 87, fmt='#ff7f00', label='Ariane 5')
	axes[0].legend()
	plt.show()
