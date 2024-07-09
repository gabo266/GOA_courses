from turtle import *


#we want to paint a hous

speed(10)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(125)    #height of the door
right(90)
forward(60)
right(90)
forward(125)
end_fill()

penup()
goto(200, 200)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(15, 125)
pendown()

color("brown")
begin_fill()
right(240)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()

penup()
goto(185, 125)
pendown()

color("brown")
begin_fill()
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()


exitonclick()