import turtle as t
import random
# import random_Color as c
tim=t.Turtle()
screen=t.Screen()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple
tim.speed("fastest")
# r_color=c.RandomColor()
def draw_spirograph(size_of_gap,circle_radius):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(circle_radius)
        tim.setheading(tim.heading()+size_of_gap)
        # tim.circle(90, 360) this also works
        # tim.left(10) this also works
degree_of_gap=int(input("What is the gaping degree? "))
radius_of_circle=int(input("What is the radius of the circle? "))
draw_spirograph(degree_of_gap,radius_of_circle)
screen.exitonclick()