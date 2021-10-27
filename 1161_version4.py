#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider is used
spider= trtl.Turtle()
spider.pensize(40)
spider.circle(20) ## Create a spider body

leg_number = 8
leg_length = 70
leg_pos = 180  / leg_number
spider.pensize(5) ## Configure spider legs
n = 4
def eye(color):
  spider.fillcolor(color)
  spider.begin_fill()
  spider.circle(5)
  spider.end_fill()
while (n < leg_number): ##Draw legs
  spider.goto(0,20)
  spider.setheading(leg_pos*n)
  spider.forward(leg_length)
  n = n + 1
n = 4
while (n < leg_number): ##Draw legs
  spider.goto(0,20)
  spider.setheading(180-leg_pos*-n)
  spider.forward(leg_length)
  n = n + 1

spider.penup()
spider.goto(0,25)
spider.pendown()
eye("red")
spider.penup()
spider.goto(20,25)
spider.pendown()
eye("red")
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()