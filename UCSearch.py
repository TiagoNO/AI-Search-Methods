from heapq import *
from SearchMethod import SearchMethod
import random

class UCSearch(SearchMethod):

    def __init__(self, initial_state, goal):
        super().__init__(initial_state, goal)
        self.open_list.append((0, initial_state))

    def getStateFromOpenList(self):
        return heappop(self.open_list)

    def addInOpenList(self, state):
        heappush(self.open_list, state)

    def __str__(self):
        return "UCSearch method"