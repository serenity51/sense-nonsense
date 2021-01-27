# # Adding fruits and vegs to the cart --- finding cost of total purchase and also balance left with me

fruits= ['melon', 'apple', "kiwi", "orange", "banana"]
cost=0
quan=0
inAmount= 1400
def totcost( quan, cost):
 for i in fruits:
     return quan *cost
tf = totcost( 10, 50) +  totcost( 10,10)+ totcost(10,60) + totcost( 10,20)+ totcost(10,5 )
print(tf) #amt spent on fruits



# Adding vegetables to the cart
kg=0
cost=0
veg= ["lemon","carrot","beans" ]
def tcost( kg, cost):
 for i in veg:
     return kg * cost
tv=tcost( 2,20) + tcost( 3, 60) + tcost( 2, 40)
print(tv) # "amount spent on vegetables is"

Total= tf+tv  #Total spent on fruits and veg
print(tf, tv, Total)


#program to determine how much money is left
def balance(inAmount, Total):
  bal = (inAmount - Total)
  if inAmount > Total:
    print("you can buy more fruit\t" + str(bal) + " " "is left")
  if Total > inAmount:
    print(" you are in the red-return some fruits", bal)
balance(inAmount,Total)

output
# 1450 300 1750
#  you are in the red-return some fruits -350

________________________________________________________________________________________________________

value for tf + tv was entered by me on the basis of the values obtained from

#print("Amount spent on fruits is",totcost("apple", 10, 50) + totcost("melon", 10,10)+ totcost("kiwi",10,60)+\
    #  totcost("orange", 10,20)+ totcost("banana",10,5 ))  ------(this is-tf)
#
#                                                              and
# print("amount spent on vegetables is",tcost("lemon", 2,20) + tcost("carrot", 3, 60) + tcost(" beans", 2, 40))-----(this is tv)


What I did
# Now I just equated b in balance to tf+tv and it automatically substituted those values for b when I called the balance function.
# which is fine,but


Question
# Is it possible to actually call the above two functions totcost and tcost to give me the same result.

Doubt
# When i did try to equate b to totcost and tcost, it didn't work.
# Presumably because both those functions were the combination of many totcosts and tcosts. Will that be right?

Doubt 2
#  I manually entered the values of tf and tv on the basis of the print result. Is it possible to tell the balance function
#  to take those values from the print command itself?

