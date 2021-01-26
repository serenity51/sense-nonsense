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

# output
# 1450 300 1750
#  you are in the red-return some fruits -350
