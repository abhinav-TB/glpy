## glpy

glpy is pyOpenGl wrapper which lets you work with pyOpenGl easily.It is not meant to be a replacement for pyOpenGl but runs on top of pyOpenGl to avoid most of the boiler plate setup

## Features

 - Robust abstraction over pyOpenGl event loop
 - decorators to simplify callback functions

## Code Example

 
    from  glpy  import *
    app = glpy()
    
    @point(10)
    def plotpoints():
	    glColor3f(100, 150, 200)
	    glVertex2f(0,0)
	    
    app.run(lambda:plotpoints())


find more examples [here](https://github.com/abhinav-TB/glpy/tree/master/examples)
  

## Installation

    pip install glpy


## API Reference

#### glpy() 

```
allowed keyword arguments
```

| Parameter | Type     | Description                | Default               |
| :-------- | :------- | :------------------------- | :------------------------- |
   mode     | constant | Display mode               | GLUT_RGBA
   size     | tuple    | Window size                | (500,500)
   position | tuple    | Window position            | (0,0)
   bgcolor  | tuple    | background color           | (0, 0, 0, 1.0)
   title    | string   | window title               | new title
axis_range  | tuple    | The range of 2D plane      | (-100, 100,-100, 100)
 

## How to use?

 - Make sure you have opengl installed on your system
 - Install the package using  pip.
 - import the package and initialilze glpy
 
   `app = glpy()`
 - you can pass in additional parameters as seen in the API Reference as keyword arguments

   ``` app = glpy(title = "line drawing")```
  - define your callback function with the help of point decorator which takes the size of the     point to be plotted as an argument . NOTE: using a decorator is not neccesory for the library to work but it can significatly reduce the code size
	``` 
    @point(10)
    def plotpoints():
	    glColor3f(100, 468, 200)
	    glVertex2f(0,0)
	```
- call the run the method using the callback function as  an argument to run the function
NOTE: use a lambda function to pass callback functions with arguments

    ``` app.run(lambda:plotpoints())```

## New Features

- @grid decorator:-  this can be used as a higher level decorator to call back functions.It will create grid lines. This is still in beta and only work with      default screen dimensions. Check out this [example](https://github.com/abhinav-TB/glpy/blob/master/examples/grid.py) to learn more

- @line decorator:- this is similar to the existing point decorator, it can be used to draw a line easily
checkout this [example](https://github.com/abhinav-TB/glpy/blob/master/examples/line.py) to learn more


## Contribute

Contributions are what makes the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

 1. Fork the Project
 2.  Create your Feature Branch (git checkout -b feature/AmazingFeature)
 3. Commit your Changes (git commit -m 'Add some AmazingFeature')
 4.  Push to the Branch (git push origin feature/AmazingFeature)
 5. Open a Pull Request

  

## License
APACHE © [Abhinav TB ](https://github.com/abhinav-TB)


