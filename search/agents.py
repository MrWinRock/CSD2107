import random
from game import Agent
from game import Directions


class DumbAgent(Agent):
    "An agent that goes West until it can't"

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)"

        print("Location: ", state.getPacmanPosition())
        print("Action available: ", state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP


class RamdomAgent(Agent):
    "An agent that picks random legal action"

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)"
        print(('Location:'), state.getPacmanPosition())
        listofactions = state.getLegalPacmanAction()[:]
        listofactions.remove(Directions.STOP)  # remove 'STOP'
        print(('Action available:'), listofactions)
        action = random.choice(listofactions)
        print("Going" + action)
        return action

class ReflexAgent(Agent):
    "An agent that prioritize action that will immediately gain food pellet"

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)"
        print(('Location:'), state.getPacmanPosition())
        listofactions = state.getLegalPacmanActions()[:]
        listofactions.remove(Directions.STOP)
        print(('Actions available:'), listofactions)
        num_food = state.getNumFood()
        for act in listofactions:
            if num_food > state.generatePacmanSuccessor(act).getNumFood():
                "if can eat food, take the action"
                return act
        return random.choice(listofactions)