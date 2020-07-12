# To calculate electricity bill of consumers
rate1 = 5  # rate for <=100 units consumed
rate2 = 10  # rate for >100 < 200 units consumed
rate3 = 15  # rate for >200 units <300
rate4 = 20  # flat rate for for > 300 units consumed
sur = 10 / 100  # of units consumed
latefee = 20  # for latepayers
discount = 50  # for earlypayers
def bill(uncon, dt, rate, sur,discount):
    if uncon <= 100 and dt < 10:
     return uncon * rate1 + uncon * sur -discount
    if uncon <= 100 and dt > 10:
     return uncon * rate1 + uncon * sur + latefee
    elif 100 < uncon < 199 and dt < 10:
     return uncon * rate2 +uncon *sur -discount
    elif 100 < uncon <= 199 and dt > 10:
     return uncon * rate2 + uncon * sur + latefee
    elif 200 <= uncon < 299 and dt < 10:
     return uncon *rate3 +uncon*sur -discount
    elif 200 <= uncon <= 299 and dt > 10:
     return uncon * rate3 + uncon * sur + latefee
    elif uncon >= 300 and dt >= 0:
     return uncon * rate4 +uncon*sur
    elif 300 <= uncon and dt >= 0:
      return uncon * rate4

#Bill for consumer
name= input('enter consumer name\t')
uncon= int(input('enter units consumed\t'))
dt= int(input('enter a date\t'))
latefee= int(input('enter latefee\t'))
discount= int(input('enter discount admissible\t'))

Totalamount = bill(250, 13, 15, .1, 20)
print('Totalamount payable is', Totalamount)

#This is the output that i got for 90 units consumed
# enter consumer name	preethu
# enter units consumed	90
# enter a date	3
# enter latefee	0
# enter discount admissible	50
# Totalamount payable is 409.0

#for 250
# enter consumer name	preethu
# enter units consumed	250
# enter a date	13
# enter latefee	20
# enter discount admissible	0
# Totalamount payable is 3795.0
#
# Process finished with exit code 0






