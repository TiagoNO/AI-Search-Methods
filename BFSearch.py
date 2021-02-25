from SearchMethod import SearchMethod, Node

class BFSearch(SearchMethod):

    def __init__(self, initial_state, goal):
        super().__init__(initial_state, goal)
        self.open_list.append(Node(initial_state, 0, 0, None))

    def getNodeFromOpenList(self):
        return self.open_list.pop(0)

    def addInOpenList(self, node):
        self.open_list.append(node)

    def __str__(self):
        return "Breadth-First Search method"

