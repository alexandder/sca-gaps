from copy import deepcopy

import lib.ca_lib as ca_lib


def fill_gaps_for_all_simulations(all_simulations, P):
    filled_simulations = []
    for sim in all_simulations:
        copy = deepcopy(sim)
        fill_gaps_from_top(copy, P)
        fill_gaps_from_bottom(copy, P)
        filled_simulations.append(copy)
    return filled_simulations


def fill_gaps_from_top(simulation, P):
    row_length = len(simulation[0])
    for i in range(1, len(simulation)):
        for j in range(0, row_length):
            nei = ''
            if j == 0 and simulation[i][j] == -1:
                nei = str(simulation[i - 1][row_length - 1]) + str(simulation[i - 1][0]) + str(simulation[i - 1][1])
            elif j == row_length - 1 and simulation[i][j] == -1:
                nei = str(simulation[i - 1][row_length - 2]) + str(simulation[i - 1][row_length - 1]) + str(simulation[i - 1][0])
            elif simulation[i][j] == -1:
                nei = str(simulation[i - 1][j - 1]) + str(simulation[i - 1][j]) + str(simulation[i - 1][j + 1])
            if nei != '' and P[nei] == 0:
                simulation[i][j] = 0
            elif nei != '' and P[nei] == 1:
                simulation[i][j] = 1


def fill_gaps_from_bottom(simulation, P):
    row_length = len(simulation[0])
    for i in range(len(simulation) - 2, 0, -1):
        for j in range(0, row_length):
            nei = ''
            c1, c2, c3, c4 = 0, 0, 0, 0
            if simulation[i][j] == -1:
                if j == 0:
                    nei = str(simulation[i - 1][row_length - 1]) + str(simulation[i - 1][0]) + str(simulation[i - 1][1])
                    c1 = simulation[i][row_length - 2]
                    c2 = simulation[i][row_length - 1]
                    c3 = simulation[i][1]
                    c4 = simulation[i][2]
                elif j == 1:
                    nei = str(simulation[i - 1][0]) + str(simulation[i - 1][1]) + str(simulation[i - 1][2])
                    c1 = simulation[i][row_length - 1]
                    c2 = simulation[i][0]
                    c3 = simulation[i][2]
                    c4 = simulation[i][3]
                elif j == row_length - 2:
                    nei = str(simulation[i - 1][row_length - 3]) + str(simulation[i - 1][row_length - 2]) + str(
                        simulation[i - 1][row_length - 1])
                    c1 = simulation[i][row_length - 4]
                    c2 = simulation[i][row_length - 3]
                    c3 = simulation[i][row_length - 1]
                    c4 = simulation[i][0]
                elif j == row_length - 1:
                    nei = str(simulation[i - 1][row_length - 2]) + str(simulation[i - 1][row_length - 1]) + str(
                        simulation[i - 1][0])
                    c1 = simulation[i][row_length - 3]
                    c2 = simulation[i][row_length - 2]
                    c3 = simulation[i][0]
                    c4 = simulation[i][1]
                else:
                    nei = str(simulation[i - 1][j - 1]) + str(simulation[i - 1][j]) + str(simulation[i - 1][j + 1])
                    c1 = simulation[i][j - 2]
                    c2 = simulation[i][j - 1]
                    c3 = simulation[i][j + 1]
                    c4 = simulation[i][j + 2]
                A1 = P[str(c1) + str(c2) + str(1)] * P[str(c2) + str(1) + str(c3)] * P[str(1) + str(c3) + str(c4)]
                A0 = P[str(c1) + str(c2) + str(0)] * P[str(c2) + str(0) + str(c3)] * P[str(0) + str(c3) + str(c4)]
                P1 = P[nei] * A1
                P0 = (1 - P[nei]) * A0
                if P1 > P0:
                    simulation[i][j] = 1
                else:
                    simulation[i][j] = 0
