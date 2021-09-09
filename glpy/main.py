from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from typing import Callable
from functools import wraps


class glpy:
    """Main class to initialize OpenGL and Glut functions

    """

    def __init__(self, **kwargs):
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
        bgcolor(List[float,float,float,float]) : background color of the window
        axis_range(List[float,float,float,float]) : range of the axis in 2D plane

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
            glClear(GL_COLOR_BUFFER_BIT)  # clearing the screen
            glPointSize(size)  # setting the point size
            glBegin(GL_POINTS)
            func(*args, **kwargs)
            glEnd()
            glFlush()
        return wrapper
    return decorate
