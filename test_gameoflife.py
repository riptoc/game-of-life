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

    def test_random_gamestate_input(self):
        """Test generation of random gamestate"""
        # Should return a list
        self.assertIsInstance(gol.random_gamestate_input(10, 10), list)
        # Each list item should be a string
        for i in gol.random_gamestate_input(10, 5):
            self.assertIsInstance(i, str)
            # Each string should only contain #s or spaces
            for j in i:
                self.assertIn(j, ("#", " "))

    def test_count_neighbours(self):
        """
            Test counting of a cell's neighbours is correct
            Test that edge wrapping is working
        """
        state = [
            [0, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [0, 0, 1, 1]
        ]

        self.assertEqual(gol.count_neighbours(1, 1, state), 4)
        self.assertEqual(gol.count_neighbours(2, 2, state), 5)
        self.assertEqual(gol.count_neighbours(3, 0, state), 5)
        self.assertEqual(gol.count_neighbours(4, 3, state), 4)
        self.assertEqual(gol.count_neighbours(0, 0, state), 5)


if __name__ == '__main__':
    unittest.main()
