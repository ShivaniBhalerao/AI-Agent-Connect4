# Team 11
Shivani Bhalerao, Chao Pan, Yumeng An

# About
Built AI agents for the connect-4 game using heuristics, decision tree, minimax with alpha-beta pruning, monte carlo and Q-learning algorithm and found minimax agent and monte carlo agent to be the top 2 performing agents for this use case.

# How to run the game

## Preparation
Make sure you've installed `pygame`, [website](https://www.pygame.org/news)
Use python 3.9 to run the project.

To install it, try:

```shell
pip3 install pygame
```

## Play the game

Run
```shell
python3 main.py
```

You will see the below prompt in terminal:
```shell
pygame 2.1.2 (SDL 2.0.18, Python 3.9.7)
Hello from the pygame community. https://www.pygame.org/contribute.html
1 human vs human;
2 human vs agent(human first);
3 agent vs human(agent first);
4 agent vs agent
Enter play mode:
```

Then, continue to choose your prefered model and agent(s) based on prompts in terminal.

## Q learning agent

### Train model
The models have been save to `q_table1.model` and `q_table2.model`.

If you want to re-train the model, in the main function of `qlearning_agent.py`, change the line:
```shell
agent = QLearningAgent(False)
```
To:
```shell
agent = QLearningAgent(True)
```
Then run:
```shell
python3 qlearning_agent.py
```