import actions
import algorithm
import globals
import graph
import minimization

# Window parameters

Border = 50
WindowSizeX = 2100
WindowSizeY = 1300
LeftBorder = Border
RightBorder = WindowSizeX - Border
TopBorder = Border
BottomBorder = WindowSizeY - Border


# Drawing context
actions_pos = 0
transfers = [] # time between 0 and 10
buttons = []
mode = None
mode_description = ['manual']
reset = None
minim = None

# classes

class rectButton:
    def __init__(self, luCornerX, luCornerY, rdCornerX, rdCornerY,
                 actionLeft = None, actionRight = None, actionDrag = None,
                 linkedData = None):
        self.luCornerX = luCornerX
        self.luCornerY = luCornerY
        self.rdCornerX = rdCornerX
        self.rdCornerY = rdCornerY
        self.actionLeft = actionLeft if actionLeft else actions.nullAction
        self.actionRight = actionRight if actionRight else actions.nullAction
        self.actionDrag = actionDrag if actionDrag else actions.nullAction
        self.linkedData = linkedData
        self.clicked = False
        
    def display(self):
        strokeWeight(4)
        stroke(128)
        fill(128 if self.clicked else 25)
        rectMode(CORNERS)
        rect(self.luCornerX, self.luCornerY, self.rdCornerX, self.rdCornerY)
        fill(200)
        textAlign(CENTER, CENTER)
        textSize(30)
        text(self.linkedData[0], (self.luCornerX + self.rdCornerX) / 2, (self.luCornerY + self.rdCornerY) / 2)
        self.clicked = max(self.clicked - 1, 0)
            
    def is_mouse_inside(self):
        return self.luCornerX < mouseX and self.luCornerY < mouseY and mouseX < self.rdCornerX and mouseY < self.rdCornerY

class vertexButton:
    def __init__(self, vertex, radius, 
                 actionLeft = None, actionRight = None, actionDrag = None):
        self.vertex = vertex
        self.radius = radius
        self.actionLeft = actionLeft if actionLeft else actions.nullAction
        self.actionRight = actionRight if actionRight else actions.nullAction
        self.actionDrag = actionDrag if actionDrag else actions.nullAction
        
    def display(self):
        fill(128)
        ellipse(self.vertex['pos'][0], self.vertex['pos'][1], 30, 30)
        fill(200)
        textSize(20)
        textAlign(CENTER, CENTER)
        text(str(self.vertex['value']), self.vertex['pos'][0], self.vertex['pos'][1])
        fill(200, 20, 20)
        textSize(17)
        textAlign(CENTER, TOP)
        text(str(self.vertex['index']), self.vertex['pos'][0], self.vertex['pos'][1] - 30)
            
    def is_mouse_inside(self):
        return sqrt((pmouseX - self.vertex['pos'][0])**2 + (pmouseY - self.vertex['pos'][1])**2) < self.radius

# setup

def setup_buttons():
    global mode, reset, minim, buttons
    buttons = []

    mode = rectButton(0, 0, WindowSizeX / 4, 50,
                      actionLeft = actions.changeMode,
                      linkedData = mode_description)
    buttons.append(mode)
    reset = rectButton(WindowSizeX / 4, 0, 2 * WindowSizeX / 4, 50,
                       actionLeft = actions.reset,
                       linkedData = ["reset"])
    buttons.append(reset)
    saveB = rectButton(2 * WindowSizeX / 4, 0, 3 * WindowSizeX / 4, 50,
                       actionLeft = actions.saveGraph,
                       linkedData = ["save"])
    buttons.append(saveB)
    minim = rectButton(3 * WindowSizeX / 4, 0, 4 * WindowSizeX / 4, 50,
                       actionLeft = minimization.minimize,
                       linkedData = ["minimize"])
    buttons.append(minim)
    
    for i, v in enumerate(globals.graph['vertices']):
        left, right = graph.nodeActionGen(i)
        button = vertexButton(v, 30, actionLeft = left, actionRight = right, actionDrag = actions.drag)
        buttons.append(button)

# draw methods

def increment_transfer():
    global transfers
    new_transfers = []
    for c in transfers:
        i, j, t = c
        if t < 10:
            new_transfers.append((i, j, t + 1))
    transfers = new_transfers

def draw_selected_algorithm():
    fill(200)
    textAlign(CENTER, CENTER)
    textSize(20)
    text(algorithm.selected_key(), WindowSizeX / 16, 50 / 2)

# each action is a button of height 40 and width 100
def draw_actions():
    rectMode(CORNERS)
    strokeWeight(4)
    stroke(128)
    textAlign(CENTER, CENTER)
    try:
        actions_to_draw = globals.actions[actions_pos: actions_pos + 31]
    except:
        actions_to_draw = globals.actions[actions_pos:]
    for i, a in enumerate(actions_to_draw):
        v, move = a
        move_string = u'<->' if move > 0 else u'>-<'
        fill(25)
        rect(0, i * 40 + 60, 100, i * 40 + 100)
        textSize(20)
        fill(200)
        text(move_string, 30, i * 40 + 80)
        textSize(30)
        fill(200, 20, 20)
        text(str(v), 70, i * 40 + 80)

    fill(128)
    rect(0, 30 * 40 + 60, 100, 30 * 40 + 100)
    fill(255)
    text(str(len(globals.actions)), 50, 30 * 40 + 80)
    
    
def draw_edges():
    strokeWeight(4)
    stroke(128)
    for e in globals.graph['edges']:
        i, j = tuple(e)
        ix, iy = tuple(globals.graph['vertices'][i]['pos'])
        jx, jy = tuple(globals.graph['vertices'][j]['pos'])
        line(ix, iy, jx, jy)
    
def draw_transfers():
    fill(255, 128, 0)
    ellipseMode(RADIUS)
    for (i, j, t) in transfers:
        ix, iy = tuple(globals.graph['vertices'][i]['pos'])
        jx, jy = tuple(globals.graph['vertices'][j]['pos'])
        x = (jx - ix) * t / 10 + ix
        y = (jy - iy) * t / 10 + iy
        ellipse(x, y, 10, 10)
        
def draw_balanced():
    if graph.balanced():
        fill(0, 255, 0)
    else:
        fill(255, 0, 0)
    
    strokeWeight(0)
    rectMode(CORNERS)
    rect(WindowSizeX - 50, WindowSizeY - 50, WindowSizeX, WindowSizeY)
    
def draw_benchmarking():
    if not globals.benchmarking:
        return
    textSize(50)
    textAlign(CENTER, CENTER)
    text("benchmarking...", WindowSizeX / 2, WindowSizeY / Z)
