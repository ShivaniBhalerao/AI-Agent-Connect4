#import random

from agent import Agent
from board import Board
import numpy as np
from game_controller import GameController

class DecisionTreeAgent(Agent):

    "This method checks diagonal cells in descending way"
    """
    |\
    | \
    |  \
    |   \
    |____\__
    """

    def checkDiagonallyRight(self,row,col,player,board):
        if row==0:
            return 0
        elif row==None:
            return -100
        #row=row-1
        #col=col+1
        points=0
        opposite_player=0
        if player==1: #look for the opposite player
            opposite_player=2
        else:
            opposite_player=1

        curr_row = row-1
        curr_col = col+1
        #check diagonally right-down
        while curr_row >=0 and curr_col < 7 and board.board[curr_row][curr_col]==opposite_player:
            points=points+1
            curr_row-=1
            curr_col+=1

        curr_row=row+1
        curr_col=col-1

        #check diagonally left-up
        while curr_row <6 and curr_col >=0 and board.board[curr_row][curr_col]==opposite_player:
            points=points+1
            curr_row+=1
            curr_col-=1

        return points




        "If current player's win should also be considered, use lines of code similar to this"
        """while row<6 and col<7:
            curr_row=row
            curr_col=col
            count=0
            
            if board[curr_row][curr_col]==player:
                while board[curr_row][curr_col]==player:
                    count=count+1
                if count*10>points:
                    points=count*100
        """

    "This method checks diagonal cells in ascending way"
    """
    |    /
    |   /
    |  /
    | /  
    |/______
    """
    def checkDiagonallyLeft(self, row, col, player, board):
        if row == 0:
            return 0
        elif row == None:
            return -100

        #row=row-1
        #col=col-1

        points = 0
        opposite_player = 0
        if player == 1:  #look for the opposite player
            opposite_player = 2
        else:
            opposite_player = 1


        #check diagonally left-down
        curr_row = row - 1
        curr_col = col - 1
        while curr_row >=0 and curr_col >=0 and board.board[curr_row][curr_col] == opposite_player:
            points = points + 1
            curr_row -= 1
            curr_col -= 1

        #check diagonally right-up
        curr_row = row + 1
        curr_col = col + 1
        while curr_row <6 and curr_col <7 and board.board[curr_row][curr_col] == opposite_player:
            points = points + 1
            curr_row += 1
            curr_col += 1


        return points

    "This method checks the column"
    """
    |   | 
    |   |
    |   |
    |   |
    |___|___
    """
    def checkCol(self,row,col,player,board):
        if row == 0:
            return 0
        elif row == None:
            return -100

        row=row-1
        points=0
        opposite_player = 0
        if player == 1: #look for the opposite player
            opposite_player = 2
        else:
            opposite_player = 1

        curr_row = row
        curr_col = col
        while curr_row >= 0 and board.board[curr_row][curr_col] == opposite_player:
            points = points + 1
            curr_row -= 1

        return points

    "This method checks the row"
    """
    |    
    |   
    |------   
    |   
    |______
    """
    def checkRow(self,row,col,player,board):

        if row == None:
            return -100

        pointsLeft=0
        pointsRight=0
        opposite_player = 0
        if player == 1: #look for the opposite player
            opposite_player = 2
        else:
            opposite_player = 1

        curr_row = row
        curr_col = col-1
        while curr_col >=0 and board.board[curr_row][curr_col] == opposite_player:
            pointsLeft = pointsLeft + 1
            curr_col -= 1

        curr_col = col+1
        while curr_col <7  and board.board[curr_row][curr_col] == opposite_player:
            pointsRight = pointsRight + 1
            curr_col += 1

        return pointsLeft+pointsRight

    """
    This method checks the columns of the board and calculates the connected coins of the opposite player.
    Further it plays the current best move.
    """
    def getCol(self, board:Board) -> int:
        #print("In dec tree")
        player=board.turn
        #print("col count:",board.getColumnCount())
        points_map={0:0,1:0,2:0,3:0,4:0,5:0,6:0}
        #points=-1
        col=-1
        for colNum in range(0,board.getColumnCount()):
            if not board.is_valid_location(colNum):
                continue

            #print("DTA col:",colNum)
            rowNum=board.get_next_open_row(colNum)

            diag_right=self.checkDiagonallyRight(rowNum, colNum, player, board)
            #print("diag_right:",diag_right)
            diag_left=self.checkDiagonallyLeft(rowNum, colNum, player, board)
            #print("diag_left:", diag_left)
            checkCol=self.checkCol(rowNum, colNum, player, board)
            #print("checkCol:", checkCol)
            checkRow=self.checkRow(rowNum, colNum, player, board)
            #print("checkRow:",checkRow)
            newpoints=max(diag_right, diag_left, checkCol, checkRow)
            points_map[colNum]=newpoints
            """
            if newpoints>points:
                col=colNum
                points=newpoints
            """

        sorted_points_tuple=sorted(points_map.items(), key=lambda col_points_tuple:col_points_tuple[1], reverse=True)
        # print(sorted_points_tuple)
        sorted_points_map={key: value for key, value in sorted_points_tuple}


        #print("points:", sorted_points_map)
        for col_index in sorted_points_map:
            if not board.is_valid_location(col_index):
                continue
            else:
                col=col_index
                break
        #print("final col:", col)

        return col