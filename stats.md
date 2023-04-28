# Play Stats
`stats.py` will let you select any two of our agents, and then automatically run 1000 games(500 games as red, 500 games as yellow) for the two agents. The number of games won will be printed in terminal.

Caution: since we are running the game 1000 times, for some agents, it may take you about an hour to get the result.

## How to run
```
python3 stats.py
```
Then choose two agents you want to compare based on the prompt in terminal, example of choose qlearning agent and monte carlo agent:
```
pygame 2.1.2 (SDL 2.0.18, Python 3.9.7)
Hello from the pygame community. https://www.pygame.org/contribute.html
1: random agent
2: decision tree agent
3: minimax agent
4: heuristic agent
5: monte carlo agent
6: qlearning agent
Enter your agent type:6
1: random agent
2: decision tree agent
3: minimax agent
4: heuristic agent
5: monte carlo agent
6: qlearning agent
Enter your agent type:5
```

## How to read the result
The three numbers in `()`:

(number of games that first player won, number of games that second player won, number of tie/draw)

### Example:
```
firstplayer <class 'random_agent.RandomAgent'> secondplayer <class 'minimax_agent.MinimaxAgent'>
(0, 500, 0)
```
The first player is random agent, the second player is minimax agent.

Numbers in`()` means the first player has won 0 game, the second player has won 500 games, and 0 game is tie/draw.

# Results

## vs Random

### Random
Let ramdon agent play with itself to see how much the first player has an advantage.
```
firstplayer <class 'random_agent.RandomAgent'> secondplayer <class 'random_agent.RandomAgent'>
(283, 217, 0)
firstplayer <class 'random_agent.RandomAgent'> secondplayer <class 'random_agent.RandomAgent'>
(275, 223, 2)
```

### QLearning
```
firstplayer <class 'random_agent.RandomAgent'> secondplayer <class 'qlearning_agent.QLearningAgent'>
(270, 230, 0)
firstplayer <class 'qlearning_agent.QLearningAgent'> secondplayer <class 'random_agent.RandomAgent'>
(288, 209, 3)
```

### Decision Tree
```
firstplayer <class 'random_agent.RandomAgent'> secondplayer <class 'decision_tree_agent.DecisionTreeAgent'>
(30, 457, 13)
firstplayer <class 'decision_tree_agent.DecisionTreeAgent'> secondplayer <class 'random_agent.RandomAgent'>
(462, 25, 13)
```

### Heuristic
```
firstplayer <class 'heuristic_agent.HeuristicAgent'> secondplayer <class 'random_agent.RandomAgent'>
(405, 95, 0)
firstplayer <class 'random_agent.RandomAgent'> secondplayer <class 'heuristic_agent.HeuristicAgent'>
(139, 361, 0)
```

### Minimax
```
firstplayer <class 'random_agent.RandomAgent'> secondplayer <class 'minimax_agent.MinimaxAgent'>
(0, 500, 0)
firstplayer <class 'minimax_agent.MinimaxAgent'> secondplayer <class 'random_agent.RandomAgent'>
(500, 0, 0)
```


### Monte Carlo
```
firstplayer <class 'random_agent.RandomAgent'> secondplayer <class 'monte_carlo_agent.MonteCarloAgent'>
(0, 500, 0)
firstplayer <class 'monte_carlo_agent.MonteCarloAgent'> secondplayer <class 'random_agent.RandomAgent'>
(499, 1, 0)
```


### Summary

Except for the q learning agent, all other algorithms seems to be able to beat the random agent.


## vs Qlearning

As Qlearning is the worst one, we first want to make sure if every other four agents(Decision Tree, Heuristic, Minimax, Monte Carlo) can beat it.

### Decision Tree

```
firstplayer <class 'qlearning_agent.QLearningAgent'> secondplayer <class 'decision_tree_agent.DecisionTreeAgent'>
(27, 461, 12)
firstplayer <class 'decision_tree_agent.DecisionTreeAgent'> secondplayer <class 'qlearning_agent.QLearningAgent'>
(474, 17, 9)
```

### Heuristic

```
firstplayer <class 'qlearning_agent.QLearningAgent'> secondplayer <class 'heuristic_agent.HeuristicAgent'>
(155, 344, 1)
firstplayer <class 'heuristic_agent.HeuristicAgent'> secondplayer <class 'qlearning_agent.QLearningAgent'>
(417, 83, 0)
```

