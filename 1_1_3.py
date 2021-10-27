#   a113_forward_and_right.py
import turtle as trtl
import random
import time
t = trtl.Turtle()
sessionid = random.randint(1,10)

print("Welcome to my game! Game Session ID:" + str(sessionid))
time.sleep(2)
step1 = input("Would you like to start a new game?")
if step1 == "yes" or "Yes":
  step2 = input("Alright, please type in the name you used earlier!")
  name = str(step2)
  if name == "rami" or "Rami" or "Nolan" or "nolan":
    print("Hey! You're an admin. Your current perms are shutting down the game or skipping all the levels. ")
    time.sleep(3)
    step3i = input("If you'd like to shut down the game type shut, if you want to continue playing type play, if you want to skip all the levels type skip")
    if step3i == "skip":
      print("ok")
    if step3i == "shut":
      shutno = 0
      while shutno <=10000:
         print(shutno)
         shutno = shutno+1
         time.sleep(0.1)
    if step3i == "play":
      print("Alright, you'll be playing the game normally!")
      time.sleep(1)
      step4i = input("Move 1: Would you like to go left or right?")
      if step4i == "right" or "Right":
        t.right(90)
        t.circle(25)
        print("You've run into a circle you died!")
      else:
        t.left(90)
        t.circle(25,360, 10)
        print("You've run into a decadadadada...; You died!")

wn = trtl.Screen()
wn.mainloop()
