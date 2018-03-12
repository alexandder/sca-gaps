import graphs.logs_reader as logs_reader
import numpy as np

all_success_rates = logs_reader.read_all_success_rates('../logs/0.05/')
print(np.average(all_success_rates))

def calculate_for_success_rates(success_rates):
    result = {'min': min(success_rates),
              'avg': np.average(success_rates),
              '95p': np.percentile(success_rates, 95),
              'max': max(success_rates),
              'sd': np.std(success_rates)}
    return result

def calculate(path):
    result = {}
    result['all'] = calculate_for_success_rates(logs_reader.read_all_success_rates(path))
    for lmb in [0.1, 0.2, 0.3, 0.4]:
        result[str(lmb)] = calculate_for_success_rates(logs_reader.read_success_rates_for_alpha(lmb, path))
    return result


result = calculate('../logs/0.05/')
print(result['all'])
print(result['0.1'])
print(result['0.2'])
print(result['0.3'])
print(result['0.4'])



