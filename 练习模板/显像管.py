#Programmer: Qin Xusen
#Time: 2021/4/27-10:08
import turtle
import time
def drawgap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawgap()
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2, 3, 5, 6,7, 8, 9] else drawline(False)
    drawline(True) if digit in [0,1,2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
    for i in date:
        if i=='-':
            turtle.write('年', font=("arial",18,"normal"))
            turtle.color("green")
            turtle.fd(40)
        elif i=='=':
            turtle.write('月', font=("arial",18,"normal"))
            turtle.color("blue")
            turtle.fd(40)
        elif i=='+':
            turtle.write('日', font=("arial",18,"normal"))
        elif i == '_':
            turtle.write('时', font=("arial", 18, "normal"))
            turtle.color("purple")
            turtle.fd(40)
        elif i == '|':
            turtle.write('分', font=("arial", 18, "normal"))
            turtle.color("yellow")
            turtle.fd(40)
        elif i == ';':
            turtle.write('秒', font=("arial", 18, "normal"))
        else:
            drawdigit(eval(i))
def main():
    turtle.setup(2000,350,0,200)
    turtle.penup()
    turtle.fd(-600)
    turtle.pensize(5)
    drawdate(time.strftime('%Y-%m=%d+%H_%M|%S;',time.localtime(time.time())))
    turtle.hideturtle()
    turtle.done()
main()