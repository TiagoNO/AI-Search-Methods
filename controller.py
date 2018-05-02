

def isAlreadyVisited(closed_list,state):
    if closed_list.has_key((state[0],state[1],state[2])):
        if closed_list[(state[0],state[1],state[2])][2] <= state[2]:
            return True
        else:
            closed_list[(state[0],state[1],state[2])] = state
            return False
    else:
        return False

def nextValidStates(map,map_height,map_width,closed_list,state):
    nextStates = []
    up = False
    down = False
    left = False
    right = False
    x = state[0]
    y = state[1]
    cost = state[2] + 1

    if x - 1 >= 0 and not isAlreadyVisited(closed_list,state):
        if map[x - 1][y] == 0:
            nextStates.append([x - 1,y,cost])
            up = True

    if y + 1 < map_height and not isAlreadyVisited(closed_list,state):
        if map[x + 1][y] == 0:
            nextStates.append([x + 1,y,cost])
            down = True

    if y - 1 >= 0 and not isAlreadyVisited(closed_list,state):
        if map[x][y-1] == 0:
            nextStates.append([x,y - 1,cost])
            left = True

    if y + 1 < map_width and not isAlreadyVisited(closed_list,state):
        if map[x][y+1] == 0:
            nextStates.append([x,y + 1,cost])
            right = True

    if up and right and map[x - 1][y + 1] == 0:
        nextStates.append([x - 1,y + 1,cost])

    if up and left and map[x - 1][y - 1] == 0:
        nextStates.append([x - 1,y - 1,cost])

    if down and right and map[x + 1][y + 1] == 0:
        nextStates.append([x + 1,y + 1,cost])

    if down and left and map[x + 1][y - 1] == 0:
        nextStates.append([x + 1,y - 1,cost])

    return nextStates