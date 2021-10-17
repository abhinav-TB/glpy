import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from glpy import *
from glpy import grid
app = glpy(axis_range=(-100,100,-100,100))

@grid
def plotpoints():
    # glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(0.0,0.0)
    glEnd()
    glFlush()

@grid
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

app.run(lambda:plotLine(0,0,40,40))

