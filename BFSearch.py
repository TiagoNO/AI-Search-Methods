from SearchMethod import SearchMethod

class BFSearch(SearchMethod):

    def __init__(self, initial_state, goal):
        super().__init__(initial_state, goal)
        self.open_list.append((0, initial_state))

    def getStateFromOpenList(self):
        return self.open_list.pop(0)

    def addInOpenList(self, state):
        self.open_list.append(state)

    def __str__(self):
        return "Breadth-First Search method"

