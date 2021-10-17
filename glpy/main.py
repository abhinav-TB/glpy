from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from typing import Callable
from functools import wraps


class glpy:
    """Main class to initialize OpenGL and Glut functions
    """

    def __init__(self, **kwargs):
        """initialize the class with the following parameters
        Keyword arguments:
        mode -- diplay mode (default GLUT_DOUBLE | GLUT_RGB)
        size -- window size (default (500, 500))
        position -- window position (default (0, 0))
        title -- window title (default "glpy")
        color -- background color (default (0.0, 0.0, 0.0))
        range -- window range (default (-1.0, 1.0, -1.0, 1.0))
        """
        self.mode = kwargs["mode"] if "mode" in kwargs else GLUT_RGBA
        self.size = kwargs["size"] if "size" in kwargs else (500, 500)
        self.position = kwargs["position"] if "position" in kwargs else (0, 0)
        self.title = kwargs["title"]if "title" in kwargs else "new title"
        self.color = kwargs["bgcolor"] if "bgcolor" in kwargs else (0, 0, 0, 1.0)
        self.range = kwargs["axis_range"] if "axis_range" in kwargs else (-100, 100,-100, 100)

    def run(self, cb: Callable):
        """
        Run the main loop of the program to execute the callbacks

        Keyword arguments:
        function(ListCallable) : a list of callback functions that will be executed -required
        """
        glutInit(sys.argv)
        glutInitDisplayMode(self.mode)
        glutInitWindowSize(*self.size)
        glutInitWindowPosition(*self.position)
        glutCreateWindow(self.title)
        glutDisplayFunc(cb)
        glClearColor(*self.color)
        gluOrtho2D(*self.range)
        glutMainLoop()


def point(size: float):
    ''' wraps a callback function allowing it to plot points '''
    def decorate(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            glPointSize(size)  # setting the point size
            glBegin(GL_POINTS)
            func(*args, **kwargs)
            glEnd()
            glFlush()
        return wrapper
    return decorate

def line(width: float):
    ''' wraps a callback function allowing it to plot lines '''
    def decorate(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            glLineWidth(width)  # setting the line width
            glBegin(GL_LINES)
            func(*args, **kwargs)
            glEnd()
            glFlush()
        return wrapper
    return decorate


    
        

