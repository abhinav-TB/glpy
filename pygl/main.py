from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from typing import Callable
from functools import wraps


class pygl:
    """Main class to initialize OpenGL and Glut functions

    """

    def __init__(self, **kwargs):

        glutInit(sys.argv)
        self.displayMode(kwargs["display_mode"]
                         if "display_mode" in kwargs else GLUT_RGBA)
        self.windowSize(*kwargs["window_size"]
                        if "window_size" in kwargs else (500, 500))
        self.windowPosition(*kwargs["window_position"]
                            if "window_position" in kwargs else (0, 0))
        self.windowTitle(kwargs["window_title"]
                         if "window_title" in kwargs else "new title")
        print(kwargs["bgcolor"])
        self.bgColor(*kwargs["bgcolor"]
                     if "bgcolor" in kwargs else (0, 0, 0, 1.0))
        self.axis_range(*kwargs["axis_range"] if "axis_range" in kwargs else (
            0, 100, 0, 100))

    def run(self, cb: Callable):
        """
        Run the main loop of the program to execute the callbacks

        Keyword arguments:
        function(ListCallable) : a list of callback functions that will be executed -required
        bgcolor(List[float,float,float,float]) : background color of the window
        axis_range(List[float,float,float,float]) : range of the axis in 2D plane

        """
        glutDisplayFunc(cb)
        glutMainLoop()

    def displayMode(self, mode: tuple):

        glutInitDisplayMode(mode)

    def windowSize(self, x: int, y: int):
        glutInitWindowSize(x, y)

    def windowPosition(self, x: int, y: int):
        glutInitWindowPosition(x, y)

    def windowTitle(self, title: str = "new title"):
        glutCreateWindow(title)

    def bgColor(self, r: float, g: float, b: float, a: float):
        glClearColor(r, g, b, a)

    def axis_range(self, x: int, y: int, z: int, w: int):
        gluOrtho2D(x, y, z, w)


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
