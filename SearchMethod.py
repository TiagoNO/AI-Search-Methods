from heapq import *
from State import State
from HeuristicMetric import ManhatamDist

class Node:
    def __init__(self, state, cost, depth, parent):
        self.state = state
        self.cost = cost
        self.depth = depth
        self.parent = parent

    def isGoal(self, goal_state):
        return (self.state == goal_state)

    def getParent(self):
        return self.parent

    def isRoot(self):
        if(self.parent == None):
            return True
        return False 

    def __le__(self, other_node):
        if(self.cost <= other_node.cost):
            return True
        return False
    
    def __lt__(self, other_node):
        if(self.cost < other_node.cost):
            return True
        return False

class SearchMethod:

    def __init__(self, initial_state, goal):
        self.initial_node = Node(initial_state, 0, 0, None)
        self.current_node = None
        self.goal = goal

        self.open_list = []
        self.open_list_map = {}
        self.closed_list = {}
        self.found_solution = False
        self.best_path = None

    def getPossibleMoves(self, game_map):
        possible_moves = []
        neighbors = game_map.getNeighbors(self.current_node.state)
        for n in neighbors:
            value = self.getStateValue(n)
            possible_moves.append(Node(n, value, self.current_node.depth+1, self.current_node))
        return possible_moves

    def getStateValue(self, node):
        return node.cost

    def inClosedList(self, node):
        if(node.coord in self.closed_list):
            return False
        return True

    def addClosedList(self, node):
        self.closed_list[node.state.coord] = node.cost

    def getNodeFromOpenList(self):
        # need to override!!
        print("NEED to override!!")
        return self.open_list[0]
        #return heappop(self.open_list)

    def addInOpenList(self, state):
        print("NEED to override!!")
        # need to override!!
        #heappush(self.open_list, state)

    def getNextNode(self):
        node = self.getNodeFromOpenList()
        if(node.state.coord in self.open_list_map):
            self.open_list_map.pop(node.state.coord)
        return node

    def replaceInOpenList(self, node):
        if(self.open_list_map[node.state.coord] > node.cost):
            for i in range(0, len(self.open_list)):
                if(self.open_list[i].state == node.state):
                    self.open_list[i] = node
                    self.open_list_map[node.state.coord] = node.cost
                    break

    def replaceFromClosedList(self, node):
        if(self.closed_list[node.state.coord] > node.cost):
            self.open_list.append(node)
            self.closed_list.pop(node.state.coord)

    def addNode(self, node):
        if(node.state.coord in self.open_list_map):
            self.replaceInOpenList(node)
        elif(node.state.coord in self.closed_list):
            self.replaceFromClosedList(node)
        else:
            self.addInOpenList(node)
            self.open_list_map[node.state.coord] = node.cost

    def writePath(self, game_map):
        self.best_path  = self.getPath()
        game_map.write_output_file(self.best_path)
        self.foundPathMessage(self.best_path)
        self.found_solution = True

    def search(self, game_map):
        while len(self.open_list) != 0:
            self.current_node = self.getNextNode()
            self.addClosedList(self.current_node)

            if(self.current_node.isGoal(self.goal)):
                self.writePath(game_map)
            
            next_states = self.getPossibleMoves(game_map)
            for ns in next_states:
                self.addNode(ns)
        
        self.noSolutionMessage()
        self.found_solution = False

    def step(self, game_map):
        self.current_node = self.getNextNode()
        self.addClosedList(self.current_node)

        if(self.current_node.isGoal(self.goal)):
            self.writePath(game_map)
            return 
        
        next_nodes = self.getPossibleMoves(game_map)
        for ns in next_nodes:
            self.addNode(ns)

        if(len(self.open_list) == 0):
            self.noSolutionMessage()
            self.found_solution = False
            
    def noSolutionMessage(self):
        print(self.__str__() + ": there is no solution for the goal and map given...")

    def getPath(self):
        node = self.current_node
        path = [(node.state.cost, node.state.coord)]

        while not node.isRoot():
            node = node.parent
            path.append((node.state.cost, node.state.coord))
        return path

    def getOpenListStates(self):
        states = []
        for n in self.open_list:
            states.append(n.state)
        return states

    def getClosedListStates(self):
        states = []
        for n in self.closed_list:
            states.append(n.state)
        return states

    def foundPathMessage(self, path):
        print("Found an path with {} cost!!".format(path[0][0]))

    def __str__(self):
        return "Stardard: "

    def foundSolution(self):
        return self.found_solution