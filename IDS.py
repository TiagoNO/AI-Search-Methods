

def is_goal(state,goal):
    if state[0] == goal[0] and state[1] == goal[1]:
        return True
    else:
        return False

def validInClosedList(closed_list,state):
    #not map_list.has_key((state[0],state[1])) and 
    if not closed_list.has_key((state[0],state[1])):
        #print closed_list,state
        return True
    else:
        return False


def getPossibleMoves(map,map_height,map_width,open_list,map_list,closed_list,state):
    nextStates = []
    up = False
    down = False
    left = False
    right = False

    x = state[0]
    y = state[1]
    cost = state[2] + 1
    father = [x,y]

    if x - 1 >= 0:
        if map[x-1][y] != 1 and validInClosedList(closed_list,[x-1,y]):
            nextStates.append([x-1,y,cost,father])
            up = True

    if x + 1 < map_height:
        if map[x+1][y] != 1 and validInClosedList(closed_list,[x+1,y]):
            nextStates.append([x+1,y,cost,father])
            down = True

    if y - 1 >= 0:
        if map[x][y-1] != 1 and validInClosedList(closed_list,[x,y-1]):
            nextStates.append([x,y-1,cost,father])
            left = True

    if y + 1 < map_width:
        if map[x][y+1] != 1 and validInClosedList(closed_list,[x,y+1]):
            nextStates.append([x,y+1,cost,father])
            right = True

    if up and left:
        if map[x-1][y-1] != 1 and validInClosedList(closed_list,[x-1,y-1]):
            nextStates.append([x-1,y-1,cost,father])

    if up and right:
       if map[x-1][y+1] != 1 and validInClosedList(closed_list,[x-1,y+1]):
            nextStates.append([x-1,y+1,cost,father])

    if down and left:
       if map[x+1][y-1] != 1 and validInClosedList(closed_list,[x+1,y-1]):
            nextStates.append([x+1,y-1,cost,father])

    if down and right:
       if map[x+1][y+1] != 1 and validInClosedList(closed_list,[x+1,y+1]):
            nextStates.append([x+1,y+1,cost,father])

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
    if state[2] > lim:
        return True
    else:
        return False

def search(map,map_height,map_width,open_list,map_list,closed_list,goal,lim):
    tree_level = 0
    while len(open_list) != 0:
        state = getNextState(open_list,map_list)
        map[state[0]][state[1]] = 3
        add_closed_list(closed_list,state)
        #print "Current state:",state

        if is_goal(state,goal):
            #print state,goal
            imprime_caminho(closed_list,state)
            return True
            #print "found!"

        elif reached_lim(state,lim):
            i = 0
            #print 'lim reached!'

        else:
            nextValidStates = getPossibleMoves(map,map_height,map_width,open_list,map_list,closed_list,state)
            #print nextValidStates
            add_open_list(open_list,map_list,nextValidStates)
            #print "Open list:",open_list
            #print "Closed list:",closed_list
            #print '\n'
            tree_level += 1

def isRoot(state):
    if state[3][0] == -1 and state[3][1] == -1:
        return True
    else:
        return False

def getFather(closed_list,state):
    #print closed_list[(state[0],state[1])]
    return closed_list[(state[3][0],state[3][1])]

def imprime_caminho(closed_list,state):
    path = []
    p_state = state
    path.insert(0,[p_state[0],p_state[1],p_state[2]])
    while not isRoot(p_state):
        #print p_state
        p_state = getFather(closed_list,p_state)
        path.insert(0,[p_state[0],p_state[1],p_state[2]])
    print path    
