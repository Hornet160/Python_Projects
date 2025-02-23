import turtle as t
import random

tim=t.Turtle()
color_list=["red",'orange','green','blue','pink','black','cyan','blue','gray','olive']

def draw_shape(num_of_sides):
    angle=360/num_of_sides
    for _ in range(num_of_sides):
        tim.width(5)
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3,11):
    tim.color(random.choice(color_list))
    draw_shape(shape_side)

screen=t.Screen()
screen.exitonclick()

# for line in range(3,11):
#     angle = int(360 / line)
#     line_color=color_list[line-2]
#     for turn in range(1,line+1):
#         tim.color(line_color)
#         tim.right(angle)
#         tim.forward(100)
