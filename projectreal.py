'''
import turtle as trtl
import time
import random
t=trtl.Turtle()

Option = input("Would you like to add, subtract, multiply, or divide?(type a for addition, s for subraction, etc.)? ")
if Option == "s":
  a=input("What would you like to subtract in the format(x-y)? ")
  a= a.split("-")
  last  =int(a[0]) - int(a[1])
  print(last)
  t.write(str(last))
  wn = trtl.Screen()
  wn.mainloop()
elif Option == "a":
   b= input("What would you like to add in the format(x+y)? ")
   b=b.split("+")
   lastb = int(b[0]) + int(b[1])
   print(lastb)
   t.write(str(lastb))
   wn = trtl.Screen()
   wn.mainloop()
elif Option == "m":
    c=input("What would you like to multiply in the format(x*y)? ")
    c=c.split("*")
    lastc = int(c[0])*int(c[1])
    print(lastc)
    t.write(str(lastc))
    wn = trtl.Screen()
    wn.mainloop()
elif Option == "d":
   d= input("What would you like to divide in the format(x/y)? ")
   d=d.split("/")
   lastd = int(d[0])/int(d[1])
   print(lastd)
   t.write(str(lastd))
   wn = trtl.Screen()
   wn.mainloop()
else:
  print("Restart code")
'''
Crocadile_Roast = 18
Seared_Beef = 15
Baked_Frog =  17
Stuffed_Duck = 22
Soaked_Chicken = 16
Baby_Kangaroo = 36

Meat_strips = 14
Meat_Salad = 16

Exotic_Tropical_Drink = 8
Jack_Sparrow_Rum = 12
James_Bonds_Beer = 12

##foodmathtotal
food_list = ["N/A",Crocadile_Roast, Seared_Beef, Baked_Frog, Stuffed_Duck, Soaked_Chicken, Baby_Kangaroo, Baby_Kangaroo, Meat_strips, Meat_Salad, Exotic_Tropical_Drink, Jack_Sparrow_Rum, James_Bonds_Beer]
item_number = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eigth', 'ninth', 'tenth', 'eleventh', 'twelth']
n_one = 0
total_price = 0

while True:
  food_choice = input('What is your ' + item_number[n_one] + ' item?')
  try:
    food_choice = int(food_choice)
  except ValueError:
    print('Please input number only!')
    continue
  n_one += 1
  total_price += food_list[food_choice]

  end = input('Would you like to end the order? (Y/N): ')
  if end.lower() == 'y':
    print('Your total price is: ' + str(total_price))
    break
  else:
    continue

