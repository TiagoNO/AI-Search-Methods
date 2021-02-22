from SearchMethod import SearchMethod

class IDSearch(SearchMethod):

    def __init__(self, initial_state, goal, limit):
        super().__init__(initial_state, goal)
        self.open_list.append((0, initial_state, 0))
        self.limit = limit
        self.out_of_bounds = []
        self.paths = []

    def getPossibleMoves(self, game_map):
        possible_moves = []
        neighbors = game_map.getNeighbors(self.current_state[1])
        for n in neighbors:
            possible_moves.append([n.cost, n, self.current_state[2] + 1])
        return possible_moves

    def getStateFromOpenList(self):
        return self.open_list.pop(len(self.open_list) - 1)

    def addInOpenList(self, state):
        self.open_list.append(state)

    def reachedLim(self):
        if(self.current_state[2] <= self.limit):
            return False
        return True

    def choosePath(self, paths_found):
        minP = paths_found[0]
        for p in paths_found:
            if(minP[0] >= p[0]):
                minP = p
        self.current_state = minP

    def increaseLimit(self):
        print("Limit: ", self.limit)
        self.limit += 30
        self.open_list.clear()
        self.closed_list.clear()
        self.open_list_map.clear()

        for os in self.out_of_bounds:
            self.addState(os)

        self.out_of_bounds.clear()

    def reachedMaxLim(self, game_map):
        if(self.limit >= game_map.height * game_map.width):
            return True

    def search(self, game_map):
        while not self.reachedMaxLim(game_map):
            self.current_state = self.getNextState()
            self.addClosedList(self.current_state)

            if(self.current_state[1].isGoal(self.goal)):
                self.paths.append(self.current_state)
            
            next_states = self.getPossibleMoves(game_map)
            for ns in next_states:
                if not self.reachedLim():
                    self.addState(ns)
                else:
                    self.out_of_bounds.append(ns)

            if len(self.open_list) == 0:
                self.increaseLimit()
        

        if len(self.paths) == 0:
            return False

        else:
            print("Num paths: ", len(self.paths))
            self.choosePath(self.paths)

            path = self.getPath()
            game_map.write_output_file(path)
            self.foundPathMessage(path)
            return True

    def step(self, game_map):
        self.current_state = self.getNextState()
        self.addClosedList(self.current_state)

        if(self.current_state[1].isGoal(self.goal)):
            self.paths.append(self.current_state)
        
        next_states = self.getPossibleMoves(game_map)
        for ns in next_states:
            if not self.reachedLim():
                self.addState(ns)
            else:
                self.out_of_bounds.append(ns)

        if len(self.open_list) == 0:
            if(len(self.paths) != 0):
                print("Num paths: ", len(self.paths))
                self.choosePath(self.paths)

                self.best_path = self.getPath()
                game_map.write_output_file(self.best_path)
                self.foundPathMessage(self.best_path)
                self.found_solution = True
            self.increaseLimit()

        if(self.reachedMaxLim(game_map)):
            self.noSolutionMessage()
            self.found_solution = False

    def __str__(self):
        return "Interactive Depth Search method"
