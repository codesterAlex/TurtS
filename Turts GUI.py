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


def circle():  # function for turning the turtle
    circle_size_num = int(circle_size.get())
    turtle.circle(circle_size_num)

def pencolor():  # function for changing pen color
    color_text_num = color_text.get()
    turtle.color(color_text_num)


def pensize():  # function for changing pen size
    pensize_num = int(pensize_input.get())
    turtle.pen(pensize = pensize_num)


def bgcolor():  # function for changing Background color
    BG_color_text_num = BG_color_text.get()
    turtle.bgcolor(BG_color_text_num)

window = Tk()
window.title("Turtle")
window.geometry("200x400")

heading = Label(window, text="TURTLE GUI").pack()

showturtle_button = Button(window, text="Show Turtle", command=showturtle).pack()

leftEntry = Entry(window)  # Editbox for left angle
leftEntry.pack()
leftEntry_Button = Button(window, text="Turn left", command=turnleft)
leftEntry_Button.pack()

moveEntry = Entry(window)  # Editbox for move distance
moveEntry.pack()
moveEntry_Button = Button(window, text="Move", command=move)
moveEntry_Button.pack()

Pup_Pdn_button = Button(window, text = "Pen Down", width = 12, relief = "sunken", command = Pup_Pdn)
Pup_Pdn_button.pack()

circle_size = Entry(window)  # Editbox for circle size
circle_size.pack()
circle_size_Button = Button(window, text="Draw Circle", command=circle)
circle_size_Button.pack()

color_text = Entry(window)  # Editbox for color
color_text.pack()
color_text_Button = Button(window, text="Change Color", command=pencolor)
color_text_Button.pack()

pensize_input = Entry(window)  # Editbox for pen size
pensize_input.pack()
pensize_Button = Button(window, text="Change Pensize", command=pensize)
pensize_Button.pack()

BG_color_text = Entry(window)  # Editbox for color
BG_color_text.pack()
BG_color_text_Button = Button(window, text="Change BG Color", command=bgcolor)
BG_color_text_Button.pack()

window.mainloop()
