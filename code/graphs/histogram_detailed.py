import matplotlib.pyplot as plt


def read_data(column):
    result = {}
    f = open('results', 'r')
    for line in f:
        data = line.replace("\n", "").replace("]", "").split(", ")
        result[data[0]] = float(data[column])
    return result


def make_plot(data, path):
    plt.bar(range(len(list(data.keys()))), list(data.values()))
    plt.xlabel('Rule')
    plt.ylabel('Max - min')
    plt.title('Max - min of success rate')
    plt.savefig(path + 'histogram_detailed.pdf')
    plt.close()

def make_plot_std(data, path):
    plt.bar(range(len(list(data.keys()))), list(data.values()))
    plt.xlabel('Rule')
    plt.ylabel('Standard deviation')
    plt.title('Standard deviation')
    plt.savefig(path + 'sd_detailed.pdf')
    plt.close()

def make_plot_mean(data, path):
    plt.bar(range(len(list(data.keys()))), list(data.values()))
    plt.xlabel('Rule')
    plt.ylabel('mean')
    plt.title('mean')
    plt.savefig(path + 'mean_detailed.pdf')
    plt.close()


make_plot(read_data(3), '')

make_plot_std(read_data(5), '')
make_plot_mean(read_data(4), '')