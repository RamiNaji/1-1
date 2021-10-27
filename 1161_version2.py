#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider is used
spider= trtl.Turtle()
spider.pensize(40)
spider.circle(20) ## Create a spider body

leg_number = 6
leg_length = 70
leg_pos = 380 / leg_number
spider.pensize(5) ## Configure spider legs
n = 0
while (n < leg_number): ##Draw legs
  spider.goto(0,0)
  spider.setheading(leg_pos*n)
  spider.forward(leg_length)
  n = n + 1
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()