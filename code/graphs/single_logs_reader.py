def read_success_rate_for_rule(rule, path):
    result = []
    f = open('../../logs/' + path + str(rule) + '.out', 'r')
    for line in f:
        if line[0] != 'a':
            data = line.split(" ")
            result.append(float(data[3].replace(',', '')))
    return result

def read_all_success_rates(path):
    result = []
    for r in range(256):
        result.append(read_success_rate_for_rule(r, path))
    return [rule for sublist in result for rule in sublist]