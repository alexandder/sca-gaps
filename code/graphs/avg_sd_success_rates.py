import numpy as np
import matplotlib.pyplot as plt
import lib.ca_data as ca_data
import graphs.logs_reader as logs_reader
from matplotlib.ticker import FuncFormatter


def find_averages(data):
    result = {}
    for d in data:
        result[d] = np.mean(data[d])
    return result

def find_sds(data):
    result = {}
    for d in data:
        result[d] = np.std(data[d])
    return result


def make_graph(averages, sds, path, name):
    avgs = {}
    ss = {}
    for r in range(256):
        avgs.setdefault(ca_data.getWolframClassForRule(r), []).append(averages[r])
        ss.setdefault(ca_data.getWolframClassForRule(r), []).append(sds[r])
    plt.plot(avgs['1'], ss['1'], 'go', marker='D', label="class I")
    plt.plot(avgs['2'], ss['2'], 'bo', marker='x', label="class II")
    plt.plot(avgs['3'], ss['3'], 'ko', marker='+', label="class III")
    plt.plot(avgs['4'], ss['4'], 'ro', marker='o', markersize=4, label="class IV")
    plt.legend()
    plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.1%}'.format(y)))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.1%}'.format(y)))
    plt.xlabel('average of success rate')
    plt.ylabel('standard deviation of success rate')
    plt.savefig(path + name)
    plt.close()

def make_graphs():
    for lmb in ['0.05/']:
        path = '../../graphs/' + lmb

        name = 'avg_sd.pdf'
        data = logs_reader.read_success_rates_for_rules(lmb)
        avgs = find_averages(data)
        sds = find_sds(data)
        make_graph(avgs, sds, path, name)

        nond_name = 'nodeterministic_avg_sd.pdf'
        nondeterministic_data = logs_reader.read_success_rates_for_nondeterministic_gaps_and_rules(lmb)
        nond_avgs = find_averages(nondeterministic_data)
        nond_sds = find_sds(nondeterministic_data)
        make_graph(nond_avgs, nond_sds, path, nond_name)

make_graphs()
