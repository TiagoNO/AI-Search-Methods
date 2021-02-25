from SearchMethod import SearchMethod, Node

class IDSearch(SearchMethod):

    def __init__(self, initial_state, goal, limit):
        super().__init__(initial_state, goal)
        self.open_list.append(Node(initial_state, 0, 0, None))
        self.limit = limit
        self.out_of_bounds = []
        self.paths = []

    def getNodeFromOpenList(self):
        return self.open_list.pop(len(self.open_list) - 1)

    def addInOpenList(self, state):
        self.open_list.append(state)

    def reachedLim(self):
        if(self.current_node.depth <= self.limit):
            return False
        return True

    def choosePath(self, paths_found):
        minP = paths_found[0]
        for p in paths_found:
            if(p <= minP):
                minP = p
        self.current_node = minP

    def increaseLimit(self):
        print("New limit: ", self.limit)
        self.limit += 30
        self.open_list.clear()
        self.closed_list.clear()
        self.open_list_map.clear()

        for os in self.out_of_bounds:
            self.addNode(os)

        self.out_of_bounds.clear()

    def reachedMaxLim(self, game_map):
        if(self.limit > game_map.height * game_map.width):
            return True

    def search(self, game_map):
        while not self.reachedMaxLim(game_map):
            self.current_node = self.getNextNode()
            self.addClosedList(self.current_node)

            if(self.current_node.isGoal(self.goal)):
                self.paths.append(self.current_node)
            
            next_nodes = self.getPossibleMoves(game_map)
            for ns in next_nodes:
                if not self.reachedLim():
                    self.addNode(ns)
                else:
                    self.out_of_bounds.append(ns)

            if len(self.open_list) == 0:
                self.increaseLimit()
        

        if len(self.paths) == 0:
            return False

        else:
            print("Num paths: ", len(self.paths))
            self.choosePath(self.paths)
            self.writePath(game_map)
            return True

    def step(self, game_map):
        self.current_node = self.getNextNode()
        self.addClosedList(self.current_node)

        if(self.current_node.isGoal(self.goal)):
            self.paths.append(self.current_node)
        
        next_nodes = self.getPossibleMoves(game_map)
        for ns in next_nodes:
            if not self.reachedLim():
                self.addNode(ns)
            else:
                self.out_of_bounds.append(ns)

        if len(self.open_list) == 0:
            if(len(self.paths) != 0):
                self.choosePath(self.paths)
                self.writePath(game_map)
                return True

            self.increaseLimit()
            if(self.reachedMaxLim(game_map)):
                self.noSolutionMessage()
                self.found_solution = False
                return False

    def __str__(self):
        return "Iteractive Depth Search method"
