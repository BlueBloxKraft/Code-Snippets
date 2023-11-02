from turtle import *
    
def drawTree():
    def drawTrunk():
        fillcolor("brown")
        begin_fill()
        for i in range(4):
            fd(20*abs(1 - 11*(i%2)))
            lt(90)
        end_fill()

    def drawLeaves():
        fillcolor("green")
        begin_fill()
        for i in range(6):
            circle(30, 160)
            rt(100)
        end_fill()
    
    lt(90)
    drawTrunk()
    fd(10)
    lt(130)
    drawLeaves()

lt(90)
speed(10)
drawTree()
ht()
