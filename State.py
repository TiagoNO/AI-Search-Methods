
class State:

    def __init__(self, coord, cost):
        self.coord = coord
        self.cost = cost

    def __eq__(self, other_state):
        if(self.coord[0] == other_state.coord[0] and self.coord[1] == other_state.coord[1]):
            return True
        return False
