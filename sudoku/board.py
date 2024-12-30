import numpy as np
from collections import Counter


def __assert_no_duplicates(values):
    """ Assert that there are no duplicates in the list of values.

        Args:
            values (list): List of values to be checked.
    """
    counter = Counter(values)
    for value, count in counter.items():
        assert (count <= 1) or (value == 0), "Duplicate non-0 value %d" % value


def __assert_valid_value(value):
    """ Assert that the value is valid.

        Args:
            value (int): Value to be checked.
    """
    assert 0 <= value <= 9, "Invalid value %d" % value


class Board(object):
    """ Class to represent a sudoku board
    """

    def __init__(self):
        """ Constructor """

        # Create a 9x9 numpy array to represent the board.
        # The first dimension of the matrix represent the row of the board,
        # while the second dimension represent the column of the board.
        # Value 0 means that the cell is empty.
        self.__board = np.zeros((9, 9), dtype=int)

        # Create a 9x9x9 numpy array to represent the board.
        # For each element of the board it defines which values are still
        # valid.
        self.__values = np.ones((9, 9, 9), dtype=bool)

    def __setitem__(self, key, value):
        """ Set the value of a cell in the board.

            Args:
                key (int, int): Tuple with the coordinates of the cell.
                value (int): Value to be set in the cell.
        """
        __assert_valid_value(value)
        self.__board[key] = value

    def isValid(self):
        """ Check if the board is valid.

            Returns:
                bool: True if the board is valid, False otherwise.
        """
        # Check if there are no duplicates in the rows and in the columns.
        for i in range(9):
            __assert_no_duplicates(self.__board[i, :])
            __assert_no_duplicates(self.__board[:, i])
        # Check if there are no duplicates in the 3x3 sub-grids.
        for i in range(3):
            for j in range(3):
                __assert_no_duplicates(
                    self.__board[3 * i:3 * i + 3, 3 * j:3 * j + 3].flatten())

    def __update_values(self):
        """ Update the values of the board. """
        for i in range(9):
            for j in range(9):
                if self.__board[i, j] != 0:
                    __assert_valid_value(self.__board[i, j])
                    self.__values[i, j, :] = False
                    self.__values[i, j, self.__board[i, j] - 1] = True
