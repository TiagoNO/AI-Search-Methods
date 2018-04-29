import sys
from entrada import get_input
from IDS import IDS


argv = sys.argv
map,map_name,map_height,map_width,initial_state,final_state = get_input(argv)
IDS(map,map_height,map_width,initial_state,final_state)