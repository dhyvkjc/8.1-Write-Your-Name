from turtle import *

Screen = Screen()



import turtle


screen = turtle.Screen()
screen.title("Drawing a Square")
screen.bgcolor("black")


pen = turtle.Turtle()
pen.shape("turtle")
pen.pencolor("blue")
pen.pensize(5)
pen.speed(2)



for _ in range(1):
    pen.right(180)
    pen.forward(50)
    pen.left(270)
    pen.forward(100)
    pen.right(-270)
    pen.forward(50)
    

pen.pencolor("red")
for _ in range(1):
    pen.up()
    pen.forward(25)
    pen.right(-270)
    pen.pendown()
    pen.forward(100)
    pen.right(180)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    pen.right(180)
    pen.forward(100)

pen.pencolor("green")
for _ in range(1):
    pen.penup()
    pen.right(90)
    pen.forward(25)
    pen.pendown()
    pen.forward(50)
    pen.left(180)
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.left(180)
    pen.forward(50)
    pen.left(-90)
    pen.forward(50)
    pen.left(-90)
    pen.forward(25)

pen.pencolor("yellow")
for _ in range(1):
    pen.penup()
    pen.forward(50)
    pen.left(90)
    pen.pendown()
    pen.forward(50)
    pen.left(180)
    pen.forward(100)
    pen.left(90)
    pen.forward(50)

pen.pencolor("white")
for _ in range(1):
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)

pen.pencolor("magenta")
for _ in range(1):
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.forward(50)
    pen.left(180)
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.left(180)
    pen.forward(50)
    pen.left(-90)
    pen.forward(50)
    pen.left(-90)
    pen.forward(25)

pen.pencolor("lime")
for _ in range(1):
    pen.penup()
    pen.forward(50)
    pen.pendown()
    pen.right(90)
    pen.forward(50)
    pen.left(180)
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(100)
    pen.left(180)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)

    


   


screen.exitonclick()
