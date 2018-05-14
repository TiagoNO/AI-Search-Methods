import sys
from input import inputManager
from ids import ids_search,ids_no_solution,ids_write_arq
from ucs import ucs_search,ucs_write_arq,ucs_no_solution
from bfs import bfs_calculate_heuristic,bfs_search,bfs_write_arq,bfs_no_solution
from astar import astar_search,astar_write_arq,astar_no_solution,calculate_heuristic
from heapq import *

input = inputManager(sys.argv)

if str(sys.argv[1]) == 'ids':
    found = False
    lim = 441
    while not found:
        state = [0.0,0,(input.initial_state[0],input.initial_state[1]),(-1,-1)]
        open_list = {0:state}
        map_list = {(state[1]):0}
        closed_list = {}
        found = ids_search(input.map,input.map_height,input.map_width,open_list,map_list,closed_list,input.goal_state,lim)
        lim += 30
        if lim >= input.map_height*input.map_width:
            ids_no_solution(state,input.goal_state)
            break
#    ids_write_arq("ids_log",input.map)

elif str(sys.argv[1]) == 'ucs':
#    print "Using UCS"
    state = [0.0,(input.initial_state[0],input.initial_state[1]),(-1,-1)]
    closed_list = {}
    heap = [state]
    heap_map = {}
    found = ucs_search(input.map,input.map_height,input.map_width,heap,heap_map,input.goal_state)
    if not found:
        ucs_no_solution(state,input.goal_state)
#    ucs_write_arq("ucs_log",input.map) # imprime o mapa e o caminho feito pelo agente

elif str(sys.argv[1]) == 'bfs':
    #print "Using BFS"
    heap_map = {}
    heuristic_map = {}
    heap_map = {}

    bfs_calculate_heuristic(input.map,input.map_height,input.map_width,heuristic_map,input.goal_state)

    state = [heuristic_map[(input.initial_state[0],input.initial_state[1])],(input.initial_state[0],input.initial_state[1]),(-1,-1),0.0]
    heap = [state]
    found = bfs_search(input.map,input.map_height,input.map_width,heap,heap_map,heuristic_map,input.goal_state)
    if not found:
        bfs_no_solution(input.initial_state,input.goal_state)
#    bfs_write_arq("bfs_log",input.map) # imprime o mapa e o caminho feito pelo agente

elif str(sys.argv[1]) == 'astar':
    #print "Using A*"
    heap_map = {}
    closed_list = {}

    #print heuristic_map[(input.initial_state[0],input.initial_state[1])]
    state = [calculate_heuristic(input.aStar,input.initial_state,input.goal_state),(input.initial_state[0],input.initial_state[1]),(-1,-1),0.0]
    heap = []
    heap_map = {state[1]:state}
    heappush(heap,state)
    found = astar_search(input.map,input.map_height,input.map_width,heap,heap_map,input.aStar,input.goal_state)
    if not found:
        astar_no_solution(input.initial_state,input.goal_state)
#    astar_write_arq("astar_log",input.map) # imprime o mapa e o caminho feito pelo agente
