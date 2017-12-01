import random

import sys

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

def perform_simulation_of_maximal_cluster_size():
    probabilities = [1.0 * x / 100 for x in range(1, 15)]
    N = 49
    result = {}
    for p in probabilities:
        maximal = 0
        for i in range(1000):
            maximal_for_simulation = 1
            if maximal_for_simulation > maximal:
                maximal = maximal_for_simulation
        result[p] = maximal
    return result

print_simulation(introduce_gaps(generate_simulation(10), 0.2))

# def make_plot_cluster_size_probability(data, path):
#     plt.plot(list(data.keys()), list(data.values()))
#     plt.xlabel('probability')
#     plt.ylabel('maximal cluster size')
#     plt.title('Maximal cluster size vs probability of introducing gap')
#     plt.savefig(path + 'cluster_size.pdf')
#     plt.close()
#
# def make_plot_for_number_of_clusters(data, path):
#     plt.plot(list(data.keys()), list(data.values()))
#     plt.xlabel('probability')
#     plt.ylabel('number of clusters')
#     plt.title('Number of clusters vs probability of introducing gap')
#     plt.savefig(path + 'cluster_number.pdf')
#     plt.close()

#print(perform_simulation_of_maximal_cluster_size())
#calculate_results_for_simulation()







