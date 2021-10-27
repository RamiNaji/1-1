#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
ladybug.pensize(10)
leg_number = 7
leg_length = 70
leg_pos = 240  / leg_number
n = 4
while (n < leg_number): ##Draw legs
  ladybug.penup()
  ladybug.goto(0,-50)
  ladybug.pendown()
  ladybug.setheading(leg_pos*n)
  x=0
  while x <10:
   ladybug.forward(leg_length/5)
   ladybug.right(18)
   x=x+1
  n = n + 1
n = 4
while (n < leg_number): ##Draw legs
  ladybug.penup()
  ladybug.goto(0,-50)
  ladybug.pendown()
  ladybug.setheading(180-leg_pos*-n)
  x=0
  while x <10:
   ladybug.forward(leg_length/5)
   ladybug.right(18)
   x=x+1

  n = n + 1
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
num_dots = 1
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1



ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()