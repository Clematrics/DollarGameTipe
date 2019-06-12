import actions
import display
import globals
import graph

from random import choice

wealthy_turn = True

def debts():
    debt = False
    for v in globals.graph['vertices']:
        if v['value'] < 0:
            debt = True
            break
    return debt

def rich_vertices():
    vertices = []
    for i, v in enumerate(globals.graph['vertices']):
        if v['value'] >= 0:
            vertices.append(i)
    return vertices

def poor_vertices():
    vertices = []
    for i, v in enumerate(globals.graph['vertices']):
        if v['value'] < 0:
            vertices.append(i)
    return vertices

def algo():
    global wealthy_turn
    if not debts():
        display.mode.actionLeft()
        print("Success !")
        print(len(globals.actions))
        return

    # spread dollars

    if wealthy_turn:
        wealthies = rich_vertices()
        if len(wealthies) == 0:
            return
        wealthies = sorted(wealthies, key=lambda x: globals.graph['vertices'][x]['value'])
        # i = wealthies[-1]
        i = choice(wealthies)
        globals.graph['vertices'][i]['action_give']()
    else:
        poor = poor_vertices()
        i = choice(poor)
        globals.graph['vertices'][i]['action_take']()
        
    wealthy_turn = not wealthy_turn
