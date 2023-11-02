import turtle as t

t.speed(20)

def moveOnY(i):
    t.pu()
    t.sety(t.ycor()+i)
    t.pd()

def moveOnX(i):
    t.pu()
    t.setx(t.xcor()+i)
    t.pd()

def drawRedCircle():
    t.fillcolor("red")
    t.begin_fill()
    t.circle(200)
    t.end_fill()

# drawEye(1) draws the left eye and drawEye(-1) draws the right eye
def drawEye(i):
    t.fillcolor("white")
    t.begin_fill()
    t.fd(90)
    t.rt(150*i)
    t.fd(78)
    t.rt(90*i)
    t.fd(45)
    t.end_fill()

'''
func_a() draws a black circle and a vertical red rectangle at its middle so
it looks like two parts of a circle
'''
def func_a():
    t.fillcolor("black")
    t.begin_fill()
    t.circle(175)
    t.end_fill()

    moveOnX(-20)
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    for i in range(4):
        t.fd(40*abs(1-10*(i%2)))
        t.lt(90)
    t.end_fill()

moveOnY(-150)
drawRedCircle()
moveOnY(25)
func_a()

t.pu()
t.fd(20)
moveOnY(175)

pos=t.pos()

moveOnX(40)
t.color("white")
t.lt(30)
t.pd()
drawEye(1)

t.pu()
t.setpos(pos)
t.lt(45)
moveOnX(-40)
t.rt(40)
t.pd()
drawEye(-1)

moveOnX(-200)
print("Complete!")
t.done()
