import random
import sys

import ca_data as ca_data


def apply_rule(number, l, c, r):
    binary_rule_number = format(number, "#010b")[2:]
    neighborhood = int(str(l) + str(c) + str(r), 2)
    position = -neighborhood + 7
    return int(binary_rule_number[position])


def applyRuleToVector(a, ruleNumber):
    result = []
    for i in range(len(a)):
        if i == len(a) - 1:
            result.append(apply_rule(ruleNumber, a[i - 1], a[i], a[0]))
        elif i == 0:
            result.append(apply_rule(ruleNumber, a[len(a) - 1], a[i], a[i + 1]))
        else:
            result.append(apply_rule(ruleNumber, a[i - 1], a[i], a[i + 1]))
    return result


def printArray(arr):
    for b in arr:
        if b == 1:
            sys.stdout.write(u"\u25A0")
        else:
            sys.stdout.write(' '),
    print


def vectorToString(arr):
    result = ""
    for b in arr:
        if b == 1:
            result += u"\u25A0"
        else:
            result += " "
    return result

def bin_vector_to_string(v):
    vs = ""
    for bit in v:
        vs += str(bit)
    return vs

def simulate(initial, T, ruleNumber):
    res = []
    res.append(initial)
    for k in range(T):
        res.append(applyRuleToVector(res[len(res) - 1], ruleNumber))
    return res


def printSimulation(simulation):
    for arr in simulation:
        printArray(arr)

def print_simulation_as_table(simulation):
    print()
    for vec in simulation:
        for v in vec:
            sys.stdout.write(str(v))
        print()

def createStandardInitalVector(N):
    initial = []
    for i in range(N):
        if i == N / 2:
            initial.append(1)
        else:
            initial.append(0)
    return initial


def getFrequencies(vector):
    res = {"111": 0, "110": 0, "101": 0, "100": 0, "011": 0, "001": 0, "010": 0, "000": 0}
    for i in range(len(vector)):
        if i == len(vector) - 2:
            index = str(vector[i]) + str(vector[i + 1]) + str(vector[0])
            res[index] = res[index] + 1
        elif i == len(vector) - 1:
            index = str(vector[i]) + str(vector[0]) + str(vector[1])
            res[index] = res[index] + 1
        else:
            index = str(vector[i]) + str(vector[i + 1]) + str(vector[i + 2])
            res[index] = res[index] + 1
    return res


def getFrequenciesOfSimulation(simulation):
    result = []
    for step in simulation:
        result.append(getFrequencies(step))
    return result

def get_neighborhoods_count_for_simulation(simulation):
    result = {"111": 0, "110": 0, "101": 0, "100": 0, "011": 0, "001": 0, "010": 0, "000": 0}
    for t in range(len(simulation)):
        freqs = getFrequencies(simulation[t])
        for nei in ca_data.elementary_neighborhoods:
            result[nei] = result[nei] + freqs[nei]
    return result


def getAggregateFrequenciesForEachBlock(frequencies):
    result = {"111": [], "110": [], "101": [], "100": [], "011": [], "001": [], "010": [], "000": []}
    f0 = frequencies[0]
    sum = 0
    for b in f0:
        sum = 1.0 * sum + f0[b]
    for i in range(len(frequencies)):
        f = frequencies[i]
        for block in f:
            if i == 0:
                result[block].append(f[block] / sum)
            else:
                prev = sum * i * result[block][i - 1]
                result[block].append((prev + f[block]) / (sum * (i + 1)))
    return result


def printFrequencies(frequencies):
    print('\t000\t 001\t 010\t 011\t 100\t 101\t 110\t 111')
    for i in range(len(frequencies)):
        f = frequencies[i]
        print(str(i) + "\t " + str(f["000"]) + "\t" + str(f["001"]) + "\t" + str(f["010"]) + "\t" + str(
            f["011"]) + "\t" + str(f["100"]) + "\t" + str(f["101"]) + "\t" + str(f["110"]) + "\t" + str(f["111"]))


def getFrequenciesForEachBlock(frequencies):
    result = {"111": [], "110": [], "101": [], "100": [], "011": [], "001": [], "010": [], "000": []}
    for i in range(len(frequencies)):
        f = frequencies[i]
        for block in f:
            result[block].append(f[block])
    return result

def create_random_initial_vector(n):
    return [random.randint(0,1) for i in range(n)]


def is_consistent_with_id(rule, neighborhood):
    return str(apply_rule(rule, int(neighborhood[0]), int(neighborhood[1]), int(neighborhood[2]))) == neighborhood[1]

def get_neighborhoods_consistent_with_id(rule):
    result = []
    neighborhoods = ['000', '001', '010', '011', '100', '101', '110', '111']
    return filter(lambda n : is_consistent_with_id(rule, n), neighborhoods)

def get_neighborhoods_non_consistent_with_id(rule):
    result = []
    neighborhoods = ['000', '001', '010', '011', '100', '101', '110', '111']
    return filter(lambda n : not is_consistent_with_id(rule, n), neighborhoods)

def get_maximal_k_for_rule(rule):
    if ca_data.getWolframClassForRule(rule) == '3':
        return 1500
    if ca_data.getWolframClassForRule(rule) == '4':
        return 1300
    return 240

def get_number_of_neghborhoods_inconsistent_with_id():
    result = {}
    for r in range(256):
        result[r] = len(get_neighborhoods_non_consistent_with_id(r))
    return result


