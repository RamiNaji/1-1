# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import time

#-----game configuration----
global score
score =0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
circle = trtl.Turtle()
circle.shape('circle')
circle.speed(0)
score_writer = trtl.Turtle()
counter =  trtl.Turtle()
#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def update_score():
  score_writer.penup()
  score_writer.goto(-100,200)
  score_writer.pendown()
  font_setup = ("Arial", 20, "normal")
  score_writer.clear()
  global score
  score = score + 1
  score_writer.write(score, font=font_setup)


def circle_clicked(x,y):
    if timer_up != True:
      circle.color('pink')
      circle.color('black')
      x = random.randint(0,400)
      y = random.randint(0,300)
      circle.penup()
      circle.goto(x,y)
      update_score()


#-----events----------------
circle.onclick(circle_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()