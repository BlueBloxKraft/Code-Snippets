import turtle as t

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

#not really a semi-circle
def drawBlackSemiCircle():
    t.fillcolor("black")
    t.begin_fill()
    t.circle(180, 160)
    t.end_fill()

def drawBlackSemiCircles():
    t.lt(10)
    drawBlackSemiCircle()
    t.lt(10)
    moveOnX(-40)
    t.lt(10)
    drawBlackSemiCircle()

def drawLeftEye():
    t.fillcolor("white")
    t.begin_fill()
    t.fd(90)
    t.rt(150)
    t.fd(78)
    t.rt(90)
    t.fd(45)
    t.end_fill()

def drawRightEye():
    t.fillcolor("white")
    t.begin_fill()
    t.fd(90)
    t.lt(150)
    t.fd(78)
    t.lt(90)
    t.fd(45)
    t.end_fill()

moveOnY(-120)
drawRedCircle()
moveOnY(22.5)
moveOnX(22.5)
drawBlackSemiCircles()

t.pu()
t.home()
moveOnY(120)
pos=t.pos()
moveOnX(40)
t.color("white")
t.lt(30)
t.pd()
drawLeftEye()

t.pu()
t.setpos(pos)
t.lt(45)
moveOnX(-40)
t.rt(40)
t.pd()
drawRightEye()

moveOnX(-200)
t.done()
print("Complete!")
