import matplotlib.pyplot as plt


def read_data():
    result = {}
    f = open('results', 'r')
    for line in f:
        data = line.split(", ")
        result[data[0]] = float(data[4])
    return result

def make_plot(data, path):
    plt.bar(range(len(list(data.keys()))), list(data.values()))
    plt.xlabel('Rule')
    plt.ylabel('Max - min')
    plt.title('Max - min of success rate')
    plt.savefig(path + 'histogram_detailed.pdf')
    plt.close()


make_plot(read_data(), '')