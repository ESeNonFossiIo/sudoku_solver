from sudoku import Board
import numpy as np


def test_board_solve():
    """ Test the solve method of the Board class. """

    board = Board()

    board.set_matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 8, 0, 0, 0, 3, 0, 0],
                      [0, 3, 0, 2, 0, 5, 0, 8, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 6, 4, 0, 8, 1, 0, 0],
                      [0, 4, 0, 0, 2, 0, 0, 9, 0],
                      [8, 0, 0, 0, 0, 0, 0, 0, 3],
                      [7, 0, 0, 3, 0, 1, 0, 0, 5],
                      [5, 6, 3, 0, 4, 0, 7, 2, 1]])

    board.solve()

    expected_solution = np.array(
      [[4, 7, 5, 6, 8, 3, 2, 1, 9],
       [6, 2, 8, 1, 9, 4, 3, 5, 7],
       [1, 3, 9, 2, 7, 5, 4, 8, 6],
       [2, 8, 7, 9, 1, 6, 5, 3, 4],
       [9, 5, 6, 4, 3, 8, 1, 7, 2],
       [3, 4, 1, 5, 2, 7, 6, 9, 8],
       [8, 1, 4, 7, 5, 2, 9, 6, 3],
       [7, 9, 2, 3, 6, 1, 8, 4, 5],
       [5, 6, 3, 8, 4, 9, 7, 2, 1]]
      )

    assert (board.get_board() == expected_solution).all()
