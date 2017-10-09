import random

import lib.ca_lib as ca_lib


def apply_stochastic_rule(rule1, rule2, l, c, r, alpha):
    if alpha < 0 or alpha > 1:
        raise Exception('Wrong alpha: ' + str(alpha))
    random_number = random.random()
    if random_number < alpha:
        return ca_lib.apply_rule(rule1, l, c, r)
    return ca_lib.apply_rule(rule2, l, c, r)

def apply_stochastic_rule_to_vector(vector, rule1, rule2, alpha):
    result = []
    result.append(apply_stochastic_rule(rule1, rule2, vector[len(vector) - 1], vector[0], vector[1], alpha))
    for i in range(1, len(vector) - 1):
        result.append(apply_stochastic_rule(rule1, rule2, vector[i - 1], vector[i], vector[i + 1], alpha))
    result.append(apply_stochastic_rule(rule1, rule2, vector[len(vector) - 2], vector[len(vector) - 1], vector[0], alpha))
    return result

def simulate(initial, T, rule1, rule2, alpha):
    res = [initial]
    for k in range(T):
        res.append(apply_stochastic_rule_to_vector(res[len(res) - 1], rule1, rule2, alpha))
    return res


def get_number_of_neighborhoods(simulation):
    result = {"111": {'0': 0, '1': 0}, "110": {'0': 0, '1': 0}, "101": {'0': 0, '1': 0}, "100": {'0': 0, '1': 0},
              "011": {'0': 0, '1': 0}, "001": {'0': 0, '1': 0}, "010": {'0': 0, '1': 0}, "000": {'0': 0, '1': 0}}
    for t in range(len(simulation) - 1):
        vector = simulation[t]

        nei = str(vector[len(vector) - 1]) + str(vector[0]) + str(vector[1])
        rule_result = str(simulation[t + 1][0])
        result[nei][rule_result] = result[nei][rule_result] + 1

        for i in range(1, len(vector) - 1):
            rule_result = str(simulation[t+1][i])
            nei = str(vector[i - 1]) + str(vector[i]) + str(vector[i + 1])
            result[nei][rule_result] = result[nei][rule_result] + 1

        nei = str(vector[len(vector) - 2]) + str(len(vector) - 1) + str(vector[0])
        rule_result = str(simulation[t + 1][len(vector) - 1])
        result[nei][rule_result] = result[nei][rule_result] + 1
    return result

def skip_neighborhood(i, vector):
    if i == 0 and (vector[len(vector) - 1] == -1 or vector[i] == -1 or vector[i+1] == -1):
        return True
    elif i == len(vector) - 1 and (vector[i-1] == -1 or vector[i] == -1 or vector[0]):
        return True
    elif i != 0 and i != len(vector) - 1 and (vector[i - 1] == -1 or vector[i] == -1 or vector[i + 1] == -1):
        return True
    return False

def get_number_of_neighborhoods_with_gaps(simulation):
    result = {"111": {'0': 0, '1': 0}, "110": {'0': 0, '1': 0}, "101": {'0': 0, '1': 0}, "100": {'0': 0, '1': 0},
              "011": {'0': 0, '1': 0}, "001": {'0': 0, '1': 0}, "010": {'0': 0, '1': 0}, "000": {'0': 0, '1': 0}}
    for t in range(len(simulation) - 1):
        vector = simulation[t]

        rule_result = simulation[t + 1][0]
        if rule_result != -1 and not skip_neighborhood(0, vector):
            nei = str(vector[len(vector) - 1]) + str(vector[0]) + str(vector[1])
            result[nei][str(rule_result)] = result[nei][str(rule_result)] + 1

        for i in range(1, len(simulation[t]) - 1):
            rule_result = simulation[t+1][i]
            if rule_result != -1 and not skip_neighborhood(i, vector):
                nei = str(vector[i - 1]) + str(vector[i]) + str(vector[i + 1])
                result[nei][str(rule_result)] = result[nei][str(rule_result)] + 1

        rule_result = simulation[t + 1][len(vector) - 1]
        if rule_result != -1 and not skip_neighborhood(len(vector) - 1, vector):
            nei = str(vector[len(vector) - 2]) + str(vector[len(vector) - 1]) + str(vector[0])
            result[nei][str(rule_result)] = result[nei][str(rule_result)] + 1
    return result
