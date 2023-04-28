'''
For Game UI, we borrowed idea form: https://github.com/KeithGalli/Connect4-Python
This repo is MIT License. We refactored and modified some of its code based on our own design.
'''

import numpy as np
import copy

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

class Board():
    def __init__(self, board = None, turn = 1):
        if board is None:
            '''
            Create an empty board, all elements are initialed as 0.
            '''
            self.board = np.zeros((ROW_COUNT, COLUMN_COUNT))
            self.turn = 1
        else:
            self.board = board
            self.turn = turn

    def drop_piece(self, col):
        '''
        Put piece on the position row, col.
        '''
        row = self.get_next_open_row(col)
        self.board[row][col] = self.turn
        self.turn = 3 - self.turn


    def is_valid_location(self, col):
        '''
        Check if the given column still has at least one zero on the top.
        If so it means there is still space to drop this piece, otherwise false.
        '''
        # print(self.board[ROW_COUNT-1][col])
        return self.board[ROW_COUNT-1][col] == 0

    def get_valid_locations(self):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def copy_board(self):
        c = copy.deepcopy(self)
        return c

    def get_next_open_row(self, col):
        '''
        Find the lowest row number that is zero, this is the location where the piece
        will go.
        '''
        for r in range(ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def get_board(self):
        '''
        Get current board.
        '''
        return self.board

    def print_board(self):
        '''
        Print the board into terminal.
        '''
        print(np.flip(self.board, 0))

    def winning_move(self, piece):
        '''
        Check if the piece(1 or 2) has won the game.
        '''
        # Check horizontal locations for win
        board = self.board
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

    def getColumnCount(self):
        return COLUMN_COUNT

    def getRowCount(self):
        return ROW_COUNT
