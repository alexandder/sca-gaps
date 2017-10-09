import unittest
import simulations
import introduce_gaps
import lib.ca_lib as ca_lib

class Test_can_be_introduced(unittest.TestCase):

    def test_one(self):
        simulation = [
            [1, 1, 1, 0, 1],
            [-1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 0), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 1), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 2), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 3), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 4), "")

    def test_two(self):
        simulation = [
            [1, 1, 1, 0, 1],
            [0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 0), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 1), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 2), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 3), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 4), "")

    def test_three(self):
        simulation = [
            [1, 1, 1, 0, 1],
            [0, 0, -1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 0), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 1), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 2), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 3), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 4), "")

    def test_four(self):
        simulation = [
            [1, 1, 1, 0, 1],
            [0, 0, 0, -1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 0), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 1), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 2), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 3), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 4), "")

    def test_five(self):
        simulation = [
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0]
        ]
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 0), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 1), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 2), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 3), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 4), "")

    def test_row_one(self):
        simulation = [
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0]
        ]
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 1), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 2), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 3), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 4), "")

    def test_row_two(self):
        simulation = [
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [0, -1, 0, 0, 0]
        ]
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 2), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 3), "")
        self.assertTrue(simulations.can_be_introduced(simulation, 2, 4), "")

    def test_row_three(self):
        simulation = [
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, -1, 0, 0]
        ]
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 3), "")
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 4), "")

    def test_row_four(self):
        simulation = [
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0]
        ]
        self.assertFalse(simulations.can_be_introduced(simulation, 2, 4), "")

class Test_introduce_gaps(unittest.TestCase):

    def test_introduce(self):

        simulation = [
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0]
        ]

        introduce_gaps.introduce_gaps_for_simulation(simulation, 10)
        ca_lib.print_simulation_as_table(simulation)
