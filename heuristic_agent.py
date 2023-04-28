import random
from agent import Agent


class HeuristicAgent(Agent):

    def getCol(self, board):
        player = board.turn
        if player == 1:
            opp_player = 2
        else:
            opp_player = 1

        valid_locations = board.get_valid_locations()
        win_set = set()
        fallback_set = set()
        stop_loss_set = set()

        for col in valid_locations:
            piece_copy = board.copy_board()
            player_copy = board.copy_board()

            piece_copy.drop_piece(col)
            if piece_copy.winning_move(player):
                win_set.add(col)

            player_copy.drop_piece(col)
            if player_copy.winning_move(opp_player):
                stop_loss_set.add(col)
            else:
                fallback_set.add(col)

        if len(win_set) > 0:
            colu = random.choice(list(win_set))
        elif len(stop_loss_set) > 0:
            colu = random.choice(list(stop_loss_set))
        elif len(fallback_set) > 0:
            colu = random.choice(list(fallback_set))

        return colu
