'''
import random
# VV NON RIGGED VERSION VV
total = 0
og = int(random.randint(1,11))
print("You drew " + str(og))
ogd = int(random.randint(1,11))
print("The dealer drew a " + str(ogd))
totald=0
totald = totald + ogd
total = total + og
while total < 21:
    input1 = input("Hit or Stand")
    if input1 == "Hit":
        og = random.randint(1,11)
        print("You drew " + str(og))
        total = total + og
        print("Your total is " + str(total))
        if totald < 17:
         ogd = int(random.randint(1,11))
         #print("The dealer drew a " + str(ogd))
         totald = totald + ogd
         #print("The dealer has a total of " +str(totald))
         if totald > 21:
            print("You won!")
            break
         elif totald == 21:
            print("You lost!")
            break
         if total >21:
            print("You lost")
         elif total ==21:
            print("You won")
        
    else:
        ogd = int(random.randint(1,11))
        print("The dealer drew a " + str(ogd))
        totald = totald + ogd
        print("The dealer has a total of " +  str(totald))
        if totald > 21:
            print("You won!")
            break
        elif totald == 21:
            print("You lost!")
            break
        if total >21:
          print("You lost")
        elif total ==21:
          print("You won")
        elif totald > total:
          print("You lost")
          break

if total > 21:
    print("You lost")
else:
    print("You won!")
'''
























num = int(input("Enter a number -> "))
if (num >= 90):
  print("A")
elif (num >= 80):
  print("B")
elif (num >= 70):
  print("C")
elif (num >= 60):
  print("D")
else:
  print("F")

