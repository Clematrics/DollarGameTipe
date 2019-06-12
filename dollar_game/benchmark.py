import algorithm
import display
import globals
import graph

perf = { name: { 'trials' : 0, 'successes' : 0, 'sequences_length' : [], 'minim_length' : [] } for name in algorithm.algorithms }
graph_size = 15
graph_degree = 4
number_tests = 1000
max_attempts = 1000

progress = 0

def benchmark(sz, deg, n, m = 400):
    global graph_size, graph_degree, number_tests, max_attempts
    if algorithm.selected_key() == "manual":
        return

    graph_size, graph_degree, number_tests, max_attempts = sz, deg, n, m
    globals.benchmarking = True
    perf[algorithm.selected_key()]['trials'] += number_tests
    display.mode.actionLeft()

def update():
    global progress
    if graph.balanced():
        progress += 1
        algo = algorithm.selected_key()
        perf[algo]['successes'] += 1
        perf[algo]['sequences_length'].append(len(globals.actions))
        display.minim.actionLeft()
        perf[algo]['minim_length'].append(len(globals.actions))
        graph.generateRandom(graph_size, graph_degree)
    elif len(globals.actions) > max_attempts:
        progress += 1
        graph.generateRandom(graph_size, graph_degree)
    if progress == number_tests:
        progress = 0
        globals.benchmarking = False

def export_results():
    with open('results.csv', 'w') as stream:
        s = "algorithm ; trials ; successes ; max ; min ; avg ; max minimized ; min minimized ; avg minimized\n"
        stream.write(s)

        for algo in perf.keys():
            if algo == "manual" or perf[algo]['trials'] == 0:
                continue
            s = algo + ';'
            s += str(perf[algo]['trials']) + ';'
            s += str(perf[algo]['successes']) + ';'
            s += str(max(perf[algo]['sequences_length'])) + ';'
            s += str(min(perf[algo]['sequences_length'])) + ';'
            s += str(sum(perf[algo]['sequences_length']) / len(perf[algo]['sequences_length'])) + ';'
            s += str(max(perf[algo]['minim_length'])) + ';'
            s += str(min(perf[algo]['minim_length'])) + ';'
            s += str(sum(perf[algo]['minim_length']) / len(perf[algo]['sequences_length']))
            stream.write(s + '\n')
