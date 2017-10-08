import random

def can_be_introduced(simulation, row, column):
    row_length = len(simulation[0])
    if column == 0:
        return simulation[row - 1][row_length - 1] != -1 and simulation[row - 1][column] != -1 \
               and simulation[row - 1][column + 1] != -1 and simulation[row][row_length - 2] != -1 \
               and simulation[row][row_length - 1] != -1
    elif column == 1:
        return simulation[row - 1][0] != -1 and simulation[row - 1][column] != -1 \
               and simulation[row - 1][column + 1] != -1 and simulation[row][row_length - 1] != -1 \
               and simulation[row][0] != -1
    elif column == row_length - 2:
        return simulation[row - 1][row_length - 3] != -1 and simulation[row - 1][row_length - 2] != -1 \
               and simulation[row - 1][row_length - 1] != -1 and simulation[row][column - 2] != -1 \
               and simulation[row][column - 1] != -1 and simulation[row][0] != -1
    elif column == row_length - 1:
        return simulation[row - 1][row_length - 2] != -1 and simulation[row - 1][row_length - 1] != -1 \
               and simulation[row - 1][0] != -1 and simulation[row][column - 2] != -1 \
               and simulation[row][column - 1] != -1 and simulation[row][0] != -1 and simulation[row][1] != -1
    else:
        return simulation[row - 1][column - 1] != -1 and simulation[row - 1][column] != -1 \
               and simulation[row - 1][column + 1] != -1 and simulation[row][column - 2] != -1 \
               and simulation[row][column - 1] != -1



def introduce_gaps_for_simulation(simulation, probability):
    for i in range(1, len(simulation) - 1):
        for j in range(len(simulation[i])):
            random_number = random.random()
            if random_number < probability and can_be_introduced(simulation, i, j):
                simulation[i][j] = -1
    return simulation