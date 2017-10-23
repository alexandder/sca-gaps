import numpy as np
import matplotlib.pyplot as plt
import lib.ca_data as ca_data
import graphs.logs_reader as logs_reader

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
        avgs.setdefault(ca_data.getWolframClassForRule(r), []).append(100*averages[r])
        ss.setdefault(ca_data.getWolframClassForRule(r), []).append(100*sds[r])
    plt.plot(avgs['1'], ss['1'], 'ro', label="Wolfram class I")
    plt.plot(avgs['2'], ss['2'], 'bo', label="Wolfram class II")
    plt.plot(avgs['3'], ss['3'], 'ko', label="Wolfram class III")
    plt.plot(avgs['4'], ss['4'], 'go', label="Wolfram class IV")
    plt.legend()
    plt.title("Average and standard deviation of success rates in %")
    plt.xlabel('average')
    plt.ylabel('standard deviation')
    plt.savefig(path + name)
    plt.close()

def make_graphs():
    for lmb in ['0.05/', '0.15/']:
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
