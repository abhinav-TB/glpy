import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from glpy import *

app = glpy()

@grid
@point(20)
def plotgrid():
    glVertex2f(0, 0)


app.run(lambda: plotgrid())