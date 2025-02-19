from turtle import Turtle,Screen
tim= Turtle()
screen= Screen()
screen.bgcolor("yellow")

# Movement Functions

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
# make the screen listen
screen.listen()

# takes command on visual stage

screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")
# clear()
screen.exitonclick()