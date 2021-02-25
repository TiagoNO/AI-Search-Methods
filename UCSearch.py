from heapq import *
from SearchMethod import SearchMethod, Node
import random

class UCSearch(SearchMethod):

    def __init__(self, initial_state, goal):
        super().__init__(initial_state, goal)
        self.open_list.append(Node(initial_state, 0, 0, None))

    def getNodeFromOpenList(self):
        return heappop(self.open_list)

    def addInOpenList(self, node):
        heappush(self.open_list, node)

    def __str__(self):
        return "UCSearch method"