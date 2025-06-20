import turtle 

emo = turtle.Turtle() 

# Draw face
emo.up() 
emo.goto(0, -100) 
emo.down() 
emo.begin_fill() 
emo.fillcolor('yellow') 
emo.circle(100) 
emo.end_fill() 

# Draw mouth (a smiling arc)
emo.up() 
emo.goto(-67, -40) 
emo.setheading(-60) 
emo.width(5) 
emo.down() 
emo.circle(80, 120)  # Arc for the smile

# Draw eyes
emo.fillcolor("black") 
for i in range(-35, 105, 70):  # i = -35, 35
    emo.up() 
    emo.goto(i, 35) 
    emo.setheading(0) 
    emo.down() 
    emo.begin_fill() 
    emo.circle(10) 
    emo.end_fill() 

# Keep the window open
emo.penup() 
emo.goto(0, -150) 
turtle.mainloop()
