from math import sqrt, sin, cos, pi, radians
import turtle
def num():
    num = int(input('Enter an integer between 1 and 100: '))
    if 1<num<100:
        print('Ok')
#num()
def rang():
    num = int(input('Enter integer btw 1 and 100(inclusive): '))
    if 1 <=num<=100:
        print('Ok')
    else:
        print('Out of range')
#rang()
def maxmin():
    num1 = int(input('Enter the first integer: '))
    num2 = int(input('Enter the second integer: '))
    num3 = int(input('Enter thr third integer: '))
    num4 = int(input('Enter the fourth integer: '))
    num5 = int(input('Enter the fifth integer: '))
    maximum = num1
    minimum = num1
    if maximum<num2:
        maximum = num2
    if maximum<num3:
        maximum = num3
    if maximum<num4:
        maximum = num4
    if maximum<num5:
        maximum = num5
    if minimum>num2:
        minimum = num2
    if minimum>num3:
        minimum = num3
    if minimum>num4:
        minimum = num4
    if minimum>num5:
        minimum = num5    
    print('Maximum =', maximum)
    print('Minimum =', minimum)
#maxmin()
def dist():
    px = float(input('Enter x coordinate of the spacecraft: '))
    py = float(input('Enter y coordinate of the spacecraft: '))

    x = float(input('Enter initial satellite x coordinate: '))
    y = float(input('Enter initial satellite y coordinate: '))

    rads = radians(60)

    COS_theta = cos(rads)
    SIN_theta = sin(rads)

    for increment in range(0, 7):
        dist = sqrt((x - px)**2 + (y-py)**2)
        print('Distance to satellite {0:10.2f} km'.format(dist))
        x, y = x*COS_theta - y*SIN_theta, x*SIN_theta + y*COS_theta

#dist()
def boxturtle():
    turtle.pencolor('red')
    turtle.forward(200)
    turtle.left(90)
    turtle.pencolor('blue')
    turtle.forward(150)
    turtle.left(90)
    turtle.pencolor('green')
    turtle.forward(200)
    turtle.left(90)
    turtle.pencolor('black')
    turtle.forward(150)
    turtle.hideturtle()
    turtle.exitonclick()
#boxturtle()
def octogon():
    turtle.pencolor('red')
    turtle.penup()
    turtle.setposition(-45, 100)
    turtle.pendown()
    for i in range(8):
        turtle.forward(80)
        turtle.right(45)

    distance = 0.2
    angle = 40
    turtle.pencolor('blue')
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()
    for i in range(100):
        turtle.forward(distance)
        turtle.left(angle)
        distance += 0.5

    turtle.hideturtle()
    turtle.exitonclick()
#octogon()
def speedvsdelay():
    y = -200
    #Default speed and default delay
    turtle.color('red')
    for x in range(10):
        turtle.penup()
        turtle.setposition(-200, y)
        turtle.pendown()
        turtle.forward(400)
        y += 10
    #Slowest speed, but no delay
    turtle.speed('slowest')
    turtle.delay(0)
    turtle.update()
    turtle.color('blue')
    for x in range(10):
        turtle.penup()
        turtle.setposition(-200, y)
        turtle.pendown()
        turtle.forward(400)
        y += 10
    #Fastest speed with 500 ms delay
    turtle.speed('fastest')
    turtle.delay(500)
    turtle.update()
    turtle.color('green')
    for x in range(10):
        turtle.penup()
        turtle.setposition(-200, y)
        turtle.pendown()
        turtle.forward(400)
        y += 10

    #Fastest speed with no delay
    turtle.speed('fastest')
    turtle.delay(0)
    turtle.update()
    turtle.color('black')
    for x in range(10):
        turtle.penup()
        turtle.setposition(-200, y)
        turtle.pendown()
        turtle.forward(400)
        y += 10
    turtle.done()
#speedvsdelay()
def triangle():
    turtle.pencolor('black')
    for edge in range(3):
        turtle.forward(200)
        turtle.left(120)
    turtle.exitonclick()
#triangle()
def star():
    turtle.pencolor('red')
    for edge in range(5):
        turtle.forward(200)
        turtle.right(144)
    turtle.exitonclick()
#star()
def zigzag():
    turtle.pencolor('yellow')
    up = 85
    down = 170
    for edge in range(2):
        turtle.left(up)
        turtle.forward(200)
        turtle.right(down)
        turtle.forward(200)
        up += 85
        down += 0
    turtle.exitonclick()
#zigzag()
def mystic():
    turtle.pencolor('green')
    ang = 1
    for edge in range(500):
        for edge in range(4):
            turtle.speed(0)
            turtle.forward(50)
            turtle.left(90)
        turtle.left(ang)
        ang += 1
    turtle.exitonclick()
#mystic()
def grid():
    turtle.pencolor('orange')
    turtle.setposition(0, 0)
    x = 0
    y = 0
    for edge in range(7):
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.setposition(0, y)
        y += 20
    turtle.setposition(0, 0)
    turtle.left(90)
    for edge in range(7):
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.setposition(x, 0)
        x += 20
    turtle.exitonclick()
#grid()
def circle():
    turtle.color('blue')
    turtle.delay(0)
    for edge in range(600):
        turtle.forward(1)
        turtle.left(0.6)
    turtle.exitonclick()
#circle()
def hexagons():
    turtle.pencolor('red')
    x = -100
    y = 100   
    for i in range(20):
        turtle.penup()
        turtle.setposition(-100, y)
        turtle.pendown()
        x = -100
        y = 100
        for j in range(20):
            turtle.delay(0)
            turtle.penup()
            turtle.setposition(x, y)
            turtle.pendown()
            for k in range(6):
                turtle.forward(10)
                turtle.left(60)
            x += 20
        y -= 20
hexagons() 
        
