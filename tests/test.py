import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from glpy import *
app = glpy(bgcolor=(0,1,1,1.0),axis_range = (0,10,0,10))


@point(10)
def plotpoints():
    glColor3f(100, 468, 200) # setting the color
    glVertex2f(0,0)# seting the verte


@point(10)
def plotLine(x1,y1,x2,y2):
    m = 2 * (y2 - y1)
    pk = m - (x2 - x1)
    y=y1 

    glColor3f(1.0,0.0,0.0) 

    for x in range(x1,x2+1):
        glVertex2f(x,y)
        pk =pk + m
        if (pk>= 0):
            y=y+1
            pk =pk - 2 * (x2 - x1)

app.run(lambda:plotpoints())

