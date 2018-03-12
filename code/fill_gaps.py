import random
from copy import deepcopy

import ca_lib as ca_lib


def fill_gaps_for_all_simulations(r1, r2, all_simulations, P, estimated_alpha):
    filled_simulations = []
    gaps_filled_from_top = []
    gaps_filled_from_bottom = []
    gaps_filled_randomly = []
    for sim in all_simulations:
        copy = deepcopy(sim)
        gaps_filled_from_top.append(fill_gaps_from_top(copy, P))
        gaps_bottom, gaps_randomly = fill_gaps_from_bottom(r1, r2, copy, P, estimated_alpha)
        gaps_filled_from_bottom.append(gaps_bottom)
        gaps_filled_randomly.append(gaps_randomly)
        filled_simulations.append(copy)
    return filled_simulations, gaps_filled_from_top, gaps_filled_from_bottom, gaps_filled_randomly


def fill_gaps_from_top(simulation, P):
    row_length = len(simulation[0])
    gaps_filled_from_top = 0
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
                gaps_filled_from_top += 1
            elif nei != '' and P[nei] == 1:
                simulation[i][j] = 1
                gaps_filled_from_top += 1
    return gaps_filled_from_top

def find_p_h_y(r1, r2, left, center, right, result, estimated_alpha):
    if ca_lib.apply_rule(r1, left, center, right) == ca_lib.apply_rule(r2, left, center, right):
        if result != ca_lib.apply_rule(r1, left, center, right):
            return 0
        else:
            return 1
    else:
        if result == ca_lib.apply_rule(r1, left, center, right):
            return estimated_alpha
        else:
            return 1 - estimated_alpha

def fill_gaps_from_bottom(r1, r2, simulation, P, estimated_alpha):
    row_length = len(simulation[0])
    gaps_filled_from_bottom = 0
    gaps_filled_randomly = 0
    for i in range(len(simulation) - 2, 0, -1):
        for j in range(0, row_length):
            if simulation[i][j] == -1:
                nei = str(access_cell(simulation, i - 1, j - 1)) + str(access_cell(simulation, i - 1, j)) + str(access_cell(simulation, i - 1, j+1))
                c1 = access_cell(simulation, i, j - 2)
                c2 = access_cell(simulation, i, j - 1)
                c3 = access_cell(simulation, i, j + 1)
                c4 = access_cell(simulation, i, j + 2)
                A1 = find_p_h_y(r1, r2, c1, c2, 1, access_cell(simulation, i + 1, j - 1), estimated_alpha) * \
                     find_p_h_y(r1, r2, c2, 1, c3, access_cell(simulation, i + 1, j), estimated_alpha) * \
                     find_p_h_y(r1, r2, 1, c3, c4, access_cell(simulation, i + 1, j + 1), estimated_alpha)
                A0 = find_p_h_y(r1, r2, c1, c2, 0, access_cell(simulation, i + 1, j - 1), estimated_alpha) * \
                     find_p_h_y(r1, r2, c2, 0, c3, access_cell(simulation, i + 1, j), estimated_alpha) * \
                     find_p_h_y(r1, r2, 0, c3, c4, access_cell(simulation, i + 1, j + 1), estimated_alpha)
                P1 = P[nei] * A1
                P0 = (1 - P[nei]) * A0
                if P1 == P0:
                    random_number = random.random()
                    if random_number < 0.5:
                        simulation[i][j] = 1
                    else:
                        simulation[i][j] = 0
                    gaps_filled_randomly += 1
                elif P1 > P0:
                    simulation[i][j] = 1
                else:
                    simulation[i][j] = 0
                gaps_filled_from_bottom += 1
    return gaps_filled_from_bottom, gaps_filled_randomly

def access_cell(simulation, i, j):
    row_length = len(simulation[i])
    if j >= row_length:
        j = j - row_length
    return simulation[i][j]

