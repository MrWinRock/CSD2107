# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    "*** YOUR CODE HERE ***"

    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myStack = util.Stack()
    visitedNodes = set()
    myStack.push((startingNode, []))

    while not myStack.isEmpty():
        currentNode, actions = myStack.pop()
        print("Node: ", currentNode)
        print("Successor: ", problem.getSuccessors(currentNode))
        if currentNode not in visitedNodes:
            visitedNodes.add(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                myStack.push((nextNode, newAction))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myQueue = util.Queue()
    visitedNodes = set()
    myQueue.push((startingNode, []))

    while not myQueue.isEmpty():
        currentNode, actions = myQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.add(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                myQueue.push((nextNode, newAction))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Use a PriorityQueue, so the cost of actions is calculated with a provided heuristic
    fringe = util.PriorityQueue()
    # Make an empty list of explored nodes
    visited = []
    # Make an empty list of actions
    actionList = []
    # Place the starting point in the priority queue
    fringe.push((problem.getStartState(), actionList), problem)
    while fringe:
        node, actions = fringe.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                nextCost = problem.getCostOfActions(nextActions)
                fringe.push((coordinate, nextActions), nextCost)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Use a priority queue, so the cost of actions is calculated with a provided heuristic
    fringe = util.PriorityQueue()
    # Make an empty list of explored nodes
    visited = []
    # Make an empty list of actions
    actionList = []
    # Place the starting point in the priority queue
    fringe.push((problem.getStartState(), actionList),
                heuristic(problem.getStartState(), problem))
    while fringe:
        node, actions = fringe.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                nextCost = problem.getCostOfActions(nextActions) + \
                    heuristic(coordinate, problem)
                fringe.push((coordinate, nextActions), nextCost)
    return []


def iterativeDeepeningAStar(problem, heuristic=nullHeuristic):
    """Iterative Deepening A* Search"""

    def search(node, cost, threshold):
        f = cost + heuristic(node, problem)
        print("Heuristic = ", f, "Threshold = ", threshold)
        # print("Start:", problem.getStartState())
        # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
        if f > threshold:
            return f
        if problem.isGoalState(node):
            return FOUND
        min_threshold = float("inf")
        for successor, action, step_cost in problem.getSuccessors(node):
            if successor not in visited:
                visited.add(successor)
                result = search(successor, cost + step_cost, threshold)
                if result == FOUND:
                    actions.append(action)
                    return FOUND
                if result < min_threshold:
                    min_threshold = result
                visited.remove(successor)
        return min_threshold

    FOUND = object()  # Unique marker for found goal
    start = problem.getStartState()
    threshold = heuristic(start, problem)
    while True:
        visited = set([start])
        actions = []
        t = search(start, 0, threshold)
        if t == FOUND:
            actions.reverse()
            return actions
        if t == float("inf"):
            return []
        threshold = t


def depthLimitSearchNotComplete(problem, depthLimit=7):
    """Depth-Limit Search Not Complete"""

    """
    For mediumMaze.
    The Least cost to make the puzzle complete is 68.
    Depth-Limit is 67, there is no solution to make the puzzle complete
    with limit of 67.
    """
    def recursiveDLS(node, depth, actions, visited):
        print(problem.getSuccessors(node))
        if problem.isGoalState(node):
            return actions  # Return the result of actions when the goal is found

        if depth == 0:
            return "cutoff"

        cutoffOccurred = False
        for nextNode, action, cost in problem.getSuccessors(node):
            if nextNode not in visited:
                newAction = actions + [action]
                visited.add(nextNode)
                result = recursiveDLS(nextNode, depth - 1, newAction, visited)
                visited.remove(nextNode)

                if result == "cutoff":
                    cutoffOccurred = True
                elif result:
                    return result

        return "cutoff" if cutoffOccurred else None

    print(problem.getStartState())
    startingNode = problem.getStartState()
    visited = set([startingNode])
    result = recursiveDLS(startingNode, depthLimit, [], visited)

    return result if result != "cutoff" else []


def depthLimitSearch(problem, depthLimit=8):
    """Depth-Limit Search"""

    """
    For mediumMaze
    Best case is the limit of 68 which is the least cost of make
    puzzle complete with depth-limit search.
    """
    def recursiveDLS(node, depth, actions, visited):
        print(problem.getSuccessors(node))
        if problem.isGoalState(node):
            return actions  # Return the result of actions when the goal is found
        if depth == 0:
            return "cutoff"

        cutoffOccurred = False
        for nextNode, action, cost in problem.getSuccessors(node):
            if nextNode not in visited:
                newAction = actions + [action]
                print("Visited1 : ", visited) #
                visited.add(nextNode)
                print("Visited 2: ", visited) #
                print("NextNode: ", nextNode) #
                result = recursiveDLS(nextNode, depth - 1, newAction, visited)
                print("Visited 3: ", visited) # 
                visited.remove(nextNode)
                print("Visited 4: ", visited) # 

                print("Result: ", result) #
                if result == "cutoff":
                    cutoffOccurred = True
                elif result:
                    return result

        return "cutoff" if cutoffOccurred else None

    startingNode = problem.getStartState()
    visited = set([startingNode])
    result = recursiveDLS(startingNode, depthLimit, [], visited)

    return result if result != "cutoff" else []


def iterativeDeepeningSearch(problem):
    def depthLimitedSearch(node, depthLimit, actions, visited):
        if problem.isGoalState(node):
            return actions

        if depthLimit == 0:
            return "cutoff"
        print("Successor: ", problem.getSuccessors(node)) #
        cutoffOccurred = False
        for nextNode, action, cost in problem.getSuccessors(node):
            if nextNode not in visited:
                print("Node expanded: ", node) #
                newAction = actions + [action]
                visited.add(nextNode)
                print("Next node: ", nextNode) #
                result = depthLimitedSearch(
                    nextNode, depthLimit - 1, newAction, visited)
                print("Visited: ", visited) #
                visited.remove(nextNode)

                if result == "cutoff":
                    cutoffOccurred = True
                elif result:
                    return result

        return "cutoff" if cutoffOccurred else None

    startingNode = problem.getStartState()

    for depthLimit in range(1, 10000):  # Use a large integer instead of float('inf')
        visited = set([startingNode]) 
        print("\n-----------------------\nDepth Limit: ", depthLimit) #
        result = depthLimitedSearch(startingNode, depthLimit, [], visited)
        if result and result != "cutoff":
            return result


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
idastar = iterativeDeepeningAStar
dlsn = depthLimitSearchNotComplete
dls = depthLimitSearch
ids = iterativeDeepeningSearch
