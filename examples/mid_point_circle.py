from glpy import *

app = glpy()

def drawPixel(x,y):
    glColor3f(0.0,1.0,0.5)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()
    glFlush()

def midPointCircleDraw(x_centre, y_centre, r): 
    x = r 
    y = 0  
    drawPixel(x+x_centre,y+y_centre)
    if (r > 0) : 
        
        drawPixel(x+x_centre,-y+y_centre)
        drawPixel(y+x_centre,x+y_centre)
        drawPixel(-y+x_centre,x+y_centre)
 
    P = 1 - r  
  
    while x > y: 
      
        y += 1
 
        if P <= 0:  
            P = P + (2 * y) + 1
 
        else:          
            x -= 1
            P = P + (2 * y) - (2 * x) + 1

 
        drawPixel(x+x_centre,y+y_centre)  
        drawPixel(-x+x_centre,y+y_centre)  
        drawPixel(x+x_centre,-y+y_centre)  
        drawPixel(-x+x_centre,-y+y_centre)  
         

        if x != y: 
            drawPixel(y+x_centre,x+y_centre)  
            drawPixel(-y+x_centre,x+y_centre)  
            drawPixel(y+x_centre,-x+y_centre)  
            drawPixel(-y+x_centre,-x+y_centre) 


x = int(input("\nEnter center:\n\tx: "))
y = int(input("\n\ty: "))
r = int(input("\nRadius: "))
app.run(lambda: midPointCircleDraw(x,y,r))
