

def is_goal(state,goal):
    if state[2][0] == goal[0] and state[2][1] == goal[1]:
        return True
    else:
        return False

def validInClosedList(open_list,map_list,closed_list,state):
    if closed_list.has_key(state[2]):
#        print state,closed_list[state[2]]
        if state[0] < closed_list[state[2]][0]:
                add_open_list(open_list,map_list,[state])
        return False
    else:
        return True


def getPossibleMoves(map,map_height,map_width,open_list,map_list,closed_list,state):
    nextStates = []
    up = False
    down = False
    left = False
    right = False

    x = state[2][0]
    y = state[2][1]
    cost = state[0] + 1.0
    tree_level = state[1] + 1
    father = [x,y]

    if x - 1 >= 0:
        n_state = [cost,tree_level,(x-1,y),father]
        if map[x-1][y] != '@':
            nextStates.append(n_state)
            up = True

    if x + 1 < map_height:
        n_state = [cost,tree_level,(x+1,y),father]
        if map[x+1][y] != '@':
            nextStates.append(n_state)
            down = True

    if y - 1 >= 0:
        n_state = [cost,tree_level,(x,y-1),father]
        if map[x][y-1] != '@':
            nextStates.append(n_state)
            left = True

    if y + 1 < map_width:
        n_state = [cost,tree_level,(x,y+1),father]
        if map[x][y+1] != '@':
            nextStates.append(n_state)
            right = True

    if up and left:
        n_state = [cost+0.5,tree_level,(x-1,y-1),father]
        if map[x-1][y-1] != '@':
            nextStates.append(n_state)

    if up and right:
        n_state = [cost+0.5,tree_level,(x-1,y+1),father]
        if map[x-1][y+1] != '@':
            nextStates.append(n_state)

    if down and left:
        n_state = [cost+0.5,tree_level,(x+1,y-1),father]
        if map[x+1][y-1] != '@':
            nextStates.append(n_state)

    if down and right:
        n_state = [cost+0.5,tree_level,(x+1,y+1),father]
        if map[x+1][y+1] != '@':
            nextStates.append(n_state)

    return nextStates

#def minPath(pathA,pathB):

#def goalFound(min):

def ids_write_arq(dir,map):
    arq = open(dir,"w")
    
    for line in map:
        for char in line:
            arq.write(str(char))
        arq.write('\n')


def getNextState(open_list,map_list):
    state = open_list.pop(len(open_list) - 1)
    if map_list.has_key(state[2]):
        map_list.pop(state[2])
    return state

def add_closed_list(closed_list,state):
    closed_list[state[2]] = state

def add_open_list(open_list,map_list,s):
    if map_list.has_key(s[2]):
        index = map_list[s[2]]
        if open_list[index][0] >= s[0]:
            open_list[index] = s           
    else:
        map_list[s[2]] = len(open_list)
        open_list[len(open_list)] = s

def is_valid(open_list,map_list,closed_list,state):
    if closed_list.has_key(state[2]):
        if closed_list[state[2]][0] > state[0]:
            add_open_list(open_list,map_list,state)
            closed_list.pop(state[2])
        return False
    else:
        return True

def reached_lim(state,lim):
    if state[1] >= lim:
        return True
    else:
        return False

def pause_execution():
    a = raw_input("pressione enter para continuar...")

def choose_min_path(paths):
    minS = paths[0]
    for s in paths:
        if minS[0] > s[0]:
            minS = s
    return minS

def ids_search(map,map_height,map_width,open_list,map_list,closed_list,goal,lim):
    paths = []
    while len(open_list) != 0:
        state = getNextState(open_list,map_list)
        #map[state[2][0]][state[2][1]] = 'x'
        add_closed_list(closed_list,state)

        if is_goal(state,goal):
            #imprime_caminho(map,closed_list,state)
            paths.append(state)

#        if lim > 20:
#            pause_execution()

        if not reached_lim(state,lim):
            nextValidStates = getPossibleMoves(map,map_height,map_width,open_list,map_list,closed_list,state)
            for s in nextValidStates:
                if is_valid(open_list,map_list,closed_list,s):
                    add_open_list(open_list,map_list,s)
    if len(paths) == 0:
        return False
    else:
        minP = choose_min_path(paths)    
        #print minP[0],minP[2]
        imprime_caminho(map,closed_list,minP)
        return True

def ids_no_solution(state,goal):
    print "<" + str(state[0]) + "," + str(state[1]) + ",0>"
    print "<" + str(goal[0]) + "," + str(goal[1]) + ",inf>" 

def isRoot(state):
    if state[3][0] == -1 and state[3][1] == -1:
        return True
    else:
        return False

def getFather(closed_list,state):
    return closed_list[(state[3][0],state[3][1])]

def out_put(path):
    print "<" + str(path[0][2][0]) + "," + str(path[0][2][1]) + "," + str(path[0][0]) + ">"
    print "<" + str(path[-1][2][0]) + "," + str(path[-1][2][1]) + "," + str(path[-1][0]) + ">\n"
    for s in path:
        print "<" + str(s[2][0]) + "," + str(s[2][1]) + "," + str(s[0]) + ">",
    print "\n"


def imprime_caminho(map,closed_list,state):
    path = []
    i = 1
    p_state = state
    map[p_state[2][0]][p_state[2][1]] = 'x'
    path.insert(0,[p_state[0],p_state[1],p_state[2]])
    while not isRoot(p_state):
        p_state = getFather(closed_list,p_state)
        map[p_state[2][0]][p_state[2][1]] = 'x'
        path.insert(0,[p_state[0],p_state[1],p_state[2]])
        i += 1
    #write_arq("ids_Final_log",map)
    out_put(path)  
    print i
