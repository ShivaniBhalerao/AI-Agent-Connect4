import numpy as np
import random

from agent import Agent
from board import Board


class QLearningAgent(Agent):
    '''
    A Qlearning model that supports training and also serialize/deserialize model.
    '''
    def __init__(self, train=True):
        '''
        When train is true, we train the model, store the model as file and use it to play.
        When train is false, we load model from file and use it to play.
        '''
        if train:
            self.q_table1 = {}
            self.q_table2 = {}
            self.epsilon1 = 0.1
            self.epsilon2 = 0.1
            self.Train()
        else:
            self.q_table1 = self.LoadQTable("q_table1.model")
            self.q_table2 = self.LoadQTable("q_table2.model")

    def getCol(self, board: Board):
        '''
        Play a move for the given board.
        '''
        if board.turn == 1:
            return self.GetAction(board, self.q_table1, 0.0)
        else:
            return self.GetAction(board, self.q_table2, 0.0)

    def LoadQTable(self, filename):
        '''
        Load a single q table from the give file.
        '''
        file = open(filename, "r")
        q_table = {}
        for line in file.readlines():
            key_value = line.split(';')
            key = key_value[0]
            value = float(key_value[1])
            q_table[key] = value
        return q_table

    def GetAction(self, board: Board, q_table, epsilon):
        '''
        Get action frmom the given q_table and epsion.
        '''
        max_score = -1
        possible_choices = []
        best_choices = []
        # There are at most 7 possible choices
        for col in range(7):
            if board.is_valid_location(col):
                # If a choice is valid, add it to all possible choices.
                possible_choices.append(col)

                # Put current piece on the board.
                current_board = np.copy(board.board)
                row = board.get_next_open_row(col)
                current_board[row][col] = 1

                # Convert the board to a string to represent the state.
                state = self.GetStateForBoard(current_board)

                # Get score for the state from q_table
                # Update best choices array based on max score.
                score = 0
                if state in q_table:
                    score = q_table[state]
                if score > max_score:
                    max_score = score
                    best_choices = [col]
                elif score == max_score:
                    best_choices.append(col)
        
        # No possible choice, return -1
        if len(possible_choices) == 0:
            return -1
        
        # Use epsilon probabliy to randomly play
        if random.uniform(0, 1) < epsilon:
            return random.choice(possible_choices)
        # Use 1 - epsilon probability to play the best choice.
        # When there is mulitple best choice, use random one.
        else:
            return random.choice(best_choices)

    def PlayerOneAction(self, board: Board):
        '''
        Get an action for first player
        '''
        return self.GetAction(board, self.q_table1, self.epsilon1)

    def PlayerTwoAction(self, board: Board):
        '''
        Get an action for second player.
        '''
        return self.GetAction(board, self.q_table2, self.epsilon2)

    def SaveQTable(self, q_table, filename):
        '''
        Store the given q_table to file.
        '''
        f = open(filename, "w")
        for key, value in q_table.items():
            line = '{0};{1}\n'.format(key, value)
            f.write(line)
        f.close

    def Train(self):
        '''
        Train the model
        '''
        self.player_one_wins = 0
        self.player_two_wins = 0
        for i in range(10000):
            print("episode:", i)
            board = Board()
            self.LearnOneGame(board)

        self.SaveQTable(self.q_table1, "q_table1.model")
        self.SaveQTable(self.q_table2, "q_table2.model")

    def GetStateForBoard(self, board):
        '''
        Serialize the board to a single string by flattern the board and
        concatenate all numbers, split by ','.
        '''
        x = board.flatten()
        # generate an array with strings
        x_arrstr = np.char.mod('%d', x)
        # combine to a string
        key = ",".join(x_arrstr)
        return key

    def GetValue(self, q_table, state):
        '''
        Get q_table value for a given state, default to 0.
        '''
        if state in q_table:
            return q_table[state]
        else:
            return 0

    def LearnOneGame(self, board: Board):
        '''
        One episode(iteration) of play and training of q_table.
        '''
        # Q learning parameter init value.
        learning_rate = 0.1
        gamma = 0.8
        done = False
        i = 0

        # There are at most 42(7*6) plays
        while not done and i < 42:
            # Play the first player and update its q_table.
            action1 = self.PlayerOneAction(board)
            current_state = self.GetStateForBoard(board.board)
            board.drop_piece(action1)
            new_state = self.GetStateForBoard(board.board)
            if board.winning_move(1):
                self.q_table1[new_state] = 100
                self.q_table2[new_state] = 0
                done = True

            old_value = self.GetValue(self.q_table1, current_state)
            next_state_value = self.GetValue(self.q_table1, new_state)
            reward = 1
            new_value = old_value + learning_rate * (reward + gamma * next_state_value - old_value)
            self.q_table1[current_state] = new_value

            if done:
                self.player_one_wins += 1
                break

            # Play the second player and update its q_table
            action2 = self.PlayerTwoAction(board)
            current_state = self.GetStateForBoard(board.board)
            board.drop_piece(action2)
            new_state = self.GetStateForBoard(board.board)
            if board.winning_move(2):
                self.q_table2[new_state] = 100
                self.q_table1[new_state] = 0
                done = True

            old_value = self.GetValue(self.q_table2, current_state)
            next_state_value = self.GetValue(self.q_table2, new_state)
            reward = 1
            new_value = old_value + learning_rate * (reward + gamma * next_state_value - old_value)
            self.q_table2[current_state] = new_value
            if done:
                self.player_two_wins += 1
                break

        # Print one iteration result for debugging purpose.
        print(self.player_one_wins, self.player_two_wins, self.player_one_wins / (self.player_two_wins + 1))


def main():
    '''
    Simple main function to train the model.
    Run python3 qlearning_agent.py will train the model.
    '''
    QLearningAgent(True)

if __name__ == "__main__":
    main()
