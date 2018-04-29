from sets import Set


def getValidActions(map,map_height,map_width,position):
    actions = {}

    if position[0] - 1 >= 0:
        if map[position[0]-1][position[1]] == '.':
            actions['w'] = 1 # can go up

    if position[0] + 1 < map_height:
        if map[position[0]+1][position[1]] == '.':
            actions['s'] = 1 # can go down

    if position[1] + 1 < map_width:
        if map[position[0]][position[1]+1] == '.':
            actions['d'] = 1 # can go right
    
    if position[0] - 1 >= 0:
        if map[position[0]][position[1]-1] == '.':
            actions['a'] = 1 # can go left

    if actions.has_key('w') & actions.has_key('d'):
        actions['e'] = 1 # can go upper right diagonal
    
    if actions.has_key('w') & actions.has_key('a'):
        actions['q'] = 1 # can go upper left diagonal
    
    if actions.has_key('s') & actions.has_key('d'):
        actions['x'] = 1 # can go lower right diagonal
    
    if actions.has_key('w') & actions.has_key('d'):
        actions['z'] = 1 # can go lower left diagonal

    return actions