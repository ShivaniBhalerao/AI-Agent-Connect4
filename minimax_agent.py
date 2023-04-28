import random
import math
from agent import Agent
from evaluation import Evaluation


class MinimaxAgent(Agent):
    def __init__(self, depth=5):
        self.depth = depth

    def minimax(self, board, player, depth, alpha, beta, maximizingPlayer):
        # evl = Evaluation(board.turn)
        evl = Evaluation(player)

        valid_locations = board.get_valid_locations()
        is_terminal = evl.is_terminal_node(board)

        if depth == 0 or is_terminal:
            if is_terminal:
                if board.winning_move(evl.bot_piece):
                    return None, 100000000000000
                elif board.winning_move(evl.opp_piece):
                    return None, -10000000000000
                else:  # Game is over, no more valid moves
                    return None, 0
            else:  # Depth is zero
                return None, evl.score_position(board)

        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                b_copy = board.copy_board()
                b_copy.drop_piece(col)
                new_score = self.minimax(b_copy, player, depth-1, alpha, beta, False)[1]

                if new_score > value:
                    value = new_score
                    column = col

                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else: # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                b_copy = board.copy_board()
                b_copy.drop_piece(col)
                new_score = self.minimax(b_copy, player, depth-1, alpha, beta, True)[1]

                if new_score < value:
                    value = new_score
                    column = col

                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def getCol(self, board):
        player = board.turn
        col, minimax_score = self.minimax(board, player, self.depth, -math.inf, math.inf, True)
        return col