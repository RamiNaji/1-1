import random
import time
import turtle as trtl
t = trtl.Turtle()
t.speed(0)
def fullsetup():
    def goto(x,y):
        t.penup()
        t.goto(x,y)
    def fullstand():
        goto(-150,-150)
        t.pendown()
        for i in range(2):
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(100)
        goto(-200, -125)
        t.write("Calculate")
    def fullhit():
        goto(150,-150)
        t.pendown()
        for i in range(2):
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(100)
        goto(100, -125)
        t.write("Hit")
    fullstand()
    fullhit()
    t.penup()
    t.speed(0)
    t.shape("circle")
    goto(0,0)
    global HitT
    global StandT
    HitT = False
    StandT = False

def follow(x, y):
    gotoresult = t.goto(x, y)
    t.color("red")
    time.sleep(0.2)
    t.color("black")
    if -250<x<-150:
        if -150<y<-100:
            print("User tapped Stand") 
        
    if 50<x<150:  
        if -150<y<-100:
            print("User tapped Hit") 
            global HitT
            global StandT
            HitT = "Yes"
            StandT = "No"
    print(t.xcor(), t.ycor())
    return gotoresult
    



fullsetup()

wn = trtl.Screen()
wn.onclick(follow)
wn.mainloop()

