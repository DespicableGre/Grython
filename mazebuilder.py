# LEBRON OF CODING
import turtle as trtl

shapes = ["empty.gif", "wall.gif", "filled.gif", "other.gif"]
wn = trtl.Screen()
wn.addshape(shapes[0])
wn.addshape(shapes[1])
wn.addshape(shapes[2])
wn.addshape(shapes[3])

builder = trtl.Turtle(shapes[0])
#painter = trtl.Turtle()

builder.penup()
builder.speed(0)

# Start building

maze = [ 16 , 16 ]
startingpos = [ -(maze[0]-1)/2*16 , (maze[1]-1)/2*16 ]

# Make grid
for y in range(maze[1]):
    builder.goto(startingpos[0],startingpos[1]-16*y)
    builder.stamp()
    for x in range(maze[0] - 1):
        builder.fd(16)
        builder.stamp()

# Generate Maze



# forgot to mention that this was to know if it was centered
painter = trtl.Turtle(shapes[2])
# painter2 = trtl.Turtle(shape=wall)
# painter3 = trtl.Turtle(shape=wall)
# painter2.goto(16,16)
# painter3.goto(-16,16)


trtl.mainloop()
