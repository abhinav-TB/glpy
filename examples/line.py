from glpy import *
app = glpy()

@line(4)
def plotLine(x1,x2,y1,y2):
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)


app.run(lambda: plotLine(0,50,0,50))