import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.bgcolor("white")
screen.title("Indian Flag")

# Create turtle
flag = turtle.Turtle()
flag.speed(0)
flag.penup()

# Constants
flag_width = 900
flag_height = 600
stripe_height = flag_height / 3

# Function to draw a filled rectangle
def draw_rectangle(color, x, y, width, height):
    flag.goto(x, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()
    flag.penup()

# Draw the 3 stripes
draw_rectangle("orange", -flag_width/2, flag_height/2, flag_width, stripe_height)
draw_rectangle("white", -flag_width/2, flag_height/2 - stripe_height, flag_width, stripe_height)
draw_rectangle("green", -flag_width/2, flag_height/2 - 2 * stripe_height, flag_width, stripe_height)

# Draw the Ashoka Chakra (navy blue)
chakra_radius = 60
flag.goto(0, 0 - chakra_radius)  # center of flag is (0, 0)
flag.setheading(0)
flag.pendown()
flag.color("navy")
flag.pensize(2)
flag.begin_fill()
flag.circle(chakra_radius)
flag.end_fill()
flag.penup()

# White circle inside the chakra (to create border effect)
flag.goto(0, -chakra_radius + 5)
flag.color("white")
flag.begin_fill()
flag.circle(chakra_radius - 5)
flag.end_fill()
flag.penup()

# Draw the 24 spokes
flag.goto(0, 0)
flag.color("navy")
flag.setheading(0)
for i in range(24):
    flag.forward(chakra_radius - 5)
    flag.pendown()
    flag.forward(5)
    flag.backward(chakra_radius)
    flag.left(15)
    flag.penup()

# Draw the central navy blue small circle
flag.goto(0, -8)
flag.pendown()
flag.begin_fill()
flag.circle(8)
flag.end_fill()
flag.penup()

# Hide turtle and finish
flag.hideturtle()
turtle.done()
