import os

def read_success_rate_for_rule(rule):
    result = []
    f = open('../../logs/' + str(rule) + '.out', 'r')
    for line in f:
        if line[0] != 'a':
            data = line.split(" ")
            result.append(float(data[7].replace(',', '')))
    return result

def read_all_success_rates():
    result = []
    for r in range(256):
        result.append(read_success_rate_for_rule(r))
    return [rule for sublist in result for rule in sublist]

def read_success_rates_for_number_of_inconsistnet_neighborhoods(number):
    result = []
    for r in range(256):
        f = open('../../logs/' + str(r) + '.out', 'r')
        for line in f:
            if line[0] != 'a':
                data = line.split(" ")
                r1 = int(data[1].replace(',', ''))
                r2 = int(data[2].replace(',', ''))
                if number_of_inconsistent_neighborhoods(r1, r2) == number:
                    result.append(float(data[7].replace(',', '')))
    return result

def number_of_inconsistent_neighborhoods(rule1, rule2):
    r1_b = format(rule1, "#010b")[2:]
    r2_b = format(rule2, "#010b")[2:]
    result = 0
    for i in range(8):
        if r1_b[i] != r2_b[i]:
            result += 1
    return result

def read_success_rates_grouped_by_inconsistent_neighborhoods():
    result = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []}
    for i in range(1, 9):
        result[str(i)] = read_success_rates_for_number_of_inconsistnet_neighborhoods(i)
    print(result['8'])
    return result

def read_success_rates_for_rules():
    result = {}
    for r in range(256):
        f = open('../../logs/' + str(r) + '.out', 'r')
        for line in f:
            if line[0] != 'a':
                data = line.split(" ")
                r2 = int(data[2].replace(',', ''))
                sr = float(data[7].replace(',', ''))
                result.setdefault(r, []).append(sr)
                result.setdefault(r2, []).append(sr)
    return result