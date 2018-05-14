

class inputManager:


    def __init__(self,argv):
        self.map = []
        self.map_name = str(argv[2])
        self.map_type = str()
        self.map_height = int()
        self.map_width = int()
        self.initial_state = (int(argv[3]),int(argv[4]))
        self.goal_state = (int(argv[5]),int(argv[6]))
        self.aStar = int(argv[7])
        self.get_map()

    def get_map(self):  
        arq = open("maps/" + self.map_name,"r")
        
        self.map_type = str(arq.readline().split()[1])

        self.map_height = int(arq.readline().split()[1])

        self.map_width = int(arq.readline().split()[1])
        
        aux = arq.readline()

        for line in arq.readlines():
            map_line = []
            for char in line:
                if char == '.':
                    map_line.append('.')
                elif char == '@':
                    map_line.append('@')
            self.map.append(map_line)

        arq.close()        