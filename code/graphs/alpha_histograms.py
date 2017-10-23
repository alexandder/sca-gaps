import matplotlib.pyplot as plt

import graphs.logs_reader as logs_reader

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

def make_graphs():
    for lmb in ['0.05/', '0.15/']:
        path = '../../graphs/' + lmb
        alphas = [0.1, 0.2, 0.3, 0.4]
        data = logs_reader.read_success_rates_for_alphas(alphas, lmb)
        make_histograms_grouped_by_neighborhoods(data, path)
