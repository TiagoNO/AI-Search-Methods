 
import pygame

# colors in rendering
GOAL_COLOR = (233, 196, 106)
OBSTACLES_COLOR = (42, 157, 143)
NOT_VISITED_COLOR = (38, 70, 83)

OPEN_LIST_COLOR = (231, 91, 60)
CLOSED_LIST_COLOR = (244, 162, 97)

MARGIN_COLOR = (24, 24, 26)
PATH_COLOR = (110, 141, 100)

# type in tilemap
GOAL = 0
OPEN_LIST = 1
CLOSED_LIST = 2
OBSTACLES = 3
NOT_VISITED = 4
PATH = 5

class GUI:

    def __init__(self, screen_size, initial_position, goal_position):
        pygame.init()

        # Set the width and height of the screen [width, height]
        self.screen_size = screen_size
        self.display = pygame.display.set_mode(self.screen_size)

        self.block_size = 20
        self.margin = 5

        #pygame.display.set_caption("My Game")
        pygame.display.set_caption("My Game")
 
        # Loop until the user clicks the close button.
        self.done = False
 
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        self.initializeTileMap(initial_position)

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.goal = goal_position

    def initializeTileMap(self, initial_position):
        self.tile_map = []
        total_block_size = (self.block_size + self.margin)
        n_width_cubes = int(self.screen_size[0]/total_block_size)
        n_height_cubes = int(self.screen_size[1]/total_block_size)

        for j in range(0, n_height_cubes):
            line = []
            for i in range(0, n_width_cubes):
                line.append(0)
            self.tile_map.append(line)
            self.position = initial_position
        #print(self.position)

    def setMap(self, game_map):
        for j in range(len(self.tile_map)):
            for i in range(len(self.tile_map[j])):
                x = self.position[0] + i
                y = self.position[1] + j

                #print("Position: ",self.position, "Index: ", (i, j))

                if(game_map.getTile((y, x)) == '@'):
                    self.tile_map[j][i] = OBSTACLES

                elif(game_map.getTile((y, x)) == '.'):
                    self.tile_map[j][i] = NOT_VISITED

        x = self.goal[0] - self.position[1]
        y = self.goal[1] - self.position[0]

        if(self.inFrame(x, y)):
            self.tile_map[x][y] = GOAL

    def movePositionRight(self, game_map):
        total_block_size = (self.block_size + self.margin)
        n_width_cubes = int(self.screen_size[1]/total_block_size)

        self.position[1] = int(self.position[1] + n_width_cubes/2)
        if(self.position[1] + n_width_cubes > game_map.width):
            self.position[1] -= (self.position[1] + n_width_cubes - game_map.width)

    def inFrame(self, x, y):
        total_block_size = (self.block_size + self.margin)
        n_width_cubes = int(self.screen_size[0]/total_block_size)
        n_height_cubes = int(self.screen_size[1]/total_block_size)

        if(x >= n_height_cubes or x < 0):
            return False
        
        if(y >= n_width_cubes or y < 0):
            return False
            
        #print([x, y], [n_width_cubes, n_height_cubes])
        return True

    def setOpenList(self, open_list, game_map):
        for s in open_list:
            x = s[1].coord[0] - self.position[1]
            y = s[1].coord[1] - self.position[0]


            if(self.inFrame(x, y)):
                self.tile_map[x][y] = OPEN_LIST

    def setClosedList(self, closed_list):
        for c in closed_list:
            x = c[0] - self.position[1]
            y = c[1] - self.position[0]

            if(self.inFrame(x, y)):
                self.tile_map[x][y] = CLOSED_LIST

    def setBestPath(self, best_path):
        #print(best_path)
        for b in best_path:
            x = b[1][0] - self.position[1]
            y = b[1][1] - self.position[0]

            if(self.inFrame(x, y)):
                self.tile_map[x][y] = PATH



    def getTileColor(self, w, h):
        if(self.tile_map[w][h] == OPEN_LIST):
            return OPEN_LIST_COLOR

        elif(self.tile_map[w][h] == CLOSED_LIST):
            return CLOSED_LIST_COLOR
        
        elif(self.tile_map[w][h] == OBSTACLES):
            return OBSTACLES_COLOR
        
        elif(self.tile_map[w][h] == GOAL):
            return GOAL_COLOR

        elif(self.tile_map[w][h] == NOT_VISITED):
            return NOT_VISITED_COLOR

        elif(self.tile_map[w][h] == PATH):
            return PATH_COLOR

    def draw(self):
        total_block_size = (self.block_size + self.margin)

        for j in range(len(self.tile_map)):
            for i in range(len(self.tile_map[j])):
                rect = pygame.Rect(i*total_block_size, j*total_block_size, self.block_size, self.block_size)                
                pygame.draw.rect(self.display, self.getTileColor(j, i), rect)
    
    def close(self):
        pygame.quit()

    def moveFrameDown(self, game_map):
        total_block_size = (self.block_size + self.margin)
        n_height_cubes = int(self.screen_size[1]/total_block_size)
        self.position[1] = min(self.position[1] + 1, game_map.height - n_height_cubes)

    def moveFrameUP(self, game_map):
        self.position[1] = max(0, self.position[1] - 1)

    def moveFrameLeft(self, game_map):
        self.position[0] = max(0, self.position[0] - 1)

    def moveFrameRight(self, game_map):
        total_block_size = (self.block_size + self.margin)
        n_width_cubes = int(self.screen_size[0]/total_block_size)
        self.position[0] = min(self.position[0] + 1, game_map.width - n_width_cubes)

    def handleEvents(self):
        for event in pygame.event.get(): #look at all events
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    self.down = True

                if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    self.up = True

                if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    self.left = True

                if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    self.right = True

            if event.type == pygame.KEYUP:
                if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    self.down = False

                if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    self.up = False

                if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    self.left = False

                if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    self.right = False


            if event.type == pygame.QUIT:
                self.done = True

    def handleMovement(self, game_map):
        if self.up:
            self.moveFrameUP(game_map)

        if self.down:
            self.moveFrameDown(game_map)

        if self.left:
            self.moveFrameLeft(game_map)

        if self.right:
            self.moveFrameRight(game_map)

    def exit(self, game_map, open_list, closed_list, best_path):
        while not self.done:
            self.step(game_map, open_list, closed_list, best_path)

    def step(self, game_map, open_list, closed_list, best_path):
        self.handleEvents()
        self.handleMovement(game_map)

        # --- Game logic should go here
    
        # --- Screen-clearing code goes here
        self.display.fill(MARGIN_COLOR)
    
        # --- Drawing code should go here
        self.setMap(game_map)
        self.setOpenList(open_list, game_map)
        self.setClosedList(closed_list)
        if(best_path != None):
            self.setBestPath(best_path)
        self.draw()
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # --- Limit to 60 frames per second
        self.clock.tick(60)        

    def update(self, game_map, open_list, closed_list, best_path):
        self.step(game_map, open_list, closed_list, best_path)
        if(best_path != None):
            self.exit(game_map, open_list, closed_list, best_path)
