# -*- coding: utf-8 -*-
import actions

import algo_alternate
import algo_only_borrow
import algo_only_give
import algo_naive

algorithms = {
    "": (lambda: None),
    "naive": algo_naive.algo,
    "only borrow": algo_only_borrow.algo,
    "only_give": algo_only_give.algo,
    "alternate": algo_alternate.algo
}

selected = 0

def select_prec():
    global selected
    selected -= 1
    selected = max(selected, 0)
    
def select_next():
    global selected
    selected += 1
    selected = min(selected, len(algorithms.keys()) - 1)

def selected_key():
    return list(algorithms.keys())[selected]

def selected_algorithm():
    return algorithms[selected_key()]
