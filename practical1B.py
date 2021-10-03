import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(1)

def draw_axis(s):
    t.setpos(0,0)
    t.shape("circle")
    t.color("blue")
    t.pensize(8)

    for i in range(4):
        t.fd(s)
        t.pu()
        t.goto(0,0)
        t.pd()
        t.lt(90)
    t.ht
draw_axis(300)

t.penup()
t.goto(-120, 50)
t.begin_fill()
t.color("red")
t.pendown()
t.circle(50)
t.penup()
t.goto(-140,10)
t.end_fill()
t.write("circle")

t.penup()
t.goto(100, 100)
t.pendown()
t.begin_fill()
t.color("lightblue")
t.circle(40, 200, 10)
t.end_fill()
t.penup()
t.goto(180,110)
t.pendown()
t.write("half circle")

t.penup()
t.setposition(130,-150)
t.pendown()
t.begin_fill()
t.color("green")
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.penup()
t.setposition(140, -160)
t.pendown()
t.write("rectangle")

t.penup()
t.setposition(-130, -170)
t.pendown()
t.begin_fill()
t.color("pink")
t.forward(90)
t.left(300)
t.forward(90)
t.left(300)
t.forward(90)
t.left(300)
t.forward(90)
t.left(300)
t.forward(90)
t.left(300)
t.end_fill()
t.penup()
t.setposition(-100,-120)
t.pendown()
t.write("hexagone")
t.penup()
t.goto(0,0)
turtle.mainloop()