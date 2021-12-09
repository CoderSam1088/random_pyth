import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

#Your code goes here. When using a command, put alex. in front of all commands
#For example alex.circle(10) will make a circle with a radius of 10.


# Makes the program MUCH faster because i'm impatient
alex.speed(0)

# Makes alex not draw, and gets him into position
def in_position():
    alex.penup()
    #this value (default -350, -350) can be changed to determine where the bottom left of the first box should start.
    alex.setposition (-300, -300)
    alex.pendown()

# Draws the checkerboard
def draw_checkerboard_black():
    #this number (default 5) is how many squares you want on the Y axis.
    for i in range (10):
        #this number (default 5) is how many squares you want on the X axis.
        for i in range (10):
            #do not change this line. this number (4) draws the 4 sides of a square
            alex.begin_fill()
            for i in range (4):
                alex.pendown()
                alex.color("black")
                alex.forward(50)
                alex.left(90)
                alex.end_fill()
                alex.penup()
                alex.forward(50)
                alex.backward(500)
                alex.left(90)
                alex.forward(50)
                alex.right(90)

def draw_checkerboard_colored():
    alex.forward(50)
    #this number (default 5) is how many squares you want on the Y axis.
    for i in range (5):
        #do not change this line. this number (4) draws the 4 sides of a square
        alex.begin_fill()
        for i in range (4):
            alex.pendown()
            alex.color("red")
            alex.forward(50)
            alex.left(90)
            alex.end_fill()
            alex.penup()
            alex.forward(100)
            alex.backward(550)
            alex.left(90)
            alex.forward(50)
            alex.right(90)
for i in range (5):
    #do not change this line. this number (4) draws the 4 sides of a square
    alex.begin_fill()
    for i in range (4):
        alex.pendown()
        alex.color("red")
        alex.forward(50)
        alex.left(90)
        alex.end_fill()
        alex.penup()
        alex.forward(100)
        alex.backward(500)
        alex.left(90)
        alex.forward(50)
        alex.right(90)


#these 2 functions do eveything listed above
in_position()
draw_checkerboard_black()
in_position()
for i in range(5):
    draw_checkerboard_colored()


#Stop your code here

#Makes the drawing window exit on a mouse click
wn.exitonclick()
