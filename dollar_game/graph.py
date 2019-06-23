import actions
from   copy import deepcopy
import display
import globals
from   math import exp, sqrt
import random
import Queue

import json

# actions generator for graph nodes

def nodeActionGen(i):
    def funcLeft(): # gives to neighbors of i one dollar
        neighbors = neighbors_of(i)
        globals.graph['vertices'][i]['value'] -= len(neighbors)
        for n in neighbors:
            globals.graph['vertices'][n]['value'] += 1
            display.transfers.append((i, n, 0))
        globals.actions.append((i, 1))

    def funcRight(): # takes from all neighbors of i one dollar
        neighbors = neighbors_of(i)
        globals.graph['vertices'][i]['value'] += len(neighbors)
        for n in neighbors:
            globals.graph['vertices'][n]['value'] -= 1
            display.transfers.append((n, i, 0))
        globals.actions.append((i, -1))

    globals.graph['vertices'][i]['action_give'] = funcLeft
    globals.graph['vertices'][i]['action_take'] = funcRight
    return funcLeft, funcRight

def optimizeGraphDisplay(graph):
    minX = min([v['pos'][0] for v in graph['vertices']])
    minY = min([v['pos'][1] for v in graph['vertices']])
    maxX = max([v['pos'][0] for v in graph['vertices']])
    maxY = max([v['pos'][1] for v in graph['vertices']])
    graph_width = maxX - minX if maxX - minX else 2
    graph_height = maxY - minY if maxY - minY else 2
    for v in graph['vertices']:
        x = int( (v['pos'][0] - minX) * (display.RightBorder - 150) / graph_width + 150 )
        y = int( (v['pos'][1] - minY) * (110 - display.BottomBorder) / graph_height + display.BottomBorder )
        v['pos'] = [x,y]

def load():
    #global graph
    with open(globals.graph_name + '.json', 'r') as stream:
        graph = json.loads( stream.read() )
    for i, v in enumerate(graph['vertices']):
        v['index'] = i
    optimizeGraphDisplay(graph)
    globals.start = graph
    globals.graph = deepcopy(graph)

def connected_components(graph):
    q = Queue.Queue()
    components = Queue.Queue()
    unseen_vertices = [v['index'] for v in graph['vertices']]
    
    while unseen_vertices != []:
        component = []
        q.put(unseen_vertices[0])
        while not q.empty():
            v = q.get()
            if v not in unseen_vertices:
                continue
            unseen_vertices.remove(v)
            component.append(v)
            for neighbor in neighbors_of_graph(v, graph):
                q.put(neighbor)
        components.put(component)
        
    return components

def generateRandom(nodes, maxEdges, max_debt = -10, strongly_winnable = True):
    graph = dict()
    graph['vertices'] = []
    graph['edges'] = []
    for i in range(nodes):
        node = dict()
        node['index'] = i
        node['pos'] = [random.randint(0, 100), random.randint(0, 100)]
        node['value'] = max_debt
        graph['vertices'].append(node)

    for v in graph['vertices']:
        # each edge can be choosed two times (from two nodes)
        edges = random.randint(1, maxEdges // 2)
        other_nodes = list(range(nodes))
        other_nodes.remove(v['index'])
        neighbors = [ random.choice(other_nodes) for _ in range(edges) ]
        graph['edges'].extend([(v['index'], n) for n in neighbors])
        
    components = connected_components(graph)
    while components.qsize() > 1:
        comp_1 = components.get()
        comp_2 = components.get()
        a = random.choice([v for v in comp_1 if len(neighbors_of_graph(i, graph))])
        b = random.choice([v for v in comp_2 if len(neighbors_of_graph(i, graph))])
        graph['edges'].append([a, b])
        components.put(comp_1 + comp_2)

    optimizeGraphDisplay(graph)

    if strongly_winnable:
        g = euler_number(graph)
        N = g - nodes * max_debt
        for _ in range(N):
            random.choice(graph['vertices'])['value'] += 1
    else:
        for v in graph['vertices']:
            v['value'] = random.randint(-5, 5)
    globals.start = deepcopy(graph)
    globals.graph = deepcopy(graph)
    display.setup_buttons()
    globals.actions = []
    display.transfers = []

###################
### Graph utils ###
###################

def euler_number(graph):
    return len(graph['edges']) - len(graph['vertices']) + 1

def balanced():
    return all([v['value'] >= 0 for v in globals.graph['vertices']])

def neighbors_of(i):
    return [ a if b == i else b for [a,b] in globals.graph['edges'] if a == i or b == i ]

def neighbors_of_graph(i, graph):
    return [ a if b == i else b for [a,b] in graph['edges'] if a == i or b == i ]

def degree_of(i):
    deg = 0
    for [a, b] in globals.graph['edges']:
        if a == i or b == i:
            deg += 1
    return deg
