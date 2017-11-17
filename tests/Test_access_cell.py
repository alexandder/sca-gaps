import unittest
import fill_gaps
import simulations
import introduce_gaps
import lib.ca_lib as ca_lib

class Test_access_celle(unittest.TestCase):

    def test_one(self):
        simulation = [
            [0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 1],
        ]
        self.assertEqual(0, fill_gaps.access_cell(simulation, 0, 0))
        self.assertEqual(1, fill_gaps.access_cell(simulation, 0, 5))
        self.assertEqual(1, fill_gaps.access_cell(simulation, 0, 4))
        self.assertEqual(1, fill_gaps.access_cell(simulation, 1, 1))
        self.assertEqual(0, fill_gaps.access_cell(simulation, 1, 3))
        self.assertEqual(0, fill_gaps.access_cell(simulation, 2, 0))

    def test_two(self):
        simulation = [
            [0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 1],
        ]
        self.assertEqual(1, fill_gaps.access_cell(simulation, 0, -1))
        self.assertEqual(1, fill_gaps.access_cell(simulation, 0, -2))
        self.assertEqual(0, fill_gaps.access_cell(simulation, 0, 6))
        self.assertEqual(0, fill_gaps.access_cell(simulation, 0, 7))
        self.assertEqual(1, fill_gaps.access_cell(simulation, 1, -1))
        self.assertEqual(0, fill_gaps.access_cell(simulation, 1, -2))
        self.assertEqual(0, fill_gaps.access_cell(simulation, 1, 6))
        self.assertEqual(1, fill_gaps.access_cell(simulation, 1, 7))

