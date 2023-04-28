import random
import numpy as np

from agent import Agent
from game_controller import GameController
from random_agent import RandomAgent
from board import Board

class MonteCarloAgent(Agent):
    def GetPossibleMoves(self, board):
        '''
        Get all possible valid moves as a list.
        '''
        possible_choices = []
        for col in range(7):
            if board.is_valid_location(col):
                possible_choices.append(col)
        return possible_choices

    def getCol(self, board:Board):
        '''
        Play a move, using monte carlo simulation to get the best choice.
        '''
        possible_choices = self.GetPossibleMoves(board)
        my_turn = board.turn
        best_choice = -1
        best_winning_rate = 0
        
        for choice in possible_choices:
            # Iterate each possible choice, play it and use ranomd to simulate until finish
            # Cacluate the winning rate of each choice.
            turn = board.turn

            # Copy the board and play the choice.
            test_game = Board(board = np.copy(board.board), turn = turn)
            test_game.drop_piece(choice)
            test_board = np.copy(test_game.board)
            winning_chance = 0

            # Iterate 100 times, randomly play until game end.
            for i in range(100):
                test_game = Board(board = np.copy(test_board))
                done = test_game.winning_move(turn)
                turn = 3 - turn
                while not done:
                    moves = self.GetPossibleMoves(test_game)
                    if len(moves) == 0:
                        break
                    move = random.choice(moves)
                    test_game.drop_piece(move)
                    if test_game.winning_move(turn):
                        done = True
                        if turn == my_turn:
                            winning_chance += 1
                    turn = 3 - turn
            
            # Choose the choice that has best winning rate.
            if winning_chance > best_winning_rate:
                best_winning_rate = winning_chance
                best_choice = choice
        return best_choice

    
def main():
    '''
    A simple main to play Monte Carlo agent vs Random Agent for debugging.
    '''
    agent = MonteCarloAgent()
    agents = [agent, RandomAgent()]
    game = GameController(agents)
    game.start()

if __name__ == "__main__":
    main()
