# # Adding fruits and vegs to the cart --- finding cost of total purchase and also balance left with me

fruits= ['melon', 'apple', "kiwi", "orange", "banana"]
cost=0
quan=0
def totcost(fruits, quan, cost):
 for i in fruits:
     return quan *cost
 print('total cost of fruits is', quan *cost)
print("Amount spent on fruits is",totcost("apple", 10, 50) + totcost("melon", 10,10)+ totcost("kiwi",10,60)+\
      totcost("orange", 10,20)+ totcost("banana",10,5 ))
tf=  1450  # "Amount spent on fruits is",

# Adding vegetables to the cart
kg=0
cost=0
veg= ["lemon","carrot","beans" ]
def tcost(veg, kg, cost):
 for i in veg:
     return kg * cost
print("amount spent on vegetables is",tcost("lemon", 2,20) + tcost("carrot", 3, 60) + tcost(" beans", 2, 40))
tv= 300  # "amount spent on vegetables is"

Total = tf+tv
print(Total)

# # #program to determine how much money is left
a=0
b=(Total)
def balance(a, b):
  bal = (a - b)
  if a> b:
    print("you can buy more fruit\t" + str(bal) + " " "is left")
  if b > a:
    print(" you are in the red-return some fruits", bal)
balance(1800, b)

# This is the output- which is correct
# 1750(1450 for fruits and 300 for vegs)
# you can buy more fruit	50 is left    - The third function balance correctly gives me this


#
# value for tf + tv was entered by me on the basis of the values obtained from

# print(print("Amount spent on fruits is",totcost("apple", 10, 50) + totcost("melon", 10,10)+ totcost("kiwi",10,60)+\
#       totcost("orange", 10,20)+ totcost("banana",10,5 ))  -------tf
#
#                                                              and
#
#   print("amount spent on vegetables is",tcost("lemon", 2,20) + tcost("carrot", 3, 60) + tcost(" beans", 2, 40))-----tv

# What I did
#
# Now I just equated b in balance to tf+tv and it automatically substituted those values for b when I called the balance function.
# which is fine,but


# Question
# Is it possible to actually call the above two functions totcost and tcost to give me the same result.

# Doubt
# When i did try to equate b to totcost and tcost, it didn't work.
# Presumably because both those functions were the combination of many totcosts and tcosts. Will that be right?

# Doubt 2
#  I manually entered the values of tf and tv on the basis of the print result. Is it possible to tell the balance function
#  to take those values from the print command itself?

