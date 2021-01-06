from turtle import *
t = Turtle()
t.screen.setup(800, 800)
t.shape("turtle")

def sq_cr(side):

    for i in range(4):
        t.left(270)
        t.fd(side)
    t.left(180)
    t.circle(side / 2, 360)

sq_cr(250)
t.screen.exitonclick()
t.screen.mainloop()
