from heapq import *

def is_goal(state,goal):
    if state[1][0] == goal[0] and state[1][1] == goal[1]:
        return True
    else:
        return False

def validInClosedList(closed_list,state):
    if closed_list.has_key(state):
        return False
    else:
        return True


def getPossibleMoves(map,map_height,map_width,heap,heap_map,heuristic_map,state):
    nextStates = []
    up = False
    down = False
    left = False
    right = False

    x = state[1][0]
    cost = state[3] + 1.0
    y = state[1][1]
    father = (x,y)
    if x - 1 >= 0:
        if map[x-1][y] != '@' and validInClosedList(heap_map,(x-1,y)):
            heu_value = heuristic_map[(x-1,y)]
            nextStates.append([heu_value,(x-1,y),father,cost])
            up = True

    if x + 1 < map_height:
        if map[x+1][y] != '@' and validInClosedList(heap_map,(x+1,y)):
            heu_value = heuristic_map[(x+1,y)]
            nextStates.append([heu_value,(x+1,y),father,cost])
            down = True

    if y - 1 >= 0:
        if map[x][y-1] != '@' and validInClosedList(heap_map,(x,y-1)):
            heu_value = heuristic_map[(x,y-1)]
            nextStates.append([heu_value,(x,y-1),father,cost])
            left = True

    if y + 1 < map_width:
        if map[x][y+1] != '@' and validInClosedList(heap_map,(x,y+1)):
            heu_value = heuristic_map[(x,y+1)]
            nextStates.append([heu_value,(x,y+1),father,cost])
            right = True

    if up and left:
        if map[x-1][y-1] != '@' and validInClosedList(heap_map,(x-1,y-1)):
            heu_value = heuristic_map[(x-1,y-1)]
            nextStates.append([heu_value,(x-1,y-1),father,cost+0.5])

    if up and right:
       if map[x-1][y+1] != '@' and validInClosedList(heap_map,(x-1,y+1)):
            heu_value = heuristic_map[(x-1,y+1)]
            nextStates.append([heu_value,(x-1,y+1),father,cost+0.5])

    if down and left:
       if map[x+1][y-1] != '@' and validInClosedList(heap_map,(x+1,y-1)):
            heu_value = heuristic_map[(x+1,y-1)]
            nextStates.append([heu_value,(x+1,y-1),father,cost+0.5])

    if down and right:
       if map[x+1][y+1] != '@' and validInClosedList(heap_map,(x+1,y+1)):
            heu_value = heuristic_map[(x+1,y+1)]
            nextStates.append([heu_value,(x+1,y+1),father,cost+0.5])

    return nextStates

def manhatam_dist(state,goal):
    dx = abs(state[0] - goal[0])
    dy = abs(state[1] - goal[1])
    return dx + dy

def bfs_calculate_heuristic(map,map_height,map_width,heuristic_map,goal_state):
    for i in xrange(map_height):
        for j in xrange(map_width):
            if map[i][j] == '.':
                heuristic_map[(i,j)] = manhatam_dist((i,j),goal_state)

def bfs_write_arq(dir,map):
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

def bfs_search(map,map_height,map_width,heap,heap_map,heuristic_map,goal):
    while heap:
        state = heappop(heap)
        add_closed_list(heap_map,state)
#        print state
        #print state

        if is_goal(state,goal):
            #print state[-1],state[1]
            imprime_caminho(map,heap_map,state)
            return True

        else:
            nextValidStates = getPossibleMoves(map,map_height,map_width,heap,heap_map,heuristic_map,state)
            for s in nextValidStates:
                add_in_heap(heap,heap_map,s)
    return False

def bfs_no_solution(state,goal):
    print "<" + str(state[0]) + "," + str(state[1]) + ",0>"
    print "<" + str(goal[0]) + "," + str(goal[1]) + ",inf>" 


def isRoot(state):
    if state[2][0] == -1 and state[2][1] == -1:
        return True
    else:
        return False

def getFather(closed_list,state):
    return closed_list[state[2]]

def out_put(path):
    print "<" + str(path[0][1][0]) + "," + str(path[0][1][1]) + "," + str(path[0][3]) + ">"
    print "<" + str(path[-1][1][0]) + "," + str(path[-1][1][1]) + "," + str(path[-1][3]) + ">\n"
    for s in path:
        print "<" + str(s[1][0]) + "," + str(s[1][1]) + "," + str(s[3]) + ">",
    print "\n"

def imprime_caminho(map,closed_list,state):
    path = []
    p_state = state
    map[state[1][0]][state[1][1]] = 'x'
    path.insert(0,[p_state[0],p_state[1],p_state[2],p_state[3]])
    while not isRoot(p_state):
        p_state = getFather(closed_list,p_state)
        map[p_state[1][0]][p_state[1][1]] = 'x'
        path.insert(0,[p_state[0],p_state[1],p_state[2],p_state[3]])
    out_put(path)
    return path
