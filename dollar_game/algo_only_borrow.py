import actions
import display
import globals
import graph
import random

def debts():
    debt = False
    for v in globals.graph['vertices']:
        if v['value'] < 0:
            debt = True
            break
    return debt

def poor_vertices():
    vertices = []
    for i, v in enumerate(globals.graph['vertices']):
        if v['value'] < 0:
            vertices.append(i)
    return vertices

def algo():
    if not debts():
        display.mode.actionLeft()
        print("Success !")
        print(len(globals.actions))
        return

    poor = poor_vertices()
    # poor = sorted(poor, key=lambda i: globals.graph['vertices'][i]['value'])
    i = random.choice(poor)
    globals.graph['vertices'][i]['action_take']()
