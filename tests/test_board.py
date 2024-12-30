from sudoku.board import Board


def test_board_constructor():
    """ Test the constructor of the Board class """
    b = Board()

    for i in range(9):
        for j in range(9):
            assert b(i, j) == 0, "Error in the constructor"
