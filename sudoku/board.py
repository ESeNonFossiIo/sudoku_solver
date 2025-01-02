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


def _is_a_valid_board(board):
    """ Check if the board is valid. i.e., if there are no duplicates in rows, columns and sub-grids.
        Args:
            board (numpy.array): Board to be checked.
        Returns:
            bool: True if the board is valid, False otherwise.
    """
    for i in range(9):
        if not _check_no_duplicates(board[i, :]):
            return False
        if not _check_no_duplicates(board[:, i]):
            return False
    for i in range(3):
        for j in range(3):  
            ic, jc = 3 * i, 3 * j
            if not _check_no_duplicates(board[ic:ic + 3, jc:jc + 3].flatten()):
                return False
    return True


def _is_a_valid_board_values(values):
    """ TODO:
    """
    for i in range(9):
        for k in range(9):
            if not values[i, :, k].any():
                return False
            if not values[:, i, k].any():
                return False
    for i in range(3):
        for j in range(3):
            ic, jc = 3 * i, 3 * j
            for k in range(9):
                if not values[ic: ic + 3, jc: jc + 3, k].any():
                    return False
    return True


def _check_valid_value(value):
    """ Check if the value is valid, i.e., if it is between 0 and 9.
        Args:
            value (int): Value to be checked.
        Returns:
            bool: True if the value is valid, False otherwise.
    """
    return 0 <= value <= 9

