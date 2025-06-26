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

def draw_spirograph(size, color):
    t.color(color)
    for _ in range(72):  # 72 * 5 degrees = 360
        t.circle(size)
        t.right(5)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan']

for i in range(50):
    color = random.choice(colors)
    size = random.randint(10, 100)
    draw_spirograph(size, color)

t.hideturtle()
screen.mainloop()
