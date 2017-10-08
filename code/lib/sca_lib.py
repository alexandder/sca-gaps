import random

import lib.ca_lib as ca_lib


def apply_stochastic_rule(rule1, rule2, l, c, r, alpha):
    if alpha < 0 or alpha > 1:
        raise Exception('Wrong alpha: ' + str(alpha))
    random_number = random.random()
    if random_number < alpha:
        return ca_lib.apply_rule(rule1, l, c, r)
    return ca_lib.apply_rule(rule2, l, c, r)

def apply_stochastic_rule_to_vector(input_configuration, rule1, rule2, alpha):
    result = []
    for i in range(len(input_configuration)):
        if i == len(input_configuration) - 1:
            result.append(apply_stochastic_rule(rule1, rule2, input_configuration[i - 1], input_configuration[i], input_configuration[0], alpha))
        elif i == 0:
            result.append(apply_stochastic_rule(rule1, rule2, input_configuration[len(input_configuration) - 1], input_configuration[i], input_configuration[i + 1], alpha))
        else:
            result.append(apply_stochastic_rule(rule1, rule2, input_configuration[i - 1], input_configuration[i], input_configuration[i + 1], alpha))
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
        for i in range(len(simulation[t])):
            vector = simulation[t]
            rule_result = str(simulation[t+1][i])
            if i == 0:
                index = str(vector[len(vector) - 1]) + str(vector[i]) + str(vector[i + 1])
                result[index][rule_result] = result[index][rule_result] + 1
            elif i == len(vector) - 1:
                index = str(vector[i - 1]) + str(vector[i]) + str(vector[0])
                result[index][rule_result] = result[index][rule_result] + 1
            else:
                index = str(vector[i - 1]) + str(vector[i]) + str(vector[i + 1])
                result[index][rule_result] = result[index][rule_result] + 1
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
        for i in range(len(simulation[t])):
            rule_result = str(simulation[t+1][i])
            if rule_result != str(-1):
                if i == 0 and not skip_neighborhood(i, vector):
                    index = str(vector[len(vector) - 1]) + str(vector[i]) + str(vector[i + 1])
                    result[index][rule_result] = result[index][rule_result] + 1
                elif i == len(vector) - 1 and not skip_neighborhood(i, vector):
                    index = str(vector[i - 1]) + str(vector[i]) + str(vector[0])
                    result[index][rule_result] = result[index][rule_result] + 1
                elif not skip_neighborhood(i, vector):
                    index = str(vector[i - 1]) + str(vector[i]) + str(vector[i + 1])
                    result[index][rule_result] = result[index][rule_result] + 1
    return result
