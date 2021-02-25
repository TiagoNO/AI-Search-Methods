 
import pygame
import math

# colors in rendering
START_COLOR = (233, 124, 97)
GOAL_COLOR = (233, 196, 106)
OBSTACLES_COLOR = (42, 157, 143)
NOT_VISITED_COLOR = (38, 70, 83)

OPEN_LIST_COLOR = (231, 91, 60)
CLOSED_LIST_COLOR = (244, 162, 97)

MARGIN_COLOR = (24, 24, 26)
PATH_COLOR = (110, 141, 100)

Error_color = (0, 0, 0)

# type in tilemap
START = 0
GOAL = 1
OPEN_LIST = 2
CLOSED_LIST = 3
OBSTACLES = 4
NOT_VISITED = 5
PATH = 6
ERROR = 7

class GUI:

    def __init__(self, screen_size, start, goal, game_map, ratio=1):
        pygame.init()

        # Set the width and height of the screen [width, height]
        self.screen_size = screen_size
        self.display = pygame.display.set_mode(self.screen_size)
        self.ratio = ratio
        self.setElementSizes(game_map)

        #pygame.display.set_caption("My Game")
        pygame.display.set_caption("Search Method")
 
        # Loop until the user clicks the close button.
        self.done = False
 
        # initialize tile map
        self.start = start
        self.goal = goal
        self.position = start

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # controllers
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.zoom_in = False
        self.zoom_out = False

    def zoomIn(self):
        self.ratio = max(0.12, self.ratio-0.22)

    def zoomOut(self):
        self.ratio = min(1, self.ratio+0.22)

    def setElementSizes(self, game_map):
        self.margin = 1

        # the frame of the original map that we will show!
        self.tile_map_size = [0, 0]
        self.tile_map_size[0] = int(max(1, self.ratio * game_map.width))
        self.tile_map_size[1] = int(max(1, self.ratio * game_map.height))
 
        self.w_block_sz = int(self.screen_size[0] / (self.tile_map_size[0])) - self.margin
        self.h_block_sz = int(self.screen_size[1] / (self.tile_map_size[1])) - self.margin

        self.w_number_blocks = int(self.screen_size[0] / (self.w_block_sz + self.margin))
        self.h_number_blocks = int(self.screen_size[1] / (self.h_block_sz + self.margin))

        #print(self.w_block_sz, self.h_block_sz)
        #print(self.w_number_blocks, self.h_number_blocks)
        #print(self.tile_map_size, self.ratio)
        self.initializeTileMap(game_map)

    def initializeTileMap(self, game_map):
        self.tile_map = []
        for i in range(0, game_map.height):
            line = []
            for j in range(0, game_map.width):
                line.append(0)
            self.tile_map.append(line)

        #print(self.tile_map)
        #print("AHHH:", len(self.tile_map), len(self.tile_map[0]))

        #print(self.position)

    def inFrame(self, x, y):
        #print(x, y, self.h_number_blocks, self.w_number_blocks)
        if(x >= self.h_number_blocks or x < 0):
            return False
        
        if(y >= self.w_number_blocks or y < 0):
            return False
        
        return True

    def setMap(self, game_map):
        for i in range(self.tile_map_size[0]):
            for j in range(self.tile_map_size[1]):
                x = self.position[0] + i
                y = self.position[1] + j

                if(game_map.getTile((y, x)) == '@'):
                    self.tile_map[j][i] = OBSTACLES

                elif(game_map.getTile((y, x)) == '.'):
                    self.tile_map[j][i] = NOT_VISITED

    def setStartAndFinish(self):
        x = self.start[0] - self.position[1]
        y = self.start[1] - self.position[0]
        
        if(self.inFrame(x, y)):
            self.tile_map[x][y] = START

        x = self.goal[0] - self.position[1]
        y = self.goal[1] - self.position[0]

        if(self.inFrame(x, y)):
            self.tile_map[x][y] = GOAL            


    def setOpenList(self, open_list, game_map):
        for s in open_list:
            x = s.coord[0] - self.position[1]
            y = s.coord[1] - self.position[0]


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
        if(self.tile_map[w][h] == START):
            return START_COLOR

        elif(self.tile_map[w][h] == OPEN_LIST):
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
        
        elif(self.tile_map[w][h] == ERROR):
            return Error_color

    def draw(self):
        for j in range(self.tile_map_size[1]):
            for i in range(self.tile_map_size[0]):
                rect = pygame.Rect(i*(self.w_block_sz+self.margin), j*(self.h_block_sz+self.margin), self.w_block_sz, self.h_block_sz)
                pygame.draw.rect(self.display, self.getTileColor(j, i), rect)
    
    def close(self):
        pygame.quit()

    def moveFrameDown(self, game_map):
        self.position[1] = min(self.position[1] + 1, game_map.height - self.tile_map_size[1])

    def moveFrameUP(self, game_map):
        self.position[1] = max(0, self.position[1] - 1)

    def moveFrameLeft(self, game_map):
        self.position[0] = max(0, self.position[0] - 1)

    def moveFrameRight(self, game_map):
        self.position[0] = min(self.position[0] + 1, game_map.width - self.tile_map_size[0])

    # set the position of the camera in a valid position
    def validPosition(self, game_map):        
        self.position[0] = max(0, self.position[0])
        self.position[1] = max(0, self.position[1])
        
        self.position[0] = min(self.position[0], game_map.width - self.tile_map_size[0])
        self.position[1] = min(self.position[1], game_map.height - self.tile_map_size[1])

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

                if(event.key == pygame.K_x):
                    self.zoom_in = True

                if(event.key == pygame.K_z):
                    self.zoom_out = True


            if event.type == pygame.KEYUP:
                if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    self.down = False

                if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    self.up = False

                if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    self.left = False

                if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    self.right = False

                if(event.key == pygame.K_x):
                    self.zoom_in = False

                if(event.key == pygame.K_z):
                    self.zoom_out = False


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

        if self.zoom_in:
            self.zoomIn()
            self.setElementSizes(game_map)
            self.zoom_in = False

        if self.zoom_out:
            self.zoomOut()
            self.setElementSizes(game_map)
            self.zoom_out = False

    def exit(self, game_map, open_list, closed_list, best_path):
        while not self.done:
            self.step(game_map, open_list, closed_list, best_path)

    def step(self, game_map, open_list, closed_list, best_path):
        # handling user events and performing the camera movements
        self.handleEvents()
        self.handleMovement(game_map)
    
        # --- Screen-clearing code
        self.display.fill(MARGIN_COLOR)
    
        # --- Drawing code
        self.validPosition(game_map)
        self.setMap(game_map)
        self.setOpenList(open_list, game_map)
        self.setClosedList(closed_list)
        if(best_path != None):
            self.setBestPath(best_path)
        self.setStartAndFinish()
        self.draw()

        pygame.display.flip()
        self.clock.tick(60)        

    def update(self, game_map, open_list, closed_list, best_path):
        self.step(game_map, open_list, closed_list, best_path)
        if(best_path != None):
            self.exit(game_map, open_list, closed_list, best_path)
