import turtle
import random

turtle.delay(0)
t = turtle.Turtle()
x =80






def lupen():
    for i in range(8):
        t.pensize(1)
        t.pd()
        farba = random.choice(("red", "blue", "pink", "orange","yellow","magenta"))
        t.fillcolor(farba)
        t.begin_fill()
        t.circle(x, 80)
        t.rt(-100)
        t.circle(x, 80)
        t.rt(35)
        t.end_fill()

def stonka():
    t.pd()
    t.pensize(5)
    t.rt(90)
    t.fd(x*2)



def list():
    t.pensize(2)
    t.fillcolor("green")
    t.begin_fill()
    t.pd()
    t.rt(180)
    t.fd(50)
    t.circle(x,50)
    t.rt(-130)
    t.circle(x, 50)
    t.end_fill()

for u in range(3):
    for i in range(5):
        t.setheading(0)
        t.pu()
        t.setpos(random.randint(-400, 400),
                 random.randint(-400, 400))
        t.pd()
        lupen()
        stonka()
        list()
    x-=20




turtle.mainloop()



