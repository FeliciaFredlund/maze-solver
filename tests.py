'''
DESCRIPTION
'''

import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    
    def test_maze_cell_coordinates(self):
        margin = 10
        num_cols = 10
        num_rows = 10
        cell_size = 10
        m2 = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size)
        self.assertEqual(
            m2._Maze__cells[0][0]._Cell__x1,
            margin
        )
        self.assertEqual(
            m2._Maze__cells[1][0]._Cell__x2,
            margin + cell_size + cell_size
        )
        self.assertEqual(
            m2._Maze__cells[0][1]._Cell__y1,
            margin + cell_size
        )
        self.assertEqual(
            m2._Maze__cells[1][2]._Cell__y2,
            margin + (2 * cell_size) + cell_size
        )

    def test_maze_break_entrance_and_exit(self):
        margin = 10
        num_cols = 12
        num_rows = 16
        cell_size = 20
        m3 = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size)
        self.assertFalse(
            m3._Maze__cells[0][0].has_top_wall
        )
        self.assertFalse(
            m3._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall
        )

    def test_reset_cells_visited(self):
        margin = 10
        num_cols = 12
        num_rows = 16
        cell_size = 20
        m4 = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size)
        self.assertFalse(
            m4._Maze__cells[0][0].visited
        )
        self.assertFalse(
            m4._Maze__cells[1][1].visited
        )
        self.assertFalse(
            m4._Maze__cells[num_cols - 1][num_rows - 1].visited
        )


if __name__ == "__main__":
    unittest.main()