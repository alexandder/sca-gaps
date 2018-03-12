import numpy as np
import matplotlib.pyplot as plt
import logs_reader as logs_reader
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter


def make_histograms_grouped_by_neighborhoods(data, path):
    f, axarr = plt.subplots(2, 2)
    xlim = 1

    axarr[0, 0].hist(data["0.1"], bins=200)
    axarr[0, 0].set_title("0.1")
    axarr[0, 0].set_xlim(0, xlim)
    axarr[0, 0].set_ylim(0, 1400)

    axarr[0, 1].hist(data["0.2"], bins=200)
    axarr[0, 1].set_title("0.2")
    axarr[0, 1].set_xlim(0, xlim)
    axarr[0, 1].set_ylim(0, 1400)

    axarr[1, 0].hist(data["0.3"], bins=200)
    axarr[1, 0].set_title("0.3")
    axarr[1, 0].set_xlim(0, xlim)
    axarr[1, 0].set_ylim(0, 1400)

    axarr[1, 1].hist(data["0.4"], bins=200)
    axarr[1, 1].set_title("0.4")
    axarr[1, 1].set_xlim(0, xlim)
    axarr[1, 1].set_ylim(0, 1400)


    f.set_size_inches(18.5, 10.5)
    f.savefig(path + 'histogram_alpha.pdf')
    plt.close(f)

def make_graph(data, lmb):
    scaled = [x for x in data]
    weights = np.ones_like(scaled) / float(len(scaled))
    plt.hist(data, weights=weights, bins=50, range=(0.5,1))
    plt.xlabel('Success rate')
    plt.ylabel('Fraction')
    plt.ylim(0, 0.5)
    plt.xlim(0.5, 1.0)
    plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    plt.savefig('../../graphs/0.05/histogram_' + str(lmb) + '.pdf')
    plt.close()

def make_graphs():
    for lmb in ['0.05/']:
        alphas = [0.1, 0.2, 0.3, 0.4]
        data = logs_reader.read_success_rates_for_alphas(alphas, lmb)
        make_graph(data['0.1'], 0.1)
        make_graph(data['0.2'], 0.2)
        make_graph(data['0.3'], 0.3)
        make_graph(data['0.4'], 0.4)

make_graphs()

