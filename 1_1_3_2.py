#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0

# iterate
while floor < num_floors: 
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("gray")
  rem = floor % 6
  if (rem >2):
    painter.color("blue")

    rem1 = floor %21
    if (rem1 >= 0 and floor >= 21):
      painter.penup()
      painter.goto(x+55, y-105)
      painter.pendown()


    if (rem1>= 0 and floor >=42):
      painter.penup()
      painter.goto(x+110, y-210)
      painter.pendown()






  y = y + 5 # location of next floor
  floor = floor + 1

   
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()