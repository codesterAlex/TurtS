import turtle

turtle.showturtle()
print("[1] Turn left: ")
print("[2] Move forward: ")
print("[3] Penup: ")
print("[4] Pendown: ")
print("[5] Draw circle: ")
print("[6] Change color: ")
x = eval(input("Enter the option: "))
while True:
    if x == 1:
        left_angle = eval(input("Enter angle: "))
        turtle.left(left_angle)
        x = eval(input("Enter the option: "))
    elif x == 2:
        forward_angle = eval(input("Enter angle: "))
        turtle.forward(forward_angle)
        x = eval(input("Enter the option: "))
    elif x == 3:
        turtle.penup()
        x = eval(input("Enter the option: "))
    elif x == 4:
        turtle.pendown()
        x = eval(input("Enter the option: "))
    elif x == 5:
        circle_angle = eval(input("Enter angle: "))
        turtle.circle(circle_angle)
        x = eval(input("Enter the option: "))
    elif x == 6:
        color_angle = eval(input("Enter enter: "))
        turtle.color(color_angle)
        x = eval(input("Enter the option: "))
    else:
        print("Enter from 1-6")
