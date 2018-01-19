

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


def find_stats():
    file = open('results', 'w')
    for r in range(256):
        stat = get_stats_for_rule(r)
        print(stat)
        file.write(', '.join(stat))
        file.write('\n')
    file.close()

find_stats()