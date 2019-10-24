from turtle import *

myTurtle = Turtle()
screen = myTurtle.getscreen()
myTurtle.forward(200)

def printName():
	name = screen.textinput("name", "What is your name?")
	myTurtle.write(name, move=True, align="left", font=("Arial", 40,"normal"))
	screen.listen()

def goForward():
	myTurtle.forward(10)

screen.onkey(printName, "p")
screen.onkey(goForward,"Up")

screen.listen()

screen.mainloop()
