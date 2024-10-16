import turtle as trtl

empty = "empty.gif"
wall = "wall.gif"
filled = "filled.gif"
other = "other.gif"

wn = trtl.Screen()

wn.addshape(empty)
wn.addshape(wall)
wn.addshape(filled)
wn.addshape(other)

builder = trtl.Turtle(shape=empty)
#painter = trtl.Turtle()

builder.penup()
builder.speed(1)

# Start building

maze = [ 16 , 16 ]

startingpos = [ 0 , 0 ]

if maze[0] % 2 != 0:
    startingpos[0] = (maze[0] - 1) / 2
else:
    startingpos[0] = (maze[0] / 2) - .5
if maze[1] % 2 != 0:
    startingpos[1] = (maze[1] - 1) / 2
else:
    startingpos[1] = (maze[1] / 2) - .5

startingpos = [ -startingpos[0] * 16, startingpos[1] * 16 ]
builder.goto(startingpos)
for y in range(maze[1]):
    builder.setheading(0)
    for x in range(maze[0]-1):
        builder.stamp()
        builder.forward(16)
        builder.stamp()
    builder.goto(startingpos[0], (y - .5) * 16)



painter = trtl.Turtle(shape=filled)
painter2 = trtl.Turtle(shape=wall)
painter3 = trtl.Turtle(shape=wall)
painter2.goto(16,16)
painter3.goto(-16,16)


trtl.mainloop()
