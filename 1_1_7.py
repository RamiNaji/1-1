#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()     
  my_turtles.append(t)
  new_color = turtle_colors.pop()
  t.color(new_color)

# the start positions are set 
startx = 0
starty = 0
direction = 90
#This loops through the list
for t in my_turtles:
  t.setheading(direction)
  t.goto(startx, starty)
  t.pendown()
  t.right(45)     
  t.forward(50)
  direction = t.heading()
  print(direction)
  
  

#	Changing the position
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()