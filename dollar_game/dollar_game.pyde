custom_graph = True
custom_graph_name = "graph_peterson"
random_graph_size = 15
random_graph_degree = 4

import actions
import algorithm
import display
import globals
import graph

def setup():
    size(display.WindowSizeX, display.WindowSizeY)
    frameRate(25)

    if custom_graph:
        globals.graph_name = custom_graph_name
        graph.load()
    else:
        graph.generateRandom(random_graph_size, random_graph_degree)

    display.setup_buttons()

def draw():
    clear()
    background(20)

    display.draw_actions()
    display.draw_transfers()
    display.draw_edges()
    display.draw_balanced()
    display.increment_transfer()
    for b in display.buttons:
        b.display()
    display.draw_selected_algorithm()

    if not globals.manual_mode:
        algorithm.selected_algorithm()()

def keyPressed():
    if key == 'a' or key == 'A':
        display.mode.actionLeft()
    if key == 'b':
        algorithm.select_prec()
    if key == 'n':
        algorithm.select_next()

def mouseClicked():
    if not globals.manual_mode:
        return
    for button in display.buttons:
        if button.is_mouse_inside():
            button.clicked = 5
            if mouseButton == LEFT:
                button.actionLeft()
            if mouseButton == RIGHT:
                button.actionRight()

def mouseWheel(event):
    display.actions_pos += event.getCount()
    if display.actions_pos >= len(globals.actions):
        display.actions_pos = len(globals.actions) - 1
    if display.actions_pos < 0:
        display.actions_pos = 0

targetButton = None
def mouseDragged():
    global targetButton
    if targetButton:
        if targetButton.is_mouse_inside():
            targetButton.actionDrag(targetButton)
        else:
            targetButton = None
    else:
        for button in display.buttons:
            if button.is_mouse_inside():
                targetButton = button
                button.actionDrag(button)
                break
