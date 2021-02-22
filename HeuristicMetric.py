
class HeuristicMetric:

    def __init__(self):
        print("Standard metric")


    def calculate(self, state):
        return 0.0

class ManhatamDist(HeuristicMetric):

    def __init__(self):
        print("Using Manhatam Distance!")

    def calculate(self, state, goal):
        dx = abs(state.coord[0] - goal.coord[0])
        dy = abs(state.coord[1] - goal.coord[1])
        return (dx + dy)

class OctileDist(HeuristicMetric):

    def __init__(self):
        print("Using Octile Distance")
    
    def max(a,b):
        if a >= b:
            return a
        else:
            return b

    def min(a,b):
        if a <= b:
            return a
        else:
            return b

    def calculate(self, state, goal):
        dx = abs(state.coord[0] - goal.coord[0])
        dy = abs(state.coord[1] - goal.coord[1])
        fn = max(dx,dy) + 0.5 * min(dx,dy)
        return fn