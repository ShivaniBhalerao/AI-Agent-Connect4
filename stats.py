from random import Random
from agent import Agent
from board import Board
from main import GetAgent
from random_agent import RandomAgent
from monte_carlo_agent import MonteCarloAgent
from minimax_agent import MinimaxAgent
from heuristic_agent import HeuristicAgent
from qlearning_agent import QLearningAgent

def Stats(agentOne:Agent, agentTwo:Agent):
    one_wins = 0
    two_wins = 0
    tie = 0
    for i in range(500):
        board = Board()
        done = False
        turn = 1
        step = 0
        while not done and step < 21:
            move = agentOne.getCol(board)
            board.drop_piece(move)
            if board.winning_move(turn):
                one_wins += 1
                break

            turn = 3 - turn
            move = agentTwo.getCol(board)
            board.drop_piece(move)
            if board.winning_move(turn):
                two_wins += 1
                break
            turn = 3 - turn
            step += 1

        if step == 21:
            tie += 1
    return (one_wins, two_wins, tie)

def ComapreAgents(agentOne:Agent, agentTwo:Agent):
    print("firstplayer", type(agentOne), "secondplayer", type(agentTwo))
    print(Stats(agentOne, agentTwo))
    print("firstplayer", type(agentTwo), "secondplayer", type(agentOne))
    print(Stats(agentTwo, agentOne))



def main():
    agentOne = GetAgent()
    agentTwo = GetAgent()
    ComapreAgents(agentOne, agentTwo)

if __name__ == "__main__":
    main()
