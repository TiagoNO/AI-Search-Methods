

def is_goal(state,goal):
    if state[0] == goal[0] and state[1] == goal[1]:
        return True
    else:
        return False

def validInClosedList(open_list,map_list,closed_list,state):
    state_key = (state[0],state[1])
    if closed_list.has_key(state_key):
        if state[2] < closed_list[state_key][2]:
            add_open_list(open_list,map_list,[state])
        return False
    elif map_list.has_key(state_key):
        index = map_list[state_key]
        if state[2] < open_list[index][2]:
            open_list[index] = state
        return False
    else:
        return True


def getPossibleMoves(map,map_height,map_width,open_list,map_list,closed_list,state):
    nextStates = []
    up = False
    down = False
    left = False
    right = False

    x = state[0]
    y = state[1]
    cost = state[2] + 1.0
    tree_level = state[3] + 1
    father = [x,y]

    if x - 1 >= 0:
        n_state = [x-1,y,cost,tree_level,father]
        if map[x-1][y] != 1 and validInClosedList(open_list,map_list,closed_list,n_state):
            nextStates.append([x-1,y,cost,tree_level,father])
            up = True

    if x + 1 < map_height:
        n_state = [x+1,y,cost,tree_level,father]
        if map[x+1][y] != 1 and validInClosedList(open_list,map_list,closed_list,n_state):
            nextStates.append([x+1,y,cost,tree_level,father])
            down = True

    if y - 1 >= 0:
        n_state = [x,y-1,cost,tree_level,father]
        if map[x][y-1] != 1 and validInClosedList(open_list,map_list,closed_list,n_state):
            nextStates.append([x,y-1,cost,tree_level,father])
            left = True

    if y + 1 < map_width:
        n_state = [x,y+1,cost,tree_level,father]
        if map[x][y+1] != 1 and validInClosedList(open_list,map_list,closed_list,n_state):
            nextStates.append([x,y+1,cost,tree_level,father])
            right = True

    if up and left:
        n_state = [x-1,y-1,cost,tree_level,father]
        if map[x-1][y-1] != 1 and validInClosedList(open_list,map_list,closed_list,n_state):
            nextStates.append([x-1,y-1,cost+0.5,tree_level,father])

    if up and right:
        n_state = [x-1,y+1,cost,tree_level,father]
        if map[x-1][y+1] != 1 and validInClosedList(open_list,map_list,closed_list,n_state):
            nextStates.append([x-1,y+1,cost+0.5,tree_level,father])

    if down and left:
        n_state = [x+1,y-1,cost,tree_level,father]
        if map[x+1][y-1] != 1 and validInClosedList(open_list,map_list,closed_list,n_state):
            nextStates.append([x+1,y-1,cost+0.5,tree_level,father])

    if down and right:
        n_state = [x+1,y+1,cost,tree_level,father]
        if map[x+1][y+1] != 1 and validInClosedList(open_list,map_list,closed_list,n_state):
            nextStates.append([x+1,y+1,cost+0.5,tree_level,father])

    return nextStates

#def minPath(pathA,pathB):

#def goalFound(min):

def write_arq(dir,map):
    arq = open(dir,"w")
    
    for line in map:
        for char in line:
            arq.write(str(char))
        arq.write('\n')


def getNextState(open_list,map_list):
    state = open_list.pop(len(open_list) - 1)
    if map_list.has_key((state[0],state[1])):
        map_list.pop((state[0],state[1]))
    return state

def add_closed_list(closed_list,state):
    closed_list[(state[0],state[1])] = state

def add_open_list(open_list,map_list,states):
    for s in states:
        state_key = (s[0],s[1])
        if map_list.has_key(state_key):
            index = map_list[state_key]
            if open_list[index][2] > s[2]:
                open_list[index] = s                
        else:
            map_list[state_key] = len(open_list)
            open_list[len(open_list)] = s

def reached_lim(state,lim):
    if state[3] >= lim:
        return True
    else:
        return False

def ids_search(map,map_height,map_width,open_list,map_list,closed_list,goal,lim):
    while len(open_list) != 0:
        state = getNextState(open_list,map_list)
        map[state[0]][state[1]] = 3
        add_closed_list(closed_list,state)

        if is_goal(state,goal):
            imprime_caminho(map,closed_list,state)
            return True

        if not reached_lim(state,lim):
            nextValidStates = getPossibleMoves(map,map_height,map_width,open_list,map_list,closed_list,state)
            add_open_list(open_list,map_list,nextValidStates)
    

def ids_no_solution(state,goal):
    print "<" + str(state[0]) + "," + str(state[1]) + ",0>"
    print "<" + str(goal[0]) + "," + str(goal[1]) + ",inf>" 

def isRoot(state):
    if state[4][0] == -1 and state[4][1] == -1:
        return True
    else:
        return False

def getFather(closed_list,state):
    return closed_list[(state[4][0],state[4][1])]

def out_put(path):
    print "<" + str(path[0][0]) + "," + str(path[0][1]) + "," + str(path[0][2]) + ">"
    print "<" + str(path[-1][0]) + "," + str(path[-1][1]) + "," + str(path[-1][2]) + ">"
    print "\n"
    for s in path:
        print "<" + str(s[0]) + "," + str(s[1]) + "," + str(s[2]) + ">",


def imprime_caminho(map,closed_list,state):
    path = []
    p_state = state
    path.insert(0,[p_state[0],p_state[1],p_state[2]])
    while not isRoot(p_state):
        p_state = getFather(closed_list,p_state)
        path.insert(0,[p_state[0],p_state[1],p_state[2]])
    #write_arq("ids_Final_log",map)
    out_put(path)  
