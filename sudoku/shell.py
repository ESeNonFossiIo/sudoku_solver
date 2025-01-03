from termcolor import colored


def bold(value):
    """ Return a bold value.
        Args:
            value (str): Value to be bold.
        Returns:
            str: Bold value.
    """
    return f"\033[1m{value}\033[0m"


def print_board_difference(board1, board2):
    """ Print the board of the first and add the difference with the second in a different color.
        Args:
            board1 (numpy.array): First board.
            board2 (numpy.array): Second board.
    """
    for i in range(9):
        if i % 3 == 0:
            print("+---------+---------+---------+")
        for j in range(9):
            if j % 3 == 0:
                print("|", end="")
            if board1[i, j] == board2[i, j]:
                print(bold(f" {board1[i, j]} "), end="")
            else:
                print(colored(f" {board2[i, j]} ", 'red'), end="")
        print("|")
    print("+---------+---------+---------+")


def board_to_str(board):
    """ Return a string representation of the matrix.
        Args:
            board (numpy.array): Matrix to be represented.
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
            s += " {} ".format(board[i, j] == 0 and " " or board[i, j])
        s += "|" + "\n"
    s += "+---------+---------+---------+" + "\n"
    return s