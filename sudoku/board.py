import numpy as np
from collections import Counter


def _check_no_duplicates(values):
    """ Check if there are no duplicates in the list of values.
        Args:
            values (list): List of values.
        Returns:
            bool: True if there are no duplicates, False.
                Zero values are ignored.
    """
    return all([(count <= 1) or (value == 0)
                for value, count in Counter(values).items()])


def _check_valid_value(value):
    """ Check if the value is valid, i.e., if it is between 0 and 9.
        Args:
            value (int): Value to be checked.
        Returns:
            bool: True if the value is valid, False otherwise.
    """
    return 0 <= value <= 9


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

    def __str__(self):
        """ Return a string representation of the board.
            Returns:
                str: String representation of the board.
        """
        s = ""
        for i in range(9):
            if i % 3 == 0:
                s += "+---------+---------+---------+" + "\n"
            for j in range(9):
                if j % 3 == 0:
                    s += "|"
                s += " {} ".format(self.__board[i, j])
            s += "|" + "\n"
        s += "+---------+---------+---------+" + "\n"
        return s

    def __setitem__(self, key, value):
        """ Set the value of a cell in the board.

            Args:
                key (int, int): Tuple with the coordinates of the cell.
                value (int): Value to be set in the cell.
        """
        assert _check_valid_value(value)
        self.__board[key] = value
        # TODO: can we avoid updating all the values? just work on key?
        self.__update_values() 

    def __getitem__(self, key):
        """ Get the value of a cell in the board.

            Args:
                key (int, int): Tuple with the coordinates of the cell.

            Returns:
                int: Value of the cell.
        """
        return self.__board[key]

    def isValid(self):
        """ Check if the board is valid. i.e., if there are no duplicates in rows, columns and sub-grids.
        
            Returns:
                bool: True if the board is valid, False otherwise.
        """
        # Check if there are no duplicates in the rows, columns and sub-grids.
        if not all([_check_no_duplicates(self.__board[i, :]) for i in range(9)]):
            return False
        elif not all([_check_no_duplicates(self.__board[:, i]) for i in range(9)]):
            return False
        elif not all([_check_no_duplicates(self.__board[3 * i:3 * i + 3, 3 * j:3 * j + 3].flatten())
                      for i in range(3) for j in range(3)]):
            return False
        else:
            return True

    def __update_values(self):
        """ Update the values of __values using the values of __board.
            If the value of a cell of __board is not zero,
            the corresponding values in __values are set to True
            and all the other values are set to False.
        """
        # TODO:

    def set_matrix(self, matrix: list[list[int]]):
        """ Set the values of the board using a matrix.

            Args:
                matrix (list of lists): List of lists with the values of the board.
        """
        # TODO: assert matrix.shape == (9, 9)
        self.__board = np.array(matrix)
        self.__update_values()

    def discover_values(self):
        """ Discover the values of the board using the values of __values.
            If there is only one valid value for a cell, it is set in __board.
        """
        self.__update_values()
        for i in range(9):
            for j in range(9):
                if self.__board[i, j] == 0:
                    # There is only one valid value for the cell
                    print(np.sum(self.__values[i, j, :]), end=",   ")
                    if np.sum(self.__values[i, j, :]) == 1:
                        valid_values = np.where(self.__values[i, j, :])[0]
                        print(valid_values)
                        self.__board[i, j] = valid_values[0] + 1
