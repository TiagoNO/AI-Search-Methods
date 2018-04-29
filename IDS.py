from controller import getValidActions


def IDS(map,map_height,map_width,state,final_state):
    actions = getValidActions(map,map_height,map_width,state)
    
