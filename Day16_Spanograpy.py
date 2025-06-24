import turtle

# Setup
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

# List of colors
colors = [
    "red", "blue", "green", "yellow", "orange",
    "pink", "purple", "cyan", "magenta", "white"
]

# Drawing overlapping circles with color changes
for i in range(7):
    for color in colors:
        turtle.color(color)
        turtle.circle(100)
        turtle.left(10)

# Hide the turtle at the end
turtle.hideturtle()

# Keep the window open
turtle.done()
