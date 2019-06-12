import globals

def minimize():
    sz = len(globals.graph['vertices'])
    seq = [0] * sz
    for v, move in globals.actions:
        seq[v] += move
    # print(seq, sum([abs(e) for e in seq]))

    while len([e for e in seq if e > 0]) > sz / 2:
        seq = [e - 1 for e in seq]
        # print(seq, sum([abs(e) for e in seq]))

    while len([e for e in seq if e < 0]) > sz / 2:
        seq = [e + 1 for e in seq]
        # print(seq, sum([abs(e) for e in seq]))
        
    actions = []
    for i, v in enumerate(seq):
        for _ in range(abs(v)):
            actions.append( (i, (-1 if v < 0 else 1)) )
    globals.actions = actions
