# Adding fruits and vegs to the cart --- finding cost of total purchase and also balance left with me

fruits= ['melon', 'apple', "kiwi", "orange", "banana"]
veg= ["lemon","carrot","beans" ]
cost=0
quan=0     # for veg, quan is in kg.
inAmount= 1400

def totcost( quan, cost):
 for i in fruits:
     for i in veg:
      tf= quan *cost
     tv = quan * cost
     return tf
     return tv
tf= totcost(10, 40) + totcost(10, 20) + totcost(10, 60) + totcost(10, 20) + totcost(10, 5)
tv= totcost(2, 20) + totcost(3, 60) + totcost(2, 40)
Total= tf+tv
print(tf, tv, Total)
# #program to determine how much money is left

def balance(inAmount, Total):
  bal = (inAmount - Total)
  if inAmount > Total:
    print("you can buy more fruit\t" + str(bal) + " " "is left")
  if Total > inAmount:
    print(" you are in the red-return some fruits", bal)
balance(inAmount,Total)