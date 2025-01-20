
'''#star pattern
import turtle
star=turtle.Turtle()
star.right(75)
star.forward(100)
for i in range(4):
    star.right(144)
    star.forward(100)
turtle.done()

#creating a turtle
import turtle
s=turtle.Turtle()

#printing a square pattern
import turtle
s=turtle.Turtle()
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.hideturtle()#after shape we dont want turtle

#using for loop
import turtle
s=turtle.Turtle()
for i in range(4):
    s.forward(100)
    s.left(90)
s.hideturtle()



import turtle
s=turtle.Turtle()
s.forward(100)
s.penup()#pickup the turtle pen
s.right(90)
s.forward(100)
s.right(90)
s.pendown()#putsdown the turtle pen
s.forward(100)


#shapes with colour
import turtle
s=turtle.Turtle()
s.fillcolor("yellow")
s.begin_fill()
for i in range(4):
    s.forward(100)
    s.left(90)
s.end_fill()

#printing the heart pattern with text
import turtle
s=turtle.Turtle()
s.fillcolor("pink")
s.begin_fill()
s.right(45)
s.forward(100)
s.left(90)
s.forward(100)
s.circle(50,180)
s.right(90)
s.circle(50,180)
s.write("Harini",align="left",font=("Ariel",30,"bold"))
s.end_fill()'''

#rangoli
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
spiral = turtle.Turtle()
spiral.speed(20)
spiral.width(3)
colors = ["red","green","orange", "yellow",  "blue", "purple","teal"]
for i in range(360):
    spiral.color(colors[i % 7]) 
    spiral.forward(i)
    spiral.right(0)
    spiral.left(100)
turtle.done()

#pattern
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)  
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(4)  
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
i = 10
while True:
    spiral.color(colors[i % 6])  
    spiral.forward(i)
    spiral.left(80) 
    i += 1

turtle.done()





