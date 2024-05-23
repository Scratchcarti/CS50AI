"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for row in board:
        for column in row:
            if column == X:
                xcount += 1
            if column == O:
                ocount += 1

    if xcount == ocount:
        return X
    if xcount > ocount:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_action = set()
    for index, row in enumerate(board):
        for ind, column in enumerate(row):
            if column == EMPTY:
                all_action.add((index, ind))

    return all_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Sorry, invalid action")

    copy_board = board[:]
    i, j = action
    copy_board[i][j] = player(copy_board)
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # diagonal
    if (board[0][0] == board[1][1] == board[2][2]):
        return board[1][1]

    if (board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]

    # rows

    for i in range(3):
        x, o = 0, 0
        for j in range(3):
            if (board[j][i] == X):
                x += 1
            if (board[j][i] == O):
                o += 1
            if x == 3:
                return X
            if o == 3:
                return O

    for i in range(3):
        x, o = 0, 0
        for j in range(3):
            if (board[i][j] == X):
                x += 1
            if (board[i][j] == O):
                o += 1

            if x == 3:
                return X
            if o == 3:
                return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not EMPTY:
        return True

    ncount = 0
    for i in board:
        for j in i:
            if j == EMPTY:
                ncount += 1

    if ncount == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
