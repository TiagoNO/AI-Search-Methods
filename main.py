import sys
from input import inputManager
from ids import ids_search,ids_no_solution
from ucs import ucs_search,ucs_write_arq,ucs_no_solution
from bfs import bfs_calculate_heuristic,bfs_search,bfs_write_arq,bfs_no_solution
from astar import astar_calculate_heuristic,astar_search,astar_write_arq,astar_no_solution
from heapq import *

input = inputManager(sys.argv)

if str(sys.argv[1]) == 'ids':
    found = False
    lim = 1
    while not found:
        #map_copy = input.map
        state = [0.0,0,(input.initial_state[0],input.initial_state[1]),[-1,-1]]
        open_list = {0:state}
        map_list = {(state[1]):0}
        closed_list = {}
        found = ids_search(input.map,input.map_height,input.map_width,open_list,map_list,closed_list,input.goal_state,lim)
        lim += 1
        if lim >= input.map_height*input.map_width:
            ids_no_solution(state,input.goal_state)
            break

elif str(sys.argv[1]) == 'ucs':
#    print "Using UCS"
    state = [0.0,(input.initial_state[0],input.initial_state[1]),(-1,-1)]
    closed_list = {}
    heap = [state]
    heap_map = {}
    found = ucs_search(input.map,input.map_height,input.map_width,heap,heap_map,input.goal_state)
    if not found:
        ucs_no_solution(state,input.goal_state)
#    j = 0
#    for i in [[201, 207, 0] ,[200, 207, 1] ,[199, 207, 2] ,[198, 207, 3] ,[197, 207, 4] ,[196, 207, 5] ,[195, 207, 6] ,[194, 207, 7] ,[193, 207, 8] ,[192, 207, 9] ,[191, 207, 10] ,[190, 207, 11] ,[189, 207, 12] ,[188, 207, 13] ,[187, 207, 14] ,[186, 207, 15] ,[185, 207, 16] ,[184, 207, 17] ,[183, 207, 18] ,[182, 207, 19] ,[181, 207, 20] ,[180, 207, 21] ,[179, 207, 22] ,[178, 207, 23] ,[177, 207, 24] ,[176, 207, 25] ,[175, 207, 26] ,[174, 207, 27] ,[173, 207, 28] ,[172, 207, 29] ,[171, 207, 30] ,[170, 207, 31] ,[169, 207, 32] ,[168, 207, 33] ,[167, 207, 34] ,[166, 207, 35] ,[165, 207, 36] ,[164, 207, 37] ,[163, 207, 38] ,[162, 207, 39] ,[161, 207, 40] ,[160, 206, 41.5] ,[159, 205, 43] ,[158, 204, 44.5] ,[157, 203, 46] ,[156, 202, 47.5] ,[155, 201, 49] ,[154, 200, 50.5] ,[153, 199, 52] ,[152, 198, 53.5] ,[151, 197, 55] ,[150, 196, 56.5] ,[149, 195, 58] ,[148, 194, 59.5] ,[147, 193, 61] ,[146, 192, 62.5] ,[145, 191, 64] ,[144, 190, 65.5] ,[143, 189, 67] ,[142, 188, 68.5] ,[141, 187, 70] ,[140, 186, 71.5] ,[139, 185, 73] ,[138, 184, 74.5] ,[137, 183, 76] ,[136, 182, 77.5] ,[135, 181, 79] ,[134, 180, 80.5] ,[133, 179, 82] ,[132, 178, 83.5] ,[131, 177, 85] ,[130, 176, 86.5] ,[129, 175, 88] ,[128, 174, 89.5] ,[127, 173, 91] ,[126, 172, 92.5] ,[125, 171, 94] ,[124, 170, 95.5] ,[123, 169, 97] ,[122, 168, 98.5] ,[121, 167, 100] ,[120, 166, 101.5] ,[119, 166, 102.5] ,[118, 166, 103.5] ,[117, 166, 104.5] ,[116, 166, 105.5] ,[115, 166, 106.5] ,[114, 166, 107.5] ,[113, 166, 108.5] ,[112, 166, 109.5] ,[111, 166, 110.5] ,[110, 166, 111.5] ,[109, 166, 112.5] ,[108, 166, 113.5] ,[107, 166, 114.5] ,[106, 166, 115.5] ,[105, 166, 116.5] ,[104, 166, 117.5] ,[103, 166, 118.5] ,[102, 166, 119.5] ,[101, 166, 120.5] ,[100, 166, 121.5] ,[99, 166, 122.5] ,[98, 166, 123.5] ,[97, 166, 124.5] ,[96, 166, 125.5] ,[95, 166, 126.5] ,[94, 166, 127.5] ,[93, 166, 128.5] ,[92, 166, 129.5] ,[91, 166, 130.5] ,[90, 166, 131.5] ,[89, 166, 132.5] ,[88, 166, 133.5] ,[87, 166, 134.5] ,[86, 166, 135.5] ,[85, 166, 136.5] ,[84, 166, 137.5]]:
#        input.map[i[0]][i[1]] = 4
    #ucs_write_arq("ucs_log",input.map) # imprime o mapa e o caminho feito pelo agente

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
    #bfs_write_arq("bfs_log",input.map) # imprime o mapa e o caminho feito pelo agente

elif str(sys.argv[1]) == 'astar':
    #print "Using A*"
    heap_map = {}
    heuristic_map = {}
    heap_map = {}

    astar_calculate_heuristic(input.map,input.map_height,input.map_width,heuristic_map,input.aStar,input.goal_state)
    #print heuristic_map[(input.initial_state[0],input.initial_state[1])]
    state = [heuristic_map[(input.initial_state[0],input.initial_state[1])],(input.initial_state[0],input.initial_state[1]),(-1,-1),0.0]
    heap = []
    heappush(heap,state)
#    print heap
    found = astar_search(input.map,input.map_height,input.map_width,heap,heap_map,heuristic_map,input.goal_state)
    if not found:
        astar_no_solution(input.initial_state,input.goal_state)
    astar_write_arq("astar_log",input.map) # imprime o mapa e o caminho feito pelo agente
