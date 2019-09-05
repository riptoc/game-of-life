import unittest

import gameoflife as gol


class TestGame(unittest.TestCase):
    def test_generate_gamestate(self):
        """Test gamestate is correctly initialised from input"""
        input = [
            "#-#--",
            "--#-#",
            "###--",
            "#-#-#"
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
                self.assertIn(j, ("#", "-"))

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

        self.assertEqual(gol.live_neighbours(1, 1, state), 4)
        self.assertEqual(gol.live_neighbours(2, 2, state), 5)
        self.assertEqual(gol.live_neighbours(3, 0, state), 5)
        self.assertEqual(gol.live_neighbours(4, 3, state), 4)
        self.assertEqual(gol.live_neighbours(0, 0, state), 5)

    def test_generate_next_gamestate(self):
        current = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 0]
        ]
        new = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(gol.get_next_gamestate(current), new)

    # Tests calculating the next cellstate
    def test_live_dies_with_under_2_live_neighbours(self):
        self.assertEqual(gol.next_cellstate(1, 1), 0)
        self.assertEqual(gol.next_cellstate(1, 0), 0)

    def test_live_cell_dies_with_over_3_live_neighbours(self):
        self.assertEqual(gol.next_cellstate(1, 4), 0)
        self.assertEqual(gol.next_cellstate(1, 6), 0)

    def test_live_cell_with_2_or_3_neighbours_lives(self):
        self.assertEqual(gol.next_cellstate(1, 2), 1)
        self.assertEqual(gol.next_cellstate(1, 3), 1)

    def test_dead_cell_with_3_neighbours_becomes_live(self):
        self.assertEqual(gol.next_cellstate(0, 3), 1)

    def test_dead_cell_with_not_3_neighbous_stays_dead(self):
        self.assertEqual(gol.next_cellstate(0, 2), 0)
        self.assertEqual(gol.next_cellstate(0, 0), 0)
        self.assertEqual(gol.next_cellstate(0, 4), 0)

    def test_gamestate_import_from_file(self):
        gs = [
            "------------------",
            "----#--------#----",
            "--#-#------#-#----",
            "---##-------##----",
            "------------------",
            "------------------",
            "----------#-------",
            "--------#-#-------",
            "---------##-------",
            "------------------"
        ]
        self.assertEqual(gol.import_gamestate('gamestate.txt'), gs)


if __name__ == '__main__':
    unittest.main()
