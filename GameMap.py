from State import State

class GameMap:

    def __init__(self, filename):
        self.readFromFile(filename)
        self.cost = 1
        self.diagonal_cost = 0.5
        self.boost_rate = 1

    def reduceCost(self):
        self.cost = self.boost_rate * self.cost
        self.diagonal_cost = self.boost_rate * self.diagonal_cost

    def getNeighbors(self, state):
        neighbors = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                x_axis = state.coord[0] + i
                y_axis = state.coord[1] + j
                cost = state.cost + self.cost

                # checking if the coordinates are inside the map
                if(x_axis < 0 or x_axis >= self.height):
                    continue

                # checking if the coordinates are inside the map
                if(y_axis < 0 or y_axis >= self.width):
                    continue

                #print(state.coord, x_axis, y_axis)

                if(self.map[x_axis][y_axis] == '@'):
                    continue

                # checking if its not adding the same state
                if(i == 0 and j == 0):
                    continue

                # diagonals movements are more expensive!
                if(i != 0 and j != 0):
                    cost += self.diagonal_cost

                neighbors.append(State((x_axis, y_axis), cost))
        return neighbors

    def readFromFile(self, filename):
        self.filename = filename
        file_ptr = open(self.filename, "r")

        self.type = str(file_ptr.readline().split()[1])
        self.height = int(file_ptr.readline().split()[1])
        self.width = int(file_ptr.readline().split()[1])
        self.name = str(file_ptr.readline())

        self.map = []

        for line in file_ptr.readlines():
            map_line = []
            for c in line:
                if(c == '.' or c == '@'):
                    map_line.append(c)
            self.map.append(map_line)
        
        file_ptr.close()

    def getTile(self, coord):
        #print("2: ", self.map[0])
        return self.map[coord[0]][coord[1]]

    def setTile(self, coord, value):
        self.map[coord[0]][coord[1]] = value

    def write_output_file(self, path):
        for s in path:
            self.map[s[1][0]][s[1][1]] = 'x'
        
        output_file = open(self.filename + "_output.txt", "w")
        for x in range(0, len(self.map)):
            for y in range(0, len(self.map[x])):
                output_file.write(self.map[x][y])
            output_file.write("\n")

    def size(self):
        return [self.width, self.height]

    def __str__(self):
        return self.map.__str__()