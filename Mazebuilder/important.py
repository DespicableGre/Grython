# LEBRON OF CODING
import turtle as trtl
import random

# BUBBLE MAZE
maze = [ 5 , 5 ]

startingpos = [ -(maze[0]-1)/2*16 , (maze[1]-1)/2*16 ] # ignore this
grid = []

shapes = ["other.gif", "wall_right.gif", "wall_up.gif", "wall_left.gif", "wall_down.gif", "filled.gif"]
wn = trtl.Screen()
wn.addshape(shapes[0])
wn.addshape(shapes[1])
wn.addshape(shapes[2])
wn.addshape(shapes[3])
wn.addshape(shapes[4])
wn.addshape(shapes[5])


builder = trtl.Turtle(shapes[0])
builder.penup()
builder.speed(0)


###
class cell:
    left = False
    up = False
    right = False
    bottom = False
def buildWalls(gridIndex):
    if grid[gridIndex].left == True:
        builder.shape(shapes[3])
        builder.stamp()
    if grid[gridIndex].up == True:
        builder.shape(shapes[2])
        builder.stamp()
    if grid[gridIndex].right == True:
        builder.shape(shapes[1])
        builder.stamp()
    if grid[gridIndex].bottom == True:
        builder.shape(shapes[4])
        builder.stamp()
def randomWalls(gridIndex):
    grid[gridIndex].left = bool(random.getrandbits(1))
    grid[gridIndex].up = bool(random.getrandbits(1))
    grid[gridIndex].right = bool(random.getrandbits(1))
    grid[gridIndex].bottom = bool(random.getrandbits(1))
###


# Start building

for width in range(maze[0] * maze[1]):
    grid.append(cell)

# Make grid
builder.fillcolor("black")
builder.goto(startingpos[0] - 8, startingpos[1] + 8)
builder.begin_fill()
builder.goto(startingpos[0] + 16 * maze[0] - 16 - 8, startingpos[1]+8)
builder.goto(startingpos[0] + 16 * maze[0] - 16 - 8, startingpos[1] - 16 * maze[1] + 8)
builder.goto(startingpos[0] - 8, startingpos[1] - 16 * maze[1] + 8)
builder.end_fill()



# Make walls
builder.shape(shapes[1])

for y in range(maze[1]):
    builder.goto(startingpos[0],startingpos[1]-16*y)
    builder.bk(16)
    for x in range(maze[0] - 1):
        builder.fd(16)
        randomWalls(y * maze[1] - (maze[0] - x) - 1)
        buildWalls(y * maze[1] - (maze[0] - x) - 1)


# Screensaver

arrow = trtl.Turtle(shape="arrow")
arrow.color("lime")
arrow.speed(0)

while(True):
    goWhere = random.randrange(0,4,1)
    if (goWhere == 0):
        arrow.left(3)
        arrow.forward(1)
    if (goWhere == 1):
        arrow.right(3)
        arrow.forward(1)
    if (goWhere == 2):
        arrow.forward(1)
    if (goWhere == 3):
        arrow.right(45)
        arrow.forward(1)
    if (goWhere == 4):
        arrow.left(45)
        arrow.forward(1)


trtl.mainloop()