### Minimax
```
firstplayer <class 'qlearning_agent.QLearningAgent'> secondplayer <class 'minimax_agent.MinimaxAgent'>
(0, 500, 0)
firstplayer <class 'minimax_agent.MinimaxAgent'> secondplayer <class 'qlearning_agent.QLearningAgent'>
(500, 0, 0)
```

### Monte Carlo
```
firstplayer <class 'qlearning_agent.QLearningAgent'> secondplayer <class 'monte_carlo_agent.MonteCarloAgent'>
(1, 499, 0)
firstplayer <class 'monte_carlo_agent.MonteCarloAgent'> secondplayer <class 'qlearning_agent.QLearningAgent'>
(500, 0, 0)
```


## vs Decision Tree

### Heuristic
```
firstplayer <class 'decision_tree_agent.DecisionTreeAgent'> secondplayer <class 'heuristic_agent.HeuristicAgent'>
(395, 97, 8)
firstplayer <class 'heuristic_agent.HeuristicAgent'> secondplayer <class 'decision_tree_agent.DecisionTreeAgent'>
(112, 375, 13)
```

### Minimax
```
firstplayer <class 'decision_tree_agent.DecisionTreeAgent'> secondplayer <class 'minimax_agent.MinimaxAgent'>
(0, 500, 0)
firstplayer <class 'minimax_agent.MinimaxAgent'> secondplayer <class 'decision_tree_agent.DecisionTreeAgent'>
(500, 0, 0)
```

### Monte Carlo
```
firstplayer <class 'decision_tree_agent.DecisionTreeAgent'> secondplayer <class 'monte_carlo_agent.MonteCarloAgent'>
(32, 467, 1)
firstplayer <class 'monte_carlo_agent.MonteCarloAgent'> secondplayer <class 'decision_tree_agent.DecisionTreeAgent'>
(386, 88, 26)
```

### Qlearning
```
firstplayer <class 'decision_tree_agent.DecisionTreeAgent'> secondplayer <class 'qlearning_agent.QLearningAgent'>
(455, 29, 16)
firstplayer <class 'qlearning_agent.QLearningAgent'> secondplayer <class 'decision_tree_agent.DecisionTreeAgent'>
(34, 453, 13)
```

## vs Minimax

### heuristic
```
firstplayer <class 'minimax_agent.MinimaxAgent'> secondplayer <class 'heuristic_agent.HeuristicAgent'>
(500, 0, 0)
firstplayer <class 'heuristic_agent.HeuristicAgent'> secondplayer <class 'minimax_agent.MinimaxAgent'>
(0, 500, 0)
```

### Monte Carlo
```
firstplayer <class 'minimax_agent.MinimaxAgent'> secondplayer <class 'monte_carlo_agent.MonteCarloAgent'>
(426, 74, 0)
firstplayer <class 'monte_carlo_agent.MonteCarloAgent'> secondplayer <class 'minimax_agent.MinimaxAgent'>
(28, 472, 0)
```

## vs Monte Carlo

### Heuristic
```
firstplayer <class 'monte_carlo_agent.MonteCarloAgent'> secondplayer <class 'heuristic_agent.HeuristicAgent'>
(499, 1, 0)
firstplayer <class 'heuristic_agent.HeuristicAgent'> secondplayer <class 'monte_carlo_agent.MonteCarloAgent'>
(4, 496, 0)
```

### Decision Tree
```
firstplayer <class 'decision_tree_agent.DecisionTreeAgent'> secondplayer <class 'monte_carlo_agent.MonteCarloAgent'>
(32, 467, 1)
firstplayer <class 'monte_carlo_agent.MonteCarloAgent'> secondplayer <class 'decision_tree_agent.DecisionTreeAgent'>
(386, 88, 26)
```

### Minimax
```
firstplayer <class 'monte_carlo_agent.MonteCarloAgent'> secondplayer <class 'minimax_agent.MinimaxAgent'>
(23, 477, 0)
firstplayer <class 'minimax_agent.MinimaxAgent'> secondplayer <class 'monte_carlo_agent.MonteCarloAgent'>
(419, 81, 0)
```