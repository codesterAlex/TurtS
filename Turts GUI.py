import turtle
from tkinter import *


def showturtle():  # function for showing turtle
    turtle.showturtle()


def turnleft():  # function for turning the turtle
    leftEntry_num = int(leftEntry.get())
    turtle.left(leftEntry_num)


def move():  # function for turning the turtle
    moveEntry_num = int(moveEntry.get())
    turtle.forward(moveEntry_num)

def Pup_Pdn():  #Function for toggle button | toggles penup and pendown
    if Pup_Pdn_button.config('relief')[-1] == 'sunken':
        Pup_Pdn_button.config(relief = "raised")
        turtle.penup()
        Pup_Pdn_button.config(text="Pen Up")
    else:
        Pup_Pdn_button.config(relief = "sunken")
        turtle.down()
        Pup_Pdn_button.config(text="Pen Down")


window = Tk()
window.title("Turtle")
window.geometry("300x300")

heading = Label(window, text="TURTLE GUI").pack()

showturtle_button = Button(window, text="Show Turtle", command=showturtle).pack()

leftEntry = Entry(window)  # Editbox for left angle
leftEntry.pack()
leftEntry_Button = Button(window, text="Turn left", command=turnleft)
leftEntry_Button.pack()

moveEntry = Entry(window)  # Editbox for left angle
moveEntry.pack()
moveEntry_Button = Button(window, text="Move", command=move)
moveEntry_Button.pack()

Pup_Pdn_button = Button(window, text = "Pen Down", width = 12, relief = "sunken", command = Pup_Pdn)
Pup_Pdn_button.pack()


window.mainloop()
