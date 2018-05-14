from heapq import *

def is_goal(state,goal):
    if state[1][0] == goal[0] and state[1][1] == goal[1]:
        return True
    else:
        return False

def validInClosedList(closed_list,state):
    if not closed_list.has_key(state):
        return True
    else:
        return False


def getPossibleMoves(map,map_height,map_width,heap,heap_map,state):
    nextStates = []
    up = False
    down = False
    left = False
    right = False

    x = state[1][0]
    y = state[1][1]
    cost = state[0] + 1.0
    father = (x,y)

    if x - 1 >= 0:
        if map[x-1][y] != '@' and validInClosedList(heap_map,(x-1,y)):
            nextStates.append([cost,(x-1,y),father])
            up = True

    if x + 1 < map_height:
        if map[x+1][y] != '@' and validInClosedList(heap_map,(x+1,y)):
            nextStates.append([cost,(x+1,y),father])
            down = True

    if y - 1 >= 0:
        if map[x][y-1] != '@' and validInClosedList(heap_map,(x,y-1)):
            nextStates.append([cost,(x,y-1),father])
            left = True

    if y + 1 < map_width:
        if map[x][y+1] != '@' and validInClosedList(heap_map,(x,y+1)):
            nextStates.append([cost,(x,y+1),father])
            right = True

    if up and left:
        if map[x-1][y-1] != '@' and validInClosedList(heap_map,(x-1,y-1)):
            nextStates.append([cost+0.5,(x-1,y-1),father])

    if up and right:
       if map[x-1][y+1] != '@' and validInClosedList(heap_map,(x-1,y+1)):
            nextStates.append([cost+0.5,(x-1,y+1),father])

    if down and left:
       if map[x+1][y-1] != '@' and validInClosedList(heap_map,(x+1,y-1)):
            nextStates.append([cost+0.5,(x+1,y-1),father])

    if down and right:
       if map[x+1][y+1] != '@' and validInClosedList(heap_map,(x+1,y+1)):
            nextStates.append([cost+0.5,(x+1,y+1),father])

    return nextStates

def ucs_write_arq(dir,map):
    arq = open(dir,"w")
    
    for line in map:
        for char in line:
            arq.write(str(char))
        arq.write('\n')

def add_closed_list(closed_list,state):
    closed_list[state[1]] = state

def add_in_heap(heap,heap_map,state):
    if heap_map.has_key(state[1]):
        if heap_map[state[1]][0] > state[0]:
            heapreplace(heap,state)
    else:
        heappush(heap,state)
        heap_map[state[1]] = state

def ucs_search(map,map_height,map_width,heap,heap_map,goal):
    while heap:
        state = heappop(heap)
        #map[state[1][0]][state[1][1]] = 'x'
        add_closed_list(heap_map,state)

        if is_goal(state,goal):
#            print state[0],state[1]
            imprime_caminho(map,heap_map,state)
            return True

        else:
            nextValidStates = getPossibleMoves(map,map_height,map_width,heap,heap_map,state)
            for s in nextValidStates:
                add_in_heap(heap,heap_map,s)
    return False

def ucs_no_solution(state,goal):
    print "<" + str(state[1][0]) + "," + str(state[1][1]) + ",0>"
    print "<" + str(goal[0]) + "," + str(goal[1]) + ",inf>" 


def isRoot(state):
    if state[2][0] == -1 and state[2][1] == -1:
        return True
    else:
        return False

def getFather(closed_list,state):
    return closed_list[state[2]]

def out_put(path):
    print "<" + str(path[0][1][0]) + "," + str(path[0][1][1]) + "," + str(path[0][0]) + ">"
    print "<" + str(path[-1][1][0]) + "," + str(path[-1][1][1]) + "," + str(path[-1][0]) + ">\n"
    for s in path:
        print "<" + str(s[1][0]) + "," + str(s[1][1]) + "," + str(s[0]) + ">",
    print "\n"

def imprime_caminho(map,closed_list,state):
    path = []
    i = 1
    p_state = state
    map[state[1][0]][state[1][1]] = 'x'
    path.insert(0,[p_state[0],p_state[1],p_state[2]])
    while not isRoot(p_state):
        p_state = getFather(closed_list,p_state)
        map[p_state[1][0]][p_state[1][1]] = 'x'
        path.insert(0,[p_state[0],p_state[1],p_state[2]])
        i += 1
    out_put(path)
    #print i
    return path
