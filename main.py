import sys
from input import inputManager
from IDS import *

input = inputManager(sys.argv)
sys.setrecursionlimit(99999999)

if str(sys.argv[1]) == 'ids':
    print "Using IDS"
    found = False
    i = 0
    while not found:
        map_copy = input.map
        state = input.initial_state + [0,[-1,-1]]
        open_list = {0:state}
        map_list = {(state[0],state[1]):0}
        closed_list = {}
        found = search(map_copy,input.map_height,input.map_width,open_list,map_list,closed_list,input.goal_state,i)
        i += 1
        #write_arq("ids_log_0" + str(i) + ".txt",map_copy)
        if i >= input.map_height*input.map_width:
            break
elif str(sys.argv[1]) == 'ucs':
    print "Using UCS"
elif str(sys.argv[1]) == 'bfs':
    print "Using BFS"
