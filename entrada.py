import sys

def get_input(argv):
    map = []
    map_height = int()
    map_width = int()
    map_name = str()
    initial_state = []
    final_state = []

    if sys.argv[1] == '-a*':
        map_name = str(argv[2])
        initial_state = str(argv[3])
        final_state = str(argv[4])
        heuristic = int(argv[5])
    else:
        map_name = str(argv[1])
        initial_state.append(int(argv[2]))
        initial_state.append(int(argv[3]))
        final_state.append(int(argv[4]))
        final_state.append(int(argv[5]))

    #print initial_state,final_state

    arq = open('maps/'+map_name,'r')
    map_type = arq.readline()
    map_height = int(arq.readline().split()[1])
    map_width = int(arq.readline().split()[1])
    map_name1 = arq.readline()

    for line in arq.readlines():
        map.append(line)
        
    return map,map_name,map_height,map_width,initial_state,final_state
