import turtle
import math

def draw_spirograph(R, r, d):
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.penup()

    # Start position
    theta = 0
    theta_rad = math.radians(theta)
    x = (R - r) * math.cos(theta_rad) + d * math.cos((R - r) / r * theta_rad)
    y = (R - r) * math.sin(theta_rad) - d * math.sin((R - r) / r * theta_rad)
    t.goto(x, y)
    t.pendown()

    for theta in range(1, 720):
        theta_rad = math.radians(theta)
        x = (R - r) * math.cos(theta_rad) + d * math.cos((R - r) / r * theta_rad)
        y = (R - r) * math.sin(theta_rad) - d * math.sin((R - r) / r * theta_rad)
        t.goto(x, y)

    t.hideturtle()

draw_spirograph(100, 20, 50)
turtle.done()
