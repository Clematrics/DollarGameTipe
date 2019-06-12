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

def rich_vertices():
    vertices = []
    for i, v in enumerate(globals.graph['vertices']):
        if v['value'] >= 0:
            vertices.append(i)
    return vertices

def algo():
    if not debts():
        display.mode.actionLeft()
        print("Success !")
        print(len(globals.actions))
        return

    # spread wealth

    wealthies = rich_vertices()
    if len(wealthies):
        wealthies = sorted(wealthies, key=lambda i: globals.graph['vertices'][i]['value'])
        # i = wealthies[0]
        i = random.choice(wealthies)
        globals.graph['vertices'][i]['action_give']()
