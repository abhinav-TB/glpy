from glpy import *

app = glpy()

@point(10)
def plotpoints():
    glColor3f(100, 468, 200)
    glVertex2f(0,0)

app.run(lambda:plotpoints())

