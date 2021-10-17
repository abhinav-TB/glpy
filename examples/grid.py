from glpy import *

app = glpy()

@grid
@point(20)
def plotgrid():
    glVertex2f(0, 0)


app.run(lambda: plotgrid())
