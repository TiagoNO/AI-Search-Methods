from heapq import *
from SearchMethod import SearchMethod, Node
from HeuristicMetric import *

class AStar(SearchMethod):

    def __init__(self, initial_state, goal, heuristic, cost_w=1, heuristic_w=1):
        super().__init__(initial_state, goal)
        self.open_list.append(Node(initial_state, 0, 0, None))
        self.heuristic = heuristic
        self.cost_w = cost_w
        self.heuristic_w = heuristic_w

    def getStateValue(self, state):
        c_value = state.cost * self.cost_w
        h_value = self.heuristic.calculate(state, self.goal) * self.heuristic_w
        return c_value + h_value

    def getNodeFromOpenList(self):
        return heappop(self.open_list)

    def addInOpenList(self, node):
        heappush(self.open_list, node)

    def __str__(self):
        return "A* method"