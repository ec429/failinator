#! /usr/bin/python

import failfast
import rocket
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

def plot_rkt(axes, rkt, fmt):
    plot_ij(axes, rkt.failures, rkt.launches, fmt=fmt, label=rkt.name)

if __name__ == "__main__":
    axes = setup_plot()
    plot_rkt(axes, rocket.Falcon9, 'b')
    plot_rkt(axes, rocket.Shuttle, 'g')
    plot_rkt(axes, rocket.ProtonM, 'r')
    plot_rkt(axes, rocket.Soyuz2, 'm')
    plot_rkt(axes, rocket.SoyuzFG, 'k')
    plot_rkt(axes, rocket.SoyuzU, 'c')
    plot_rkt(axes, rocket.AtlasV, 'y')
    plot_rkt(axes, rocket.Ariane5, '#ff7f00')
    plot_rkt(axes, rocket.DeltaII, '0.5')
    plot_rkt(axes, rocket.DeltaIV, '#ffbf7f')
    plot_rkt(axes, rocket.Antares, '#7f7fff')
    axes[0].legend()
    plt.show()
