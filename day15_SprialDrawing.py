import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')

# Set up turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Function to draw a spirograph
def draw_spirograph(size, color):
    t.color(color)
    for _ in range(72):  # 72 * 5 degrees = 360 degrees
        t.circle(size)
        t.right(5)

# Color palette
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan']

# Draw multiple spirographs
for i in range(50):
    color = random.choice(colors)
    size = random.randint(10, 100)
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))  # Move to random position
    t.pendown()
    draw_spirograph(size, color)

# Keep the window open
screen.mainloop()
