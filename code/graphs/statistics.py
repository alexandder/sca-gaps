import logs_reader as logs_reader
import numpy as np

# all_success_rates = logs_reader.read_all_success_rates('../logs/0.05/')
# print(np.average(all_success_rates))

def fmt(d):
    return "{0:.2f} \%".format(d*100.0)

def calculate_for_success_rates(success_rates):
    result = {'min': fmt(min(success_rates)),
               '5p': fmt(np.percentile(success_rates, 5)),
              'avg': fmt(np.average(success_rates)),
              'max': fmt(max(success_rates)),
              'sd': fmt(np.std(success_rates))}
    return result

def calculate(path):
    result = {}
    for lmb in [0.1, 0.2, 0.3, 0.4]:
        result[str(lmb)] = calculate_for_success_rates(logs_reader.read_success_rates_for_alpha(lmb, path))
    
    result['all'] = calculate_for_success_rates(logs_reader.read_all_success_rates(path))
    return result


result = calculate('../logs/0.05/')

for r in result:
    print(r + " & "+ " & ".join([result[r][p] for p in result[r]])+" \\\\")




