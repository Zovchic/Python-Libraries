==================================== PyCanvas.py ====================================================

PyCanvas is a library for making 2D projects in the  Python console.

How to install it:

1. Copy or Move PyCanvas.py file into your project's folder
2. Then import it to your project using "import PyCanvas" or "from PyCanvas import *"
3. Success!

=================================== Function List ==================================================

1. canvas(width, height)
	
	canvas() function initializes the canvas. Returns 3 results:
		*  list, which is initialized canvas
		*  it's width
		*  it's height

	Example:

		A, w, h = canvas(9, 9) 

2. clc() / clcw()

	Clears the console(clc() for linux/Mac OS, clcw() for Windows)

3. create(lst, sym, lx, ly, objName)

	This function creates an object on canvas.
	Inputs:
		* lst - must be equal to variable, which stores your canvas
		* sym - equal to symbol, which will be displayed in canvas as your object
		* lx, ly -  start coordinates of object
		* objName - string, name, which is using by system

4. ers(lst, objName)

	Deletes an object from the canvas.

5. move(lst, objName, movex, movey)

	Moves an existing object.
	Inputs:
		* lst - must be equal to variable, which stores your canvas
		* objName - name of object you want to delete
		* movex, movey - number of steps by x, y you want to move the object by

6. prcvs(lst)

	Prints the canvas

7. frame(lst, delay=1.0, system="w")

	This function prints a canvas(lst input) with a delay after printing(delay input)
	You can use it in games and animations.

	system - letter that means your operating system("l" for Mac Os/linux, "w" for Windows)

8. coords(objName)

	Returns a list with object coordinates.
	You can get only x / y by using coords(objName)[0] / coords(objName)[1]

9. fobj(objName)

	Simply returns 1, if object exists and returns 0, if object doesn't exist