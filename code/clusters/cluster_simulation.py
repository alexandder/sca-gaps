
import numpy as np
import random
import sys
from collections import Counter
import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt
# import lib.ca_lib as ca_lib
# import lib.sca_lib as sca_lib
import initial_configurations as initial_configurations


def generate_simulation(N):
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        result.append(row)
    return result

def introduce_gaps(simulation, prob):
    counter = 1
    for i in range(1, len(simulation[0]) - 1):
        for j in range(len(simulation[0])):
            random_number = random.random()
            if random_number < prob:
                simulation[i][j] = counter
                counter += 1
    return simulation

def print_simulation(simulation):
    for row in simulation:
        for cell in row:
            sys.stdout.write(str(cell))
            sys.stdout.write(" ")
        sys.stdout.write("\n")

def access_cell(simulation, i, j):
    row_length = len(simulation[i])
    if j >= row_length:
        j = j - row_length
    return simulation[i][j]

def is_in_cluster(simulation, row_current, column_current, row_neighbor, column_neighbor):
    return access_cell()


def offset_column(column, row_length):
    if column >= row_length:
        return column - row_length
    return column

def process_cell(simulation, row, column, current_value, row_length):
    if access_cell(simulation, row, column) != 0:
        simulation[row][offset_column(column, row_length)] = min(current_value, access_cell(simulation, row, column))

def make_clusters(simulation):
    counter = 1
    row_length = len(simulation[0])
    for i in range(1, len(simulation[0]) - 1):
        for j in range(row_length):
            current_value = access_cell(simulation, i, j)
            if current_value != 0:
                process_cell(simulation, i - 1, j - 1, current_value, row_length)
                process_cell(simulation, i - 1, j, current_value, row_length)
                process_cell(simulation, i - 1, j + 1, current_value, row_length)
                process_cell(simulation, i, j - 2, current_value, row_length)
                process_cell(simulation, i, j - 1, current_value, row_length)
                process_cell(simulation, i, j + 1, current_value, row_length)
                process_cell(simulation, i, j + 2, current_value, row_length)
                process_cell(simulation, i + 1, j - 1, current_value, row_length)
                process_cell(simulation, i + 1, j, current_value, row_length)
                process_cell(simulation, i + 1, j + 1, current_value, row_length)
    return simulation

def count_clusters(simulation):
    result = {}
    for row in simulation:
        result = dict(Counter(result) + Counter(row))
    del result[0]
    return result

def find_max_cluster_size(counted_clusters, N):
    return 1.0*np.average(list(counted_clusters.values()))

def find_number_of_clusters(counted_clusters):
    return len(counted_clusters.keys())

def perform_simulation_of_maximal_cluster_size():
    probabilities = [0.005] + [1.0 * x / 80 for x in range(1, 20)]
    N = 49
    result = {}
    for p in probabilities:
        maximal = []
        for i in range(250):
            grouped_simulation = make_clusters(make_clusters(introduce_gaps(generate_simulation(N), p)))
            counted_clusters = count_clusters(grouped_simulation)
            maximal.append(find_max_cluster_size(counted_clusters, N))
        result[p] = 1.0*sum(maximal) / len(maximal)
    print(result)
    return result

def perform_simulation_of_number_of_clusters():
    probabilities = [0.005] + [1.0 * x / 20 for x in range(1, 20)]
    N = 49
    result = {}
    for p in probabilities:
        number = []
        for i in range(250):
            grouped_simulation = make_clusters(make_clusters(introduce_gaps(generate_simulation(N), p)))
            counted_clusters = count_clusters(grouped_simulation)
            number.append(find_number_of_clusters(counted_clusters))
        result[p] = 1.0*sum(number)/len(number)
    return result



def make_plot_cluster_size_probability(data, path):
    plt.plot(list(data.keys()), list(data.values()))
    plt.xlabel('probability')
    plt.ylabel('maximal cluster size as % of all cells')
    plt.savefig(path + 'cluster_size.pdf')
    plt.close()

def make_plot_for_number_of_clusters(data, path):
    plt.plot(list(data.keys()), list(data.values()))
    plt.xlabel('probability')
    plt.ylabel('number of clusters')
    plt.savefig(path + 'cluster_number.pdf')
    plt.close()

#make_plot_cluster_size_probability(perform_simulation_of_maximal_cluster_size(), '')
make_plot_for_number_of_clusters(perform_simulation_of_number_of_clusters(), '')







