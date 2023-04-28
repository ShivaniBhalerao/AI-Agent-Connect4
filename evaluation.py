from board import WINDOW_LENGTH, EMPTY

class Evaluation:
    def __init__(self, piece):
        self.bot_piece = piece
        if self.bot_piece == 1:
            self.opp_piece = 2
        else:
            self.opp_piece = 1

    def evaluate_window(self, window):
        score = 0
        if window.count(self.bot_piece) == 4:
            score += 100
        elif window.count(self.bot_piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(self.bot_piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(self.opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    def score_position(self, board):
        score = 0

        ## Score center column
        center_array = [int(i) for i in list(board.get_board()[:, board.getColumnCount()//2])]
        center_count = center_array.count(self.bot_piece)
        score += center_count * 3

        ## Score Horizontal
        for r in range(board.getRowCount()):
            row_array = [int(i) for i in list(board.get_board()[r,:])]
            for c in range(board.getColumnCount()-3):
                window = row_array[c:c+WINDOW_LENGTH]
                score += self.evaluate_window(window)

        ## Score Vertical
        for c in range(board.getColumnCount()):
            col_array = [int(i) for i in list(board.get_board()[:,c])]
            for r in range(board.getRowCount()-3):
                window = col_array[r:r+WINDOW_LENGTH]
                score += self.evaluate_window(window)

        ## Score positive sloped diagonal
        for r in range(board.getRowCount()-3):
            for c in range(board.getColumnCount()-3):
                window = [board.get_board()[r+i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window)

        ## Score negative sloped diagonal
        for r in range(board.getRowCount()-3):
            for c in range(board.getColumnCount()-3):
                window = [board.get_board()[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window)

        return score

    def is_terminal_node(self, board):
        return board.winning_move(self.bot_piece) or board.winning_move(self.opp_piece) or \
               len(board.get_valid_locations()) == 0
