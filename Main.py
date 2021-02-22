from State import State
from GameMap import GameMap
from BFSearch import BFSearch
from IDSearch import IDSearch
from UCSearch import UCSearch
from AStar import AStar
from HeuristicMetric import *

import argparse
import sys

use_gui = True

UCS_type = "UCS"
BFS_type = "BFS"
Astar_type = "Astar"
IDS_type = "IDS"

def initializeGUI():
    from GUI import GUI
    return GUI((1920, 1080), list(start.coord), list(goal.coord))

def initializeGameMap(map_file):
    return GameMap(map_file)

def checkState(start, goal_state):
    if(game_map.getTile(start.coord) == '@'):
        print("Invalid initial start!!")
        exit()
    
    if(game_map.getTile(goal.coord) == '@'):
        print("Invalid goal!!")
        exit()

def initializeMethod(method_type):
    if(method_type == UCS_type):
        return UCSearch(start, goal)
    elif(method_type == BFS_type):
        return BFSearch(start, goal)
    elif(method_type == Astar_type):
        return AStar(start, goal, OctileDist(), 4, 4)
    elif(method_type == IDS_type):
        return IDSearch(start, goal, 50)
    else:
        print("Method not recognized...")
        exit()

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", help="Wich method to use", type=str, default=UCS_type, choices=[UCS_type, BFS_type, Astar_type, IDS_type])
    parser.add_argument("--map", help="Directory of the game map", type=str, required=True)
    parser.add_argument("--gui", help="Use graphic visualization", type=bool, default=False)
    return parser.parse_args()

args = parseArgs()
game_map = initializeGameMap(args.map)

start = State((0, 0), 0, 0, None)
goal = State((26, 15), 0, 0, None)

use_gui = args.gui
if(use_gui):
    gui = initializeGUI()

checkState(start, goal)
method = initializeMethod(args.method)

while True:
    finished = method.foundSolution()
    if(not method.foundSolution()):
        method.step(game_map)
    finished = (finished and method.foundSolution())

    if(use_gui):
        gui.update(game_map, method.open_list, method.closed_list.keys(), method.best_path)

    if(finished):
        break