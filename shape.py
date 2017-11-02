#This is my software for turtle which will help to make shapes

import turtle

turtle.showturtle()
move = True
bgcolor=input("Enter backgroud color: ")
turtle.bgcolor(bgcolor)

print("Enter [1] for automatic shape \n")
print("Enter [2] for making mannual shape \n")

shape = int(input("Enter the your choice? : "))

if shape == 1:
    print("Enter [1] for circle.")
    print("Enter [2] for squre")
    print("Enter [3] for triangle")
    print("Enter [4] for parrallel")

    command = int(input("Enter your choice? "))
    while move:
        if command == 1:
            color = input("Enter the color of the circle? ")
            width = int(input("Enter the width of the line? "))
            radius = int(input("Enter the radius of the squre? :"))
            turtle.color(color)
            turtle.width(width)
            turtle.circle(radius)
            any = input("Enter any key to exit")
            if any != None:
                move = False

        elif command == 2:
            color = input("Enter the color of the squre?" )
            width = int(input("Enter the width of the line? "))
            turtle.color(color)
            turtle.width(width)
            length = int(input("Enter the length of the each line? "))
            turtle.penup()
            turtle.goto(-length,length)
            turtle.pendown()
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            any = input("Enter any key to exit")
            if any != None:
                move = False
        elif command == 3:
            color = input("Enter the color of the triangle? ")
            width = int(input("Enter the width of the line? "))
            turtle.color(color)
            turtle.width(width)
            l1 = int(input("Enter the Length of the first line? "))
            l2 = int(input("Enter the Length of the second line? "))
            aAngle = int(input("Enter the angle of inclination? "))
            rAngle = 180- aAngle
            turtle.forward(l1)
            turtle.left(rAngle)
            turtle.forward(l2)
            turtle.goto(0,0)
            any = input("Enter any key to exit")
            if any != None:
                move = False

        elif command == 4:
                color = input("Enter the color of the triangle? ")
                width = int(input("Enter the width of the line? "))
                turtle.color(color)
                turtle.width(width)
                length = int(input("Enter the length of base? "))
                height = int(input("Enter the height of parallogram? "))
                angle = int(input("Enter the angle of inclination? "))
                turtle.forward(length)
                turtle.left(angle)
                turtle.forward(height)
                turtle.penup()
                turtle.goto(0,0)
                turtle.pendown()
                turtle.forward(height)
                turtle.right(angle)
                turtle.forward(length)
                any = input("Enter any key to exit")
                if any != None:
                    move = False

        else:
                print("Sorry the input is incorrect!!!")





else:
    print("Sorry!!! service not avalaible.")








