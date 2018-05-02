from controller import *
import os

def search(map,map_height,map_width,closed_list,current_state,goal_state,tree_level,lim):
    minDiscovered = []
    map[current_state[0]][current_state[1]] = 3
    print current_state
    if isGoal(current_state,goal_state):
        closed_list[(current_state[0],current_state[1],current_state[2])] = current_state
        map[current_state[0]][current_state[1]] = 0
        return [current_state]
    if tree_level < lim:        
        nexStates = nextValidStates(map,map_height,map_width,closed_list,current_state)
        if len(nexStates) != 0:
            closed_list[(current_state[0],current_state[1],current_state[2])] = current_state
            for s in nexStates:
                path = search(map,map_height,map_width,closed_list,s,goal_state,tree_level+1,lim)
                if path != None:
                    minDiscovered = minPath(minDiscovered,path)
    closed_list[(current_state[0],current_state[1],current_state[2])] = current_state
    map[current_state[0]][current_state[1]] = 0
    if len(minDiscovered) == 0:
        return None
    return minDiscovered + [current_state]

def limited_search(map,map_height,map_width,initial_state,goal_state):
    i = 10
    minDiscovered = []
    while(len(minDiscovered) == 0):
        path = search(map,map_height,map_width,{},initial_state,goal_state,0,i)
        if path != None:
            minDiscovered = minPath(minDiscovered,path)
        i+= 10
    print minDiscovered

def write_map(map):
    arq = open("ids_log.txt","w")
    for line in map:
        for j in line:
            arq.write(str(j))
        arq.write("\n")

def isGoal(current_state,goal_state):
    if current_state[0] == goal_state[0] and current_state[1] == goal_state[1]:
        return True
    else:
        return False

def minPath(pathA,pathB):
    if len(pathA) == 0:
        #print pathB
        return pathB
    if len(pathA) >= len(pathB):
        #print pathB
        return pathB
    else:
        #print pathA
        return pathA