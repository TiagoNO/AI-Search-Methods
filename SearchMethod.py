from heapq import *
from State import State
from HeuristicMetric import ManhatamDist

class SearchMethod:

    def __init__(self, initial_state, goal):
        self.initial_state = initial_state
        self.current_state = None
        self.goal = goal

        self.open_list = []
        self.open_list_map = {}
        self.closed_list = {}
        self.found_solution = False
        self.best_path = None

    def getPossibleMoves(self, game_map):
        possible_moves = []
        neighbors = game_map.getNeighbors(self.current_state[1])
        for n in neighbors:
            value = self.getStateValue(n)
            possible_moves.append([value, n])
        return possible_moves

    def getStateValue(self, state):
        return state.cost

    def inClosedList(self, state):
        if(state.coord in self.closed_list):
            return False
        return True

    def addClosedList(self, state):
        self.closed_list[state[1].coord] = state[0]

    def getStateFromOpenList(self):
        # need to override!!
        print("NEED to override!!")
        return self.open_list[0]
        #return heappop(self.open_list)

    def addInOpenList(self, state):
        print("NEED to override!!")
        # need to override!!
        #heappush(self.open_list, state)

    def getNextState(self):
        state = self.getStateFromOpenList()
        if(state[1].coord in self.open_list_map):
            self.open_list_map.pop(state[1].coord)
        return state

    def replaceInOpenList(self, state):
        if(self.open_list_map[state[1].coord] > state[0]):
            for i in range(0, len(self.open_list)):
                if(self.open_list[i][1].coord == state[1].coord):
                    self.open_list[i] = state
                    self.open_list_map[state[1].coord] = state[0]
                    break

    def replaceFromClosedList(self, state):
        if(self.closed_list[state[1].coord] > state[0]):
            self.open_list.append(state)
            self.closed_list.pop(state[1].coord)

    def addState(self, state):
        if(state[1].coord in self.open_list_map):
            self.replaceInOpenList(state)
        elif(state[1].coord in self.closed_list):
            self.replaceFromClosedList(state)
        else:
            self.addInOpenList(state)
            self.open_list_map[state[1].coord] = state[0]

    def writePath(self, game_map):
        self.best_path  = self.getPath()
        game_map.write_output_file(self.best_path)
        self.foundPathMessage(self.best_path)
        self.found_solution = True

    def search(self, game_map):
        while len(self.open_list) != 0:
            self.current_state = self.getNextState()
            self.addClosedList(self.current_state)

            if(self.current_state[1].isGoal(self.goal)):
                self.writePath(game_map)
            
            next_states = self.getPossibleMoves(game_map)
            for ns in next_states:
                self.addState(ns)
        
        self.noSolutionMessage()
        self.found_solution = False

    def step(self, game_map):
        self.current_state = self.getNextState()
        self.addClosedList(self.current_state)

        if(self.current_state[1].isGoal(self.goal)):
            self.writePath(game_map)
            return 
        
        next_states = self.getPossibleMoves(game_map)
        for ns in next_states:
            self.addState(ns)

        if(len(self.open_list) == 0):
            self.noSolutionMessage()
            self.found_solution = False
            
    def noSolutionMessage(self):
        print(self.__str__() + ": there is no solution for the goal and map given...")

    def getPath(self):
        state = self.current_state[1]
        path = [(state.cost, state.coord)]

        while not state.isRoot():
            state = state.getParent()
            path.append((state.cost, state.coord))

        return path

    def foundPathMessage(self, path):
        print("Found an path with {} cost!!".format(path[0][0]))

    def __str__(self):
        return "Stardard: "

    def foundSolution(self):
        return self.found_solution