unCon=0
dt =0
rate1 =5
rate2 =15
rate3 =50

sur1 =0
sur2 =5/100
sur3= 10/100

latefee = 10
discount = 50

unCon = int(input('\nenter no of units used\t'))
dt = int(input('\nenter the date\t'))

for unCon in range (100, 199, 20):
    if dt <=10:
        print("--------------------------------------")
        print('BILL FOR CONSUMER')
        print('_______________________________________')
        print('no of units used \t', unCon)
        print('rate per unit \t', rate1)
        print('surcharge for sur1\t', sur1)
        print('discount allowed', discount)
        print('amount payable is ', unCon * rate1 + unCon * sur1 - discount)

for unCon in range (100, 199, 20):
    if dt >10:
       print("--------------------------------------")
       print('BILL FOR CONSUMER')
       print('_______________________________________')
       print('no of units used \t', unCon)
       print('rate per unit \t', rate1)
       print('surcharge \t', sur1)
       print('latefee to be paid', latefee)
       print('amount payable is ', unCon * rate1 + unCon * sur1 + latefee)

for unCon in range (200, 401, 100):
   if dt <10:
        print("--------------------------------------")
        print('BILL FOR CONSUMER')
        print('_______________________________________')
        print('no of units used \t', unCon)
        print('rate per unit \t', rate2)
        print('surcharge \t', sur2)
        print('discount allowed', discount)
        print('amount payable is ', unCon * rate2 + unCon * sur2 - discount)
   if dt > 10:
        print("--------------------------------------")
        print('BILL FOR CONSUMER')
        print('_______________________________________')
        print('no of units used \t', unCon)
        print('rate per unit \t', rate2)
        print('surcharge \t', sur2)
        print('latefee is', latefee)
        print('amount payable is ', unCon * rate2 + unCon * sur2 + latefee)

   for unCon in range(402, 802, 100):
       if  dt == 0:
        print("--------------------------------------")
        print('BILL FOR CONSUMER')
        print('_______________________________________')
        print('no of units used \t', unCon)
        print('rate per unit \t', rate4)
        print(unCon * 50)
