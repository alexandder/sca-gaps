import math
import numpy as np

def get_stats_for_rule(rule):
    result = []
    f = open('../../logs/detailed/' + str(rule) + '.out', 'r')
    for line in f:
        result = line.split(' ')
    if '' in result:
        result.remove('')
    result = list(map(float, result))
    f.close()
    for r in range(256):
        other_rule = []
        if r != rule:
            f = open('../../logs/detailed/' + str(r) + '.out', 'r')
            for line in f:
                other_rule = line.split(' ')
            if '' in other_rule:
                other_rule.remove('')
            f.close()
            other_rule = list(map(float, other_rule))
            start = find_place(rule, r) * 10000
            end = (find_place(rule, r) + 1) * 10000
            if start < len(other_rule) and end < len(other_rule):
                result.extend(other_rule[start:end])
            print("end rule " + str(rule) + " " + str(r))
    return [str(rule), str(len(result)), str(max(result)), str(min(result)), str(max(result) - min(result)), str(1.0*sum(result)/len(result))]

def find_place(current_rule, file_rule):
    if current_rule < file_rule:
        return current_rule
    return current_rule - 1

def stddev(lst):
    """returns the standard deviation of lst"""
    variance = 0
    mn = math.mean(lst)
    for e in lst:
        variance += (e-mn)**2
    variance /= len(lst)

    return math.sqrt(variance)

def get_stats_in_memory():
    keys = [str(i) for i in range(3)]
    result = {key: [] for key in keys}
    print(result)
    for r in range(3):
        f = open(str(r) + '.out', 'r')
        all_r = []
        for line in f:
            all_r = line.split(' ')
        if '' in result:
            all_r.remove('')
        all_r = list(map(float, all_r))
        result[str(r)] = all_r
        for second_r in range(3):
            if second_r != r:
                start = find_place(second_r, r) * 10
                end = (find_place(second_r, r) + 1) * 10
                result[str(second_r)].extend(all_r[start:end])
    for k in result:
        print(len(result[k]))
    return result


def find_stats():
    file = open('results2', 'w')
    for r in [55, 66]:
        stat = get_stats_for_rule(r)
        print(stat)
        file.write(', '.join(stat))
        file.write('\n')
    file.close()

def group_logs():
    logs = []
    for r in range(256):
        f = open('../../logs/detailed/' + str(r) + '.out', 'r')
        for line in f:
            logs = line.split(' ')
        if '' in logs:
            logs.remove('')
        f.close()
        for second_r in range(256):
            if second_r != r:
                start = find_place(second_r, r) * 10000
                end = (find_place(second_r, r) + 1) * 10000
                if start < len(logs) and end < len(logs):
                    rest = ' '.join(logs[start:end])
                    with open('../../logs/detailed_grouped/' + str(r) + '.out', "a") as myfile:
                        myfile.write(' ')
                        myfile.write(rest)
                print("end rule " + str(second_r) + " " + str(r))

def get_stats():
    for r in range(256):
        result = []
        f = open('../../logs/detailed_grouped/' + str(r) + '.out', 'r')
        for line in f:
            result = line.split(' ')
        if '' in result:
            result.remove('')
        f.close()
        result = list(map(float, result))
        print ([str(r), len(result), max(result), min(result), max(result) - min(result),
                np.mean(result), np.std(result)])
get_stats()