# TODO: function to print difference between boards using colors


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

    @staticmethod
    def __get_matrix_as_string(matrix):
        """ Return a string representation of the matrix.
            Args:
                matrix (numpy.array): Matrix to be represented.
            Returns:
                str: String representation of the matrix.
        """
        s = ""
        for i in range(9):
            if i % 3 == 0:
                s += "+---------+---------+---------+" + "\n"
            for j in range(9):
                if j % 3 == 0:
                    s += "|"
                s += " {} ".format(matrix[i, j] == 0 and " " or matrix[i, j])
            s += "|" + "\n"
        s += "+---------+---------+---------+" + "\n"
        return s

    def __str__(self):
        """ Return a string representation of the board.
            Returns:
                str: String representation of the board.
        """
        return self.__get_matrix_as_string(self.__board)

    def values_matrix(self, index):
        """ Return a string representation of the values matrix.
            Args:
                index (int): Index of the values matrix.
            Returns:
                str: String representation of the values matrix.
        """
        return self.__get_matrix_as_string(self.__values[:, :, index-1]).replace('True', 'X').replace('False', ' ')

    def get_board(self):
        """ Return the board.
            Returns:
                numpy.array: Board.
        """
        return self.__board

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

    def n_missing_values(self):
        """ Return the number of missing values in the board.

            Returns:
                int: Number of missing values in the board.
        """
        return (self.__board == 0).sum()

    def isValid(self):
        """ Check if the board is valid. i.e., if there are no duplicates in rows, columns and sub-grids.

            Returns:
                bool: True if the board is valid, False otherwise.
        """
        return _is_a_valid_board(self.__board)

    def __update_values(self):
        """ Update the values of the board using the values of __board. """
        # Set all values of the rows, columns and sub-grids that contain a cell already computed
        # to False and teh cell itself to True.
        for i in range(9):
            for j in range(9):
                if self.__board[i, j] != 0:
                    index = self.__board[i, j] - 1
                    # Set the values of the line to False
                    self.__values[i, :, index] = False
                    # Set the values of the column to False
                    self.__values[:, j, index] = False
                    # Set the values of the sub-grid to False
                    ic, jc = 3 * (i // 3), 3 * (j // 3)
                    self.__values[ic:ic + 3, jc:jc + 3, index] = False
                    # Set the value of the cell to True
                    self.__values[i, j, :] = False
                    self.__values[i, j, index] = True

        # TODO
        for i in range(9):
            for j in range(9):
                if self.__board[i, j] == 0:
                    for k in range(0, 9):
                        # If all the true values are in the same sub-grid,
                        # then the other rows can be set to 0.
                        # Indices of the sub-grid
                        ig, jg = 3 * (i // 3), 3 * (j // 3)
                        # Rows:
                        nTrueRow = self.__values[i, :, k].sum()
                        nTrueRowSubGrid = self.__values[i, jg:jg + 3, k].sum()
                        if (nTrueRow == nTrueRowSubGrid) and (nTrueRow > 0):
                            for ii in range(3):
                                if ii != i % 3:
                                    self.__values[ig + ii, jg:jg + 3, k] = False
                        # Columns:
                        nTrueCol = self.__values[:, j, k].sum()
                        nTrueColSubGrid = self.__values[ig:ig + 3, j, k].sum()
                        if (nTrueCol == nTrueColSubGrid) and (nTrueCol > 0):
                            for jj in range(3):
                                if jj != j % 3:
                                    self.__values[ig:ig + 3, jg + jj, k] = False

    def __update_board(self):
        """ Update the board using the values of __values. """
        for j in range(9):
            for k in range(9):
                if self.__values[:, j, k].sum() == 1:
                    index = np.where(self.__values[:, j, k])[0][0]
                    self.__board[index, j] = k + 1
                elif self.__values[j, :, k].sum() == 1:
                    index = np.where(self.__values[j, :, k])[0][0]
                    self.__board[j, index] = k + 1
        for i in range(9):
            for j in range(9):
                if self.__values[i, j, :].sum() == 1:
                    index = self.available_values(i, j)[0]
                    self.__board[i, j] = index + 1
        for i in range(3):
            for j in range(3):
                ic, jc = 3 * i, 3 * j
                for k in range(9):
                    if self.__values[ic: ic + 3, jc: jc + 3, k].sum() == 1:
                        index = np.where(self.__values[3 * i:3 * i + 3, 3 * j:3 * j + 3, k])
                        iv, jv = [index[0][0], index[1][0]]
                        self.__board[ic + iv, jc + jv] = k + 1

    def set_matrix(self, matrix: list[list[int]]):
        """ Set the values of the board using a matrix.

            Args:
                matrix (list of lists): List of lists with the values of the board.
        """
        # TODO: assert matrix.shape == (9, 9)
        self.__board = np.array(matrix)
        # Reset the values of __values
        self.__values = np.ones((9, 9, 9), dtype=bool)
        self.__update_values()

    def random_board(self, seed=None):
        """ Generate a valid random board.
            Args:
                seed (int): Seed for the random number generator. Default is None.
            Returns:
                numpy.array: Random board.
        """

        if seed is not None:
            np.random.seed(seed)

        def _random_value(_board, _values):
            while True:
                i, j, k = np.random.randint(0, 9, 3)

                if _values[i, j, k]:
                    old_board = _board.copy()
                    old_values = _values.copy()
                    _board[i, j] = k + 1
                    _values[i, :, k] = False
                    _values[:, j, k] = False
                    ic, jc = 3 * (i // 3), 3 * (j // 3)
                    _values[ic:ic + 3, jc:jc + 3, k] = False
                    _values[i, j, :] = False
                    _values[i, j, k] = True
                    if _is_a_valid_board(_board) and _is_a_valid_board_values(_values):
                        return _board, _values
                    else:
                        # Revert
                        _board = old_board
                        _values = old_values
                        # Exclude this combination
                        _values[i, j, k] = False

        _board = np.zeros((9, 9), dtype=int)
        _values = np.ones((9, 9, 9), dtype=bool)
        do = True
        while do:
            _board, _values = _random_value(_board, _values)
            self.set_matrix(_board)
            do = not self.solve()

        return _board

    def available_values(self, i, j):
        """ Return the available values for a cell.
            Args:
                i (int): Row of the cell.
                j (int): Column of the cell.
            Returns:
                numpy.array: Available values for the cell.
        """
        return [v for v in range(9) if self.__values[i, j, v]]
        
    def discover_values(self):
        """ Discover the values of the board using the values of __values.
            If there is only one valid value for a cell, it is set in __board.
        """
        self.__update_board()
        self.__update_values()

    def solve(self):
        """ Solve the sudoku board.
            Returns:
                bool: True if the board was solved, False otherwise.
        """
        oldMissing = self.n_missing_values()
        do = True
        while do:
            self.discover_values()
            do = (oldMissing != self.n_missing_values())
            oldMissing = self.n_missing_values()
        return (self.n_missing_values() == 0)
