import turtle
from tkinter import *

def showturtle():       #function for showing turtle
    turtle.showturtle()

window = Tk()
window.title("Turtle")
window.geometry("300x300")

heading = Label(window, text = "TURTLE GUI")

showturtle_button = Button(window, text = "Show Turtle", command = showturtle)

showturtle_button.pack()
heading.pack()
window.mainloop()