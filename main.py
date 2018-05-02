import sys
from input import inputManager
from IDS import *

input = inputManager(sys.argv)
#ids = ids(input.map_height,input.map_width,input.initial_state,input.goal_state)
sys.setrecursionlimit(99999999)

if str(sys.argv[1]) == 'ids':
    print "Using IDS"
    #a = input.initial_state + [0]
    #ids.search(input.map,1,[])
    limited_search(input.map,input.map_height,input.map_width,input.initial_state + [0],input.goal_state)
    write_map(input.map)
elif str(sys.argv[1]) == 'ucs':
    print "Using UCS"
elif str(sys.argv[1]) == 'bfs':
    print "Using BFS"
