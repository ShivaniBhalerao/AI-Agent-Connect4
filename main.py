from game_controller import GameController
from qlearning_agent import QLearningAgent
from random_agent import RandomAgent
from decision_tree_agent import DecisionTreeAgent
from minimax_agent import MinimaxAgent
from heuristic_agent import HeuristicAgent
from monte_carlo_agent import MonteCarloAgent

agents = {
    "1": RandomAgent(),
    "2": DecisionTreeAgent(),
    "3": MinimaxAgent(),
    "4": HeuristicAgent(),
    "5": MonteCarloAgent(),
    "6": QLearningAgent(False)}


def GetAgent():
    print("1: random agent")
    print("2: decision tree agent")
    print("3: minimax agent")
    print("4: heuristic agent")
    print("5: monte carlo agent")
    print("6: qlearning agent")
    agent_type = input("Enter your agent type:")
    if agent_type in agents:
        return agents[agent_type]
    else:
        print("Valid range must be [1,5]")
        return GetAgent()


def main():
    print("1 human vs human;")
    print("2 human vs agent(human first);")
    print("3 agent vs human(agent first);")
    print("4 agent vs agent")
    mode = input("Enter play mode:")
    if mode == "1":
        game = GameController([])
        game.start()
    elif mode == "2":
        GameController([GetAgent()], True).start()
    elif mode == "3":
        GameController([GetAgent()], False).start()
    elif mode == "4":
        print("\nchoose your first agent")
        agent1 = GetAgent()
        print("\nchoose your second agent")
        agent2 = GetAgent()
        GameController([agent1, agent2]).start()
    else:
        print("Valid range is [1,4]")
        main()


if __name__ == "__main__":
    main()
