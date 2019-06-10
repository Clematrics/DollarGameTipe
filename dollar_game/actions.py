from copy import copy
import display
from   copy import deepcopy
import globals
import json
import os

def nullAction(*args, **kwargs):
    pass

def changeMode():
    globals.manual_mode = not globals.manual_mode
    if globals.manual_mode:
        display.mode_description[0] = 'manual'
    else:
        display.mode_description[0] = 'automatic'
        
def reset():
    globals.actions = []
    for v in globals.graph['vertices']:
        v['value'] = copy(globals.start['vertices'][v['index']]['value'])

def saveGraph():
    number = 0
    while( os.path.isfile("saved_graph_" + str(number) + '.json')):
        number += 1
    temp_graph = deepcopy(globals.graph)
    for v in temp_graph['vertices']:
        del v['action_give']
        del v['action_take']
    with open("saved_graph_" + str(number) + '.json', 'w') as stream:
        json.dump( temp_graph, stream )

def drag(button):
    if isinstance(button, display.vertexButton):
        button.vertex['pos'] = [mouseX, mouseY]
    elif isinstance(button, display.rectButton):
        button_width = abs( button.rdCornerX - button.luCornerX )
        button_height = abs( button.rdCornerY - button.luCornerY )
        button.luCornerX = mouseX - button_width 
        button.luCornerY = mouseY - button_height
        button.rdCornerX = mouseX + button_width
        button.rdCornerY = mouseY + button_height
