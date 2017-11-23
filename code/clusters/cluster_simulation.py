import random

import sys

import lib.ca_lib as ca_lib
import lib.sca_lib as sca_lib
import initial_configurations as initial_configurations

#probability of gap introduction vs maximal cluster size

def generate_simulation(N):
    result = []
    for i in range(N):
        result.append(ca_lib.create_random_initial_vector(N))
    return result

def introduce_gaps(simulation, probability):
    for i in range(len(simulation)):
        for j in range(len(simulation[i])):
            r = random.random()
            if r < probability:
                simulation[i][j] = -1
    return simulation

def find_maximal_cluster_size(simulation):
    result = 0
    for i in range(len(simulation)):
        row_result = 0
        for j in range(len(simulation[i])):
            if simulation[i][j] == -1:
                row_result += 1
            else:
                if row_result > result:
                    result = row_result
                row_result = 0

    return result

def find_number_of_all_clusters(simulation):
    result = 0
    for i in range(len(simulation)):
        row_result = 0
        for j in range(len(simulation[i])):
            if simulation[i][j] == -1:
                row_result += 1
            else:
                if row_result > 1:
                    result += 1
                row_result = 0

    return result

def group_by_cluster_size(simulation):
    result = {}
    for i in range(len(simulation)):
        row_result = 0
        for j in range(len(simulation[i])):
            if simulation[i][j] == -1:
                row_result += 1
            else:
                if row_result > 1:
                    if row_result in result.keys():
                        result[row_result] += 1
                    else:
                        result[row_result] = 1
                row_result = 0
        print(row_result)
        for j in range(len(simulation[i])):
            if simulation[i][j] == -1:
                row_result += 1
            else:
                if row_result > 1:
                    if row_result in result.keys():
                        result[row_result] += 1
                    else:
                        result[row_result] = 1
                break
    return result

def perform_simulation_of_maximal_cluster_size():
    probabilities = [1.0 * x / 100 for x in range(1, 10)]
    N = 49
    result = {}
    for p in probabilities:
        maximal = 0
        for i in range(100):
            maximal_for_simulation = find_maximal_cluster_size(introduce_gaps(generate_simulation(N), p))
            if maximal_for_simulation > maximal:
                maximal = maximal_for_simulation
        result[p] = maximal
    return result


def calculate_results_for_simulation():
    p = 1
    simulation = introduce_gaps(generate_simulation(49), p)
    for vec in simulation:
        for v in vec:
            sys.stdout.write(str(v))
        print()
    print(find_maximal_cluster_size(simulation))
    print(find_number_of_all_clusters(simulation))
    print(group_by_cluster_size(simulation))

#print(perform_simulation_of_maximal_cluster_size())
calculate_results_for_simulation()







# probability of gap introduction vs number of clusters