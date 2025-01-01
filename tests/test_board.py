from sudoku.board import Board
from sudoku.board import _check_valid_value
from sudoku.board import _check_no_duplicates


def test__check_valid_value():
    """ Test the _check_valid_value function """
    assert _check_valid_value(0), "Error in _check_valid_value."
    assert _check_valid_value(1), "Error in _check_valid_value."
    assert _check_valid_value(9), "Error in _check_valid_value."
    assert not _check_valid_value(10), "Error in _check_valid_value."
    assert not _check_valid_value(-1), "Error in _check_valid_value."
    
    
def test__check_duplicates():
    """ Test the _check_duplicates function """
    assert _check_no_duplicates([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), \
        "Error in _check_duplicates."
    assert _check_no_duplicates([0, 1, 2, 3, 4, 5, 6, 7, 8, 0]), \
        "Error in _check_duplicates."
    assert not _check_no_duplicates([0, 1, 2, 1, 0]), \
        "Error in _check_duplicates."


def test_board_constructor():
    """ Test the constructor of the Board class """
    b = Board()

    for i in range(9):
        for j in range(9):
            assert b[i, j] == 0, \
                "Error in the __getitem__ method or in the "

    b[0, 0] = 1
    assert b[0, 0] == 1, "Error in the __setitem__ method"

    b[0, 1] = 1
    assert not b.isValid()

    b[0, 1] = 0

