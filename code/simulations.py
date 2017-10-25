from copy import deepcopy

import initial_configurations
import introduce_gaps as gaps
import lib.ca_data as ca_data
import lib.sca_lib as sca_lib


def perform_simulation_and_introduce_gaps_for_rules(I, rule1, rule2, alpha, N, T, gap_probability, all_simulations, all_simulations_with_gaps):
    simulation = sca_lib.simulate(I, T, rule1, rule2, alpha)
    all_simulations.append(deepcopy(simulation))
    simulation = gaps.introduce_gaps_for_simulation(simulation, int(N*T*gap_probability))
    all_simulations_with_gaps.append(deepcopy(simulation))
    return sca_lib.get_number_of_neighborhoods_with_gaps(simulation)


def merge_number_of_neighborhoods(result, simulated):
    elementary_neighborhoods = ca_data.elementary_neighborhoods
    for nei in elementary_neighborhoods:
        result[nei]['0'] = result[nei]['0'] + simulated[nei]['0']
        result[nei]['1'] = result[nei]['1'] + simulated[nei]['1']
    return result


def perform_simulations(K, rule1, rule2, alpha, N, T, gap_probability):
    total_number_of_neighborhoods = {"111": {'0': 0, '1': 0}, "110": {'0': 0, '1': 0}, "101": {'0': 0, '1': 0},
                                     "100": {'0': 0, '1': 0},
                                     "011": {'0': 0, '1': 0}, "001": {'0': 0, '1': 0}, "010": {'0': 0, '1': 0},
                                     "000": {'0': 0, '1': 0}}
    all_simulations = []
    all_simulations_with_gaps = []
    for I in initial_configurations.initial_configurations:
        simulated_number_of_neighborhoods = perform_simulation_and_introduce_gaps_for_rules(I, rule1, rule2, alpha, N, T, gap_probability, all_simulations, all_simulations_with_gaps)
        merge_number_of_neighborhoods(total_number_of_neighborhoods, simulated_number_of_neighborhoods)
    return total_number_of_neighborhoods, all_simulations, all_simulations_with_gaps

def find_probabilities(total_number_of_neighborhoods):
    P = {"111": 0, "110": 0, "101": 0, "100": 0, "011": 0, "010": 0, "001": 0, "000": 0}
    for nei in ca_data.elementary_neighborhoods:
        P[nei] = 1.0 * total_number_of_neighborhoods[nei]['1'] / (
            total_number_of_neighborhoods[nei]['1'] + total_number_of_neighborhoods[nei]['0'])
    return P

def print_dict_of_total_number_of_neighborhoods(total_number_of_neighborhoods):
    elementary_neighborhoods = ca_data.elementary_neighborhoods
    for nei in elementary_neighborhoods:
        print(nei + ": " + total_number_of_neighborhoods[nei])
    print()
