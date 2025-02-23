import turtle as t
import random

tim=t.Turtle()
screen=t.Screen()
# color_list=["red",'orange','green','blue','pink','black','cyan','blue','gray','olive']
directions=[0, 90, 180, 270]
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_tuple=(r,g,b)
    return color_tuple


for _ in range(0,500):
    tim.pensize(10)
    tim.speed("fastest")
    tim.setheading(random.choice(directions))
    tim.color(random_color())
    # tim.color(random.choice(color_list))
    tim.forward(30)


screen.exitonclick()