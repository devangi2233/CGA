#scaling in 2D 
import turtle
import numpy as np

ab = turtle.Turtle()
ab.setposition(0,0)
ab.pd()
ab.pu()
ab.setposition(30,60)
ab.pd()
ab.write("original object")
x = np.array([[0,0], [40,50]])
y = np.array([[3,0], [0,1]])
result = np.array([[0,0], [0,0]])

result = x.dot(y)
for r in result:
    print(r)

def Scaling(result):
    ab.pu()
    ab.setposition(0,0)
    ab.pd()
    for point in result:
        ab.goto(point[0], point[1])

Scaling(result)
ab.pu()
ab.setposition(60,20)
ab.pd()
ab.write("scale object")

turtle.mainloop()