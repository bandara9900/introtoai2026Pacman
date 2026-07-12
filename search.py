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
from game import Directions
from typing import List

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




def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """
    # 1. THE STARTING POINT
    startState = problem.getStartState()
    
    # 2. THE TOOLS
    fringe = util.Stack()
    fringe.push((startState, []))
    visited = set()

    # 3. THE EXPLORATION LOOP
    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    newPath = actions + [action]
                    fringe.push((successor, newPath))

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # 1. THE STARTING POINT
    startState = problem.getStartState()
    
    # 2. THE TOOLS
    # Notice the magic change: We use a Queue instead of a Stack!
    fringe = util.Queue() 
    fringe.push((startState, []))
    
    visited = set()

    # 3. THE EXPLORATION LOOP
    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    newPath = actions + [action]
                    fringe.push((successor, newPath))

    return []
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # 1. THE STARTING POINT
    startState = problem.getStartState()
    
    # 2. THE TOOLS
    # The magic change: We use a Priority Queue!
    fringe = util.PriorityQueue() 
    
    # We now need to track THREE things: the state, the path, AND the total cost.
    # We push a tuple: (state, actions, cost)
    # The second argument (0) is the "priority" (the cost). Lowest cost goes first!
    fringe.push((startState, [], 0), 0) 
    
    visited = set()

    # 3. THE EXPLORATION LOOP
    while not fringe.isEmpty():
        # Pop gives us the state, actions, and the total cost to get there
        state, actions, cost = fringe.pop()

        # Did we find the goal?
        if problem.isGoalState(state):
            return actions

        # Have we been here before?
        if state not in visited:
            visited.add(state)

            # Look at all the next steps
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    # Calculate the NEW total cost
                    new_cost = cost + stepCost
                    new_path = actions + [action]
                    
                    # Push to the Priority Queue. 
                    # The item is (state, path, new_cost). 
                    # The priority is new_cost (so the queue sorts by cost!)
                    fringe.push((successor, new_path, new_cost), new_cost)

    return []
def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # 1. THE STARTING POINT
    startState = problem.getStartState()
    
    # 2. THE TOOLS
    fringe = util.PriorityQueue() 
    
    # Calculate the starting priority: Cost (0) + Heuristic guess for the start state
    start_priority = 0 + heuristic(startState, problem)
    
    # Push: (state, actions, cost). Priority is the combined score.
    fringe.push((startState, [], 0), start_priority) 
    
    visited = set()

    # 3. THE EXPLORATION LOOP
    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    new_cost = cost + stepCost
                    new_path = actions + [action]
                    
                    # THE MAGIC OF A*: Add the heuristic guess to the cost!
                    h_n = heuristic(successor, problem)
                    priority = new_cost + h_n
                    
                    # Push to the Priority Queue using the combined score
                    fringe.push((successor, new_path, new_cost), priority)

    return []
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
