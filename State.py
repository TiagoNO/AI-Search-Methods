
class State:

    def __init__(self, coord, heuristic, cost, parent):
        self.cost = cost
        self.coord = coord
        self.parent = parent
        
    def isGoal(self, goal_state):
        if(self.coord[0] == goal_state.coord[0] and self.coord[1] == goal_state.coord[1]):
            return True

        return False

    def getParent(self):
        return self.parent

    def isRoot(self):
        if(self.parent == None):
            return True
        return False

    def __le__(self, other_state):
        if(self.cost <= other_state.cost):
            return self
        return other_state
    
    def __lt__(self, other_state):
        if(self.cost < other_state.cost):
            return self
        return other_state
