from glpy import *
app = glpy(title = "line drawing")

@point(10)
def plotLine(x1,y1,x2,y2):
    glColor3f(1.0,0.0,0.0) 

    x = x1
    y = y1
    glVertex2f(x, y)  # plot the first point

    dx = x2 - x1
    dy = y2 - y1

    p = dy - (dx/2)

    while x < x2:
        x += 1

        if p < 0:
            p += dy
        else:
            y += 1
            p += dy - dx

        glVertex2f(x, y)


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
app.run(lambda:plotLine(x1,y1,x2,y2))
