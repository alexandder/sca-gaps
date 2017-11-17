import unittest
import simulations
import introduce_gaps
import lib.ca_lib as ca_lib

class Test_can_be_introduced(unittest.TestCase):

    def test_fill_gaps_from_top(self):
        P = []