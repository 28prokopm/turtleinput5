import random
import turtle
#insert random


screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('black')


t = turtle.Turtle()


t.pencolor('white')
t.penup()
t.goto(0,200)
t.pendown()
t.write("Background Color",font=("arial",30,"normal"),align="center")


t.pencolor('tan')
t.penup()
t.goto(-75,100)
t.pendown()
t.write("1.Tan",font=("arial",20,"normal"),align="left")


t.pencolor('azure')
t.penup()
t.goto(-75,50)
t.pendown()
t.write("2.Azure",font=("arial",20,"normal"),align="left")


t.pencolor('aquamarine')
t.penup()
t.goto(-75,0)
t.pendown()
t.write("3.Aquamarine",font=("arial",20,"normal"),align="left")


t.pencolor('darkkhaki')
t.penup()
t.goto(-75,-50)
t.pendown()
t.write("4.DarkKhaki",font=("arial",20,"normal"),align="left")


t.pencolor('white')
t.penup()
t.goto(0,-150)
t.pendown()
t.write("Chose One",font=("arial",30,"normal"),align="center")


choose = int(input("Choose one: "))
if choose == 1:
    screen.bgcolor('tan')
elif choose == 2:
    screen.bgcolor('azure')
elif choose == 3:
    screen.bgcolor('aquamarine')
else:
    screen.bgcolor('darkkhaki')
t.clear()
t.pencolor('black')
t.penup()
t.goto(0,0)
t.pendown()
t.write("Enter you name",font=("arial",30,"normal"),align="center")

t.clear()

name = input("Enter your name: ")
t.clear()
operation = random.randint(1, 4)
operation = 4
if operation == 1:
    symbol = "+"
    number1 = random.randint(-100,100)
    number2 = random.randint(-100,100)
    solution=number1 + number2
elif operation == 2:
    symbol = "-"
    number1 = random.randint(-100,100)
    number2 = random.randint(-100,100)
    solution=number1 - number2
elif operation == 3:
    symbol = "*"
    number1 = random.randint(-10, 10)
    number2 = random.randint(-10, 10)
    solution = number1 * number2
elif operation == 4:
    symbol = "/"
    number1 = random.randint(-10, 10)
    number2 = random.randint(1, 10)
    sign = random.randint(1, 2)
    if sign == 2:
        number2 = -1 + number2
    solution = number1 / number2


t.pencolor('red')
t.penup()
t.goto(0,150)
t.pendown()
t.write(name,font=("arial",30,"normal"),align="center")


t.pencolor('red')
t.penup()
t.goto(-200,0)
t.pendown()
t.write(number1,font=("arial",30,"normal"),align="center")


t.pencolor('red')
t.penup()
t.goto(-100,0)
t.pendown()
t.write(symbol,font=("arial",30,"normal"),align="center")


t.pencolor('red')
t.penup()
t.goto(0,0)
t.pendown()
t.write(number2,font=("arial",30,"normal"),align="center")


t.pencolor('red')
t.penup()
t.goto(100,0)
t.pendown()
t.write("=",font=("arial",30,"normal"),align="center")


answer=float(input('Enter Answer:'))


t.pencolor('red')
t.penup()
t.goto(200,0)
t.pendown()
t.write(solution,font=("arial",30,"normal"),align="center")


t.pencolor('red')
t.penup()
t.goto(0,-150)
t.pendown()
t.write("Your answer is: "+str(answer),font=("arial",30,"normal"),align="center")


if solution == answer:
    screen.bgcolor('dodgerblue')
    t.pencolor('red')
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.write("Correct",font=("arial",30,"normal"),align="center")
else:
    screen.bgcolor('darkorange')
    t.pencolor('red')
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.write("Incorrect",font=("arial",30,"normal"),align="center")


turtle.done()