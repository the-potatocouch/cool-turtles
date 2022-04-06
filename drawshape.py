# turtle1.py
# Made by PotatoCouch (https://github.com/the-potatocouch)

import math
import turtle

screen = turtle.getscreen()

tutel = turtle.Turtle()

tutel.speed("normal")

tutel.shape("turtle")

tutel.pensize(10)

turtle.title("Turtle")

turtle.degrees()

tutel.setheading(90)


def drawshape(sides, radius):

    tutel.penup()

    # find the sum of all angles
    angles_sum = (sides - 2) * 180

    # find the value of a single angle in the polygon
    common_angle = angles_sum / sides

    # find the length of every side with trigonometry
    # same thing as solving for a ssa triangle
    # we know that 2 sides have the length of radius
    # and we know all angles. since we have 2 sides of
    # equal length, that means that the angles that make up
    # them and their adjacent side (the unknown here)
    # are equal to the common angle (divided by two but multiplied by two since we have two of them)
    # because of this, we can calculate the missing angle
    # because the sum of all angles in a triangle is equal to 180
    # so, angle3 = 180 - (angle1 + angle2)

    # the common angle is equal to 2 normal angles

    angle3 = 180 - (common_angle)

    # finding unknown side

    x = (math.sin(angle3) * radius) / (math.sin(common_angle / 2))

    print(x)
    tutel.pendown()

    # repeat the same thing once for every side

    for i in range(sides):

        tutel.forward(x)

        tutel.right(common_angle)

    tutel.left(common_angle)

    tutel.penup()

    tutel.home()


drawshape(4, 80)


while True:

    tutel.home()
