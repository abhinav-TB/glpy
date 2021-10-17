from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from typing import Callable
from functools import wraps

def plotaxes():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(0,-100)
    glVertex2f(0,100)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(100,0)
    glVertex2f(-100,0)
    glEnd()

def plotgrid():
    glColor3f(0.202, 0.202, 0.202)
    for i in range(-100,100,10):
        if i != 0:
            glBegin(GL_LINES)
            glVertex2f(i,100)
            glVertex2f(i,-100)
            glEnd()
            glBegin(GL_LINES)
            glVertex2f(100,i)
            glVertex2f(-100,i)
            glEnd()


def grid(func):
    def inner(*args,**kwargs):
        plotaxes()
        plotgrid()
        func(*args,**kwargs)
    
    return inner