import random

from agent import Agent
from board import Board

class RandomAgent(Agent):
    def getCol(self, board:Board) -> int:
        '''
        Return an random choice from all possible choices.
        We use this as baseline for other agents.
        '''
        while True:
            random_col = random.randint(0, board.getColumnCount() - 1)
            if board.is_valid_location(random_col):
                return random_col
