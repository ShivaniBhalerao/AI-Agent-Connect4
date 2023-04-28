'''
For Game UI, we borrowed idea form: https://github.com/KeithGalli/Connect4-Python
This repo is MIT License. We refactored and modified some of its code based on our own design.
'''

import random
import pygame
import sys
import math
from board import RED, BLACK, YELLOW, Board, SQUARESIZE, size, width, RADIUS, \
    COLUMN_COUNT, ROW_COUNT, BLUE, PLAYER_PIECE, AI_PIECE, height


EMPTY = 0
PLAYER_ONE_PIECE = 1
PLAYER_TWO_PIECE = 2

HUMAN = 1


class GameController():
    def __init__(self, agents, human_first = True):
        pygame.init()

        self.screen = pygame.display.set_mode(size)
        self.board = Board()
        self.board.print_board()
        self.my_font = pygame.font.SysFont("monospace", 75)
        self.draw_board()
        self.agents = agents
        if len(self.agents) == 0:
            self.playerOne = HUMAN
            self.playerTwo = HUMAN
        elif len(self.agents) == 1:
            if human_first:
                self.playerOne = HUMAN
                self.playerTwo = self.agents[0]
            else:
                self.playerOne = self.agents[0]
                self.playerTwo = HUMAN
        else:
            self.playerOne = self.agents[0]
            self.playerTwo = self.agents[1]

        pygame.display.update()

    def draw_board(self):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE,
                                 (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2),
                                                        int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if self.board.get_board()[r][c] == PLAYER_PIECE:
                    pygame.draw.circle(self.screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2),
                                                          height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif self.board.get_board()[r][c] == AI_PIECE:
                    pygame.draw.circle(self.screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2),
                                                             height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    def no_moves_left(self,board):
        for col in range(0,7):
            if board.is_valid_location(col):
                return False
        return True

    def start(self):
        screen = self.screen
        board = self.board
        game_over = False
        tie=0
        turn = 1
        if len(self.agents) == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        while not game_over:

            "To check if there are no moves left"
            if self.no_moves_left(board):
                label = self.my_font.render("No moves left. It's a tie.", 1, BLUE)
                screen.blit(label, (40, 10))
                game_over = True
                board.print_board()
                self.draw_board()
                pygame.time.wait(3000)
                pygame.quit()
                continue


            if turn == 1:
                current_player = self.playerOne
                color = RED
            else:
                current_player = self.playerTwo
                color = YELLOW
            # if turn == 1:
            #     color = RED

            if current_player == HUMAN:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEMOTION:
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                        posx = event.pos[0]
                        pygame.draw.circle(screen, color, (posx, int(SQUARESIZE/2)), RADIUS)

                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                        # print(event.pos)
                        # Ask for Player 1 Input
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))

                        if board.is_valid_location(col):
                            board.drop_piece(col)

                            if board.winning_move(turn):
                                label = self.my_font.render("Player {} Wins!".format(turn), 1, color)
                                screen.blit(label, (40, 10))
                                game_over = True

                            turn = 3 - turn

                            board.print_board()
                            self.draw_board()

            else:
                col = current_player.getCol(board)

                if board.is_valid_location(col):
                    board.drop_piece(col)

                    if board.winning_move(turn):
                        label = self.my_font.render("Player {} Wins!".format(turn), 1, color)
                        screen.blit(label, (40, 10))
                        game_over = True

                    board.print_board()
                    self.draw_board()

                    if len(self.agents) == 2:
                        pygame.time.wait(1000)
                    turn = 3 - turn

            if game_over:
                if turn == 1:
                    print(type(self.playerTwo))
                else:
                    print(type(self.playerOne))
                pygame.time.wait(3000)
                pygame.quit()