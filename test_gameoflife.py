import unittest

import gameoflife as gol


class TestGame(unittest.TestCase):
    def test_generate_gamestate(self):
        """Test gamestate is correctly initialised from input"""
        input = [
            "# #  ",
            "  # #",
            "###  ",
            "# # #"
        ]
        result = [
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 1, 1, 0, 0],
            [1, 0, 1, 0, 1]
        ]
        self.assertEqual(gol.generate_gamestate(input), result)
