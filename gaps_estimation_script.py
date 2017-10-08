import random
from copy import deepcopy

elementary_neighborhoods = ['000', '001', '010', '011', '100', '101', '110', '111']



initial_configurations = [[1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
[0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
[1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
[1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],
[0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
[1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
[1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
[0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
[1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
[0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
[0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
[0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
[1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
[1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
[0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
[1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1],
[0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
[0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
[1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
[0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
[0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
[1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
[0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
[0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
[0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
[0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
[0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
[1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1],
[0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
[0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
[1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
[1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
[1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
[0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]]

def binP(N, p, x1, x2):
    p = float(p)
    q = p / (1 - p)
    k = 0.0
    v = 1.0
    s = 0.0
    tot = 0.0

    while (k <= N):
        tot += v
        if (k >= x1 and k <= x2):
            s += v
        if (tot > 10 ** 30):
            s = s / 10 ** 30
            tot = tot / 10 ** 30
            v = v / 10 ** 30
        k += 1
        v = v * q * (N + 1 - k) / k
    return s / tot


def calcBin(vx, vN, vCL=95):
    '''
    Calculate the exact confidence interval for a binomial proportion

    Usage:
    >>> calcBin(13,100)
    (0.07107391357421874, 0.21204372406005856)
    >>> calcBin(4,7)
    (0.18405151367187494, 0.9010086059570312)
    '''
    vx = float(vx)
    vN = float(vN)
    # Set the confidence bounds
    vTU = (100 - float(vCL)) / 2
    vTL = vTU

    vP = vx / vN
    if (vx == 0):
        dl = 0.0
    else:
        v = vP / 2
        vsL = 0
        vsH = vP
        p = vTL / 100

        while ((vsH - vsL) > 10 ** -5):
            if (binP(vN, v, vx, vN) > p):
                vsH = v
                v = (vsL + v) / 2
            else:
                vsL = v
                v = (v + vsH) / 2
        dl = v

    if (vx == vN):
        ul = 1.0
    else:
        v = (1 + vP) / 2
        vsL = vP
        vsH = 1
        p = vTU / 100
        while ((vsH - vsL) > 10 ** -5):
            if (binP(vN, v, 0, vx) < p):
                vsH = v
                v = (vsL + v) / 2
            else:
                vsL = v
                v = (v + vsH) / 2
        ul = v
    return (dl, ul)


def apply_rule(number, l, c, r):
    binary_rule_number = format(number, "#010b")[2:]
    neighborhood = int(str(l) + str(c) + str(r), 2)
    position = -neighborhood + 7
    return int(binary_rule_number[position])

def apply_stochastic_rule(rule1, rule2, l, c, r, alpha):
    if alpha < 0 or alpha > 1:
        raise Exception('Wrong alpha: ' + str(alpha))
    random_number = random.random()
    if random_number < alpha:
        return apply_rule(rule1, l, c, r)
    return apply_rule(rule2, l, c, r)

def apply_stochastic_rule_to_vector(input_configuration, rule1, rule2, alpha):
    result = []
    for i in range(len(input_configuration)):
        if i == len(input_configuration) - 1:
            result.append(apply_stochastic_rule(rule1, rule2, input_configuration[i - 1], input_configuration[i], input_configuration[0], alpha))
        elif i == 0:
            result.append(apply_stochastic_rule(rule1, rule2, input_configuration[len(input_configuration) - 1], input_configuration[i], input_configuration[i + 1], alpha))
        else:
            result.append(apply_stochastic_rule(rule1, rule2, input_configuration[i - 1], input_configuration[i], input_configuration[i + 1], alpha))
    return result

def simulate(initial, T, rule1, rule2, alpha):
    res = [initial]
    for k in range(T):
        res.append(apply_stochastic_rule_to_vector(res[len(res) - 1], rule1, rule2, alpha))
    return res


def get_number_of_neighborhoods(simulation):
    result = {"111": {'0': 0, '1': 0}, "110": {'0': 0, '1': 0}, "101": {'0': 0, '1': 0}, "100": {'0': 0, '1': 0},
              "011": {'0': 0, '1': 0}, "001": {'0': 0, '1': 0}, "010": {'0': 0, '1': 0}, "000": {'0': 0, '1': 0}}
    for t in range(len(simulation) - 1):
        for i in range(len(simulation[t])):
            vector = simulation[t]
            rule_result = str(simulation[t+1][i])
            if i == 0:
                index = str(vector[len(vector) - 1]) + str(vector[i]) + str(vector[i + 1])
                result[index][rule_result] = result[index][rule_result] + 1
            elif i == len(vector) - 1:
                index = str(vector[i - 1]) + str(vector[i]) + str(vector[0])
                result[index][rule_result] = result[index][rule_result] + 1
            else:
                index = str(vector[i - 1]) + str(vector[i]) + str(vector[i + 1])
                result[index][rule_result] = result[index][rule_result] + 1
    return result

def skip_neighborhood(i, vector):
    if i == 0 and (vector[len(vector) - 1] == -1 or vector[i] == -1 or vector[i+1] == -1):
        return True
    elif i == len(vector) - 1 and (vector[i-1] == -1 or vector[i] == -1 or vector[0]):
        return True
    elif i != 0 and i != len(vector) - 1 and (vector[i - 1] == -1 or vector[i] == -1 or vector[i + 1] == -1):
        return True
    return False

def get_number_of_neighborhoods_with_gaps(simulation):
    result = {"111": {'0': 0, '1': 0}, "110": {'0': 0, '1': 0}, "101": {'0': 0, '1': 0}, "100": {'0': 0, '1': 0},
              "011": {'0': 0, '1': 0}, "001": {'0': 0, '1': 0}, "010": {'0': 0, '1': 0}, "000": {'0': 0, '1': 0}}
    for t in range(len(simulation) - 1):
        vector = simulation[t]
        for i in range(len(simulation[t])):
            rule_result = str(simulation[t+1][i])
            if rule_result != str(-1):
                if i == 0 and not skip_neighborhood(i, vector):
                    index = str(vector[len(vector) - 1]) + str(vector[i]) + str(vector[i + 1])
                    result[index][rule_result] = result[index][rule_result] + 1
                elif i == len(vector) - 1 and not skip_neighborhood(i, vector):
                    index = str(vector[i - 1]) + str(vector[i]) + str(vector[0])
                    result[index][rule_result] = result[index][rule_result] + 1
                elif not skip_neighborhood(i, vector):
                    index = str(vector[i - 1]) + str(vector[i]) + str(vector[i + 1])
                    result[index][rule_result] = result[index][rule_result] + 1
    return result

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

def perform_simulation_and_introduce_gaps_for_rules(I, rule1, rule2, alpha, N, T, gap_probability, all_simulations, all_simulations_with_gaps):
    simulation = simulate(I, T, rule1, rule2, alpha)
    all_simulations.append(deepcopy(simulation))
    simulation = introduce_gaps_for_simulation(simulation, gap_probability)
    all_simulations_with_gaps.append(deepcopy(simulation))
    return get_number_of_neighborhoods_with_gaps(simulation)


def merge_number_of_neighborhoods(result, simulated):
    for nei in elementary_neighborhoods:
        result[nei]['0'] = result[nei]['0'] + simulated[nei]['0']
        result[nei]['1'] = result[nei]['1'] + simulated[nei]['1']
    return result


def perform_simulations(rule1, rule2, alpha, N, T, gap_probability):
    total_number_of_neighborhoods = {"111": {'0': 0, '1': 0}, "110": {'0': 0, '1': 0}, "101": {'0': 0, '1': 0},
                                     "100": {'0': 0, '1': 0},
                                     "011": {'0': 0, '1': 0}, "001": {'0': 0, '1': 0}, "010": {'0': 0, '1': 0},
                                     "000": {'0': 0, '1': 0}}
    all_simulations = []
    all_simulations_with_gaps = []
    for I in initial_configurations:
        simulated_number_of_neighborhoods = perform_simulation_and_introduce_gaps_for_rules(I, rule1, rule2, alpha, N, T, gap_probability, all_simulations, all_simulations_with_gaps)
        merge_number_of_neighborhoods(total_number_of_neighborhoods, simulated_number_of_neighborhoods)
    return total_number_of_neighborhoods, all_simulations, all_simulations_with_gaps

def find_probabilities(total_number_of_neighborhoods):
    P = {"111": 0, "110": 0, "101": 0, "100": 0, "011": 0, "010": 0, "001": 0, "000": 0}
    for nei in elementary_neighborhoods:
        P[nei] = 1.0 * total_number_of_neighborhoods[nei]['1'] / (
            total_number_of_neighborhoods[nei]['1'] + total_number_of_neighborhoods[nei]['0'])
    return P

def print_dict_of_total_number_of_neighborhoods(total_number_of_neighborhoods):
    for nei in elementary_neighborhoods:
        print(nei + ": " + total_number_of_neighborhoods[nei])
    print()

def get_intervals_for_simulations(rule1, rule2, alpha):
    result = []
    rules_matched = 'MATCH'
    success_rates = []
    for i in range(10):
        total_num, all_simulations, all_simulations_with_gaps = perform_simulations(rule1, rule2, alpha, 49, 49, 0.05)
        P = find_probabilities(total_num)
        filled_simulations = fill_gaps_for_all_simulations(all_simulations_with_gaps, P)
        total_number_of_gaps = get_total_number_of_gaps(all_simulations_with_gaps)
        total_number_of_failures = get_number_of_failures(all_simulations, filled_simulations)
        if total_number_of_gaps == 0:
            success_rates.append(1.0)
        else:
            success_rate = 1 - (total_number_of_failures/total_number_of_gaps*1.0)
            success_rates.append(success_rate)
        match = estimate_rules(P, rule1, rule2)
        alpha_L, alpha_U = calculate_confidence_interval(P, total_num)
        interval = {'alpha_L': alpha_L, 'alpha_U': alpha_U}
        result.append(interval)
        if match == 'NO_MATCH':
            rules_matched = match
    return result, rules_matched, success_rates

def calculate_confidence_interval(P, total_number_of_neighborhoods):
    nei_for_p_less_than_half = []
    nei_for_p_greater_than_half = []
    for nei in elementary_neighborhoods:
        if 0 < P[nei] < 0.5:
            nei_for_p_less_than_half.append(nei)
        elif 0.5 < P[nei] < 1.0:
            nei_for_p_greater_than_half.append(nei)
    N_STAR_less_than = 0
    for nei in nei_for_p_less_than_half:
        N_STAR_less_than += total_number_of_neighborhoods[nei]['1'] + total_number_of_neighborhoods[nei]['0']
    N_STAR_greater_than = 0
    for nei in nei_for_p_greater_than_half:
        N_STAR_greater_than += total_number_of_neighborhoods[nei]['1'] + total_number_of_neighborhoods[nei]['0']

    N_STAR = N_STAR_greater_than + N_STAR_less_than

    K_STAR = 0
    for nei in nei_for_p_greater_than_half:
        K_STAR += total_number_of_neighborhoods[nei]['0']
    for nei in nei_for_p_less_than_half:
        K_STAR += total_number_of_neighborhoods[nei]['1']

    if K_STAR != 0 and N_STAR != 0:
        alpha_L, alpha_U = calcBin(K_STAR, N_STAR)
        return alpha_L, alpha_U
    return 0, 0

def get_number_of_failures(all_simulations, all_filled_simulations):
    total_number_of_failures = 0
    for i in range(len(all_simulations)):
        for j in range(len(all_simulations[i])):
            for k in range(len(all_simulations[i][j])):
                if all_filled_simulations[i][j][k] != all_simulations[i][j][k]:
                    total_number_of_failures += 1
    return total_number_of_failures

def get_total_number_of_gaps(all_simulations_with_gaps):
    total_number_of_gaps = 0
    for i in range(len(all_simulations_with_gaps)):
        for j in range(len(all_simulations_with_gaps[i])):
            for k in range(len(all_simulations_with_gaps[i][j])):
                if all_simulations_with_gaps[i][j][k] == -1:
                    total_number_of_gaps += 1
    return total_number_of_gaps

def find_max_error(intervals, alpha):
    result = 0
    for interval in intervals:
        alpha_dash = (interval['alpha_L'] + interval['alpha_U']) / 2
        error = abs(alpha - alpha_dash) / abs(alpha)
        if error > result:
            result = error
    return result

def is_alpha_not_in_interval(interval, alpha):
    return interval['alpha_L'] > alpha or interval['alpha_U'] < alpha

def find_wrong_estimation_ratio(intervals, alpha):
    count = 0
    for interval in intervals:
        if is_alpha_not_in_interval(interval, alpha):
            count += 1
    return 1.0*count/len(intervals)

def find_max_distance(intervals, alpha):
    result = 0
    for interval in intervals:
        distance = 0
        if is_alpha_not_in_interval(interval, alpha):
            if interval['alpha_L'] > alpha:
                distance = abs(interval['alpha_L'] - alpha)
            else:
                distance = abs(interval['alpha_U'] - alpha)
        if distance > result:
            result = distance
    return result

def estimate_rules(P, rule1, rule2):
    rule1_est = []
    rule2_est = []
    for nei in P:
        if P[nei] == 0:
            rule1_est.append('0')
            rule2_est.append('0')
        elif P[nei] == 1:
            rule1_est.append('1')
            rule2_est.append('1')
        elif 0 < P[nei] < 0.5:
            rule1_est.append('1')
            rule2_est.append('0')
        else:
            rule1_est.append('0')
            rule2_est.append('1')
    if int(''.join(rule1_est), 2) == rule1 and int(''.join(rule2_est), 2) == rule2:
        return 'MATCH'
    else:
        return 'NO_MATCH ' + str(int(''.join(rule1_est), 2)) + ' ' + str(int(''.join(rule2_est), 2))



def estimate_all_rules(alphas):
    print("alpha, r1, r2, max_err, wrong_ration, max_dist, match, filling success rate")
    for r1 in [204]:
        for r2 in range(256):
            if r1 != r2:
                for a in alphas:
                    intervals, match, success_rates = get_intervals_for_simulations(r1, r2, a)
                    print(a, r1, r2, find_max_error(intervals, a),
                          find_wrong_estimation_ratio(intervals, a),
                          find_max_distance(intervals, a),
                          match, sum(success_rates) / len(success_rates))


rule1 = 0
rule2 = 16
alpha = 0.25
alphas = [0.1, 0.2, 0.3, 0.4]

estimate_all_rules(alphas)