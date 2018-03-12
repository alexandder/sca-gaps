import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import logs_reader as logs_reader


def make_histogram_for_all(data, path):
    plt.hist(data, bins=100, range=(0.5,1))
    plt.xlabel('Success rate')
    plt.ylabel('Number')
    plt.xlim(0.5,1.0)
    plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    plt.savefig(path + 'histogram_all.pdf')
    plt.close()

def make_histograms_grouped_by_neighborhoods(data, path):
    f, axarr = plt.subplots(2, 4)
    xlim = 1

    axarr[0, 0].hist(data['1'], bins=200)
    axarr[0, 0].set_title("1")
    axarr[0, 0].set_xlim(0, xlim)

    axarr[0, 1].hist(data['2'], bins=200)
    axarr[0, 1].set_title("2")
    axarr[0, 1].set_xlim(0, xlim)

    axarr[0, 2].hist(data['3'], bins=200)
    axarr[0, 2].set_title("3")
    axarr[0, 2].set_xlim(0, xlim)

    axarr[0, 3].hist(data['4'], bins=200)
    axarr[0, 3].set_title("4")
    axarr[0, 3].set_xlim(0, xlim)

    axarr[1, 0].hist(data['5'], bins=200)
    axarr[1, 0].set_title("5")
    axarr[1, 0].set_xlim(0, xlim)

    axarr[1, 1].hist(data['6'], bins=200)
    axarr[1, 1].set_title("6")
    axarr[1, 1].set_xlim(0, xlim)

    axarr[1, 2].hist(data['7'], bins=200)
    axarr[1, 2].set_title("7")
    axarr[1, 2].set_xlim(0, xlim)

    axarr[1, 3].hist(data['8'], bins=200)
    axarr[1, 3].set_title("8")
    axarr[1, 3].set_xlim(0, xlim)
    #axarr[1, 3].set_ylim(0, 75)
    f.set_size_inches(18.5, 10.5)
    f.savefig(path + 'histogram_neighborhoods.pdf')
    plt.close(f)

def make_histogram_number_of_nondeterministic_gaps(data, path):
    plt.hist(data, bins=200)
    plt.xlabel('Nondeterministic gaps')
    plt.ylabel('Number')
    plt.savefig(path + 'histogram_number_nondeterministic_gaps.pdf')
    plt.close()

def make_histogram_for_nei(data, path, nei):
    weights = np.ones_like(data) / float(len(data))
    plt.hist(data, weights=weights, range=(0.5,1), bins=50)
    plt.xlabel('Success rate')
    plt.ylabel('Fraction')
    plt.xlim(0.5, 1.0)
    plt.ylim(0, 1.0)
    plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    plt.savefig(path + 'histogram_sr_' + str(nei) + '.pdf')
    plt.close()

def make_graphs():
    for lmb in ['0.05/']:
        path = '../../graphs/' + lmb

        all_success_rates = logs_reader.read_all_success_rates(lmb)
        make_histogram_for_all(all_success_rates, path)

        success_rates_grouped = logs_reader.read_success_rates_grouped_by_inconsistent_neighborhoods(lmb)
        make_histograms_grouped_by_neighborhoods(success_rates_grouped, path)

        number_nondeterministic_gaps = logs_reader.read_number_of_nondeterministic_gaps(lmb)
        make_histogram_number_of_nondeterministic_gaps(number_nondeterministic_gaps, path)

for i in range(1, 9):
    success_rates_grouped = logs_reader.read_success_rates_grouped_by_inconsistent_neighborhoods('0.05/')
    make_histogram_for_nei(success_rates_grouped[str(i)], '../../graphs/0.05/', i)

# path = '../../graphs/' + '0.05/'

# all_success_rates = logs_reader.read_all_success_rates('0.05/')
# make_histogram_for_all(all_success_rates, path)