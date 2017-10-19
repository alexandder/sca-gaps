import matplotlib.pyplot as plt

import graphs.logs_reader as logs_reader


def make_histogram_for_all(data):
    plt.hist(data, bins=200)
    plt.xlabel('Success rate')
    plt.ylabel('Number')
    plt.title('Success rate histogram for all')
    plt.savefig('../../graphs/histogram_all.pdf')

def make_histograms_grouped_by_neighborhoods(data):
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
    f.savefig('../../graphs/histogram_neighborhoods.pdf')
    plt.close(f)

# all_success_rates = logs_reader.read_all_success_rates()
# make_histogram_for_all(all_success_rates)

success_rates_grouped = logs_reader.read_success_rates_grouped_by_inconsistent_neighborhoods()
make_histograms_grouped_by_neighborhoods(success_rates_grouped)