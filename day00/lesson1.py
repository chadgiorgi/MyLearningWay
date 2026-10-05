from turtle import *

width(4)
color("blue")
speed(30)
#Walls
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#Door
forward(70)
left(90)

color("magenta")
begin_fill()
forward(100)
right(90)

forward(50)

right(90)
forward(100)
end_fill()
#Roof
penup()
goto(200, 200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

#windows
penup()
goto(10, 105)
pendown()

color("yellow")
begin_fill()
right(240)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(135, 105)
pendown()

begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()





exitonclick()
