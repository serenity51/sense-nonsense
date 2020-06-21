# calculate electricity bill

unCon = 0
rate = 0
sur = 0
dt = 0
ampayable = 0
rate1 = 5  # rate for <=99 unCon
rate2 = 8  # rate for >= 100 < =199
rate3 = 10  # rate for >= 200 <=399
rate4 = 20  # flat rate for > 400

sur1 = 0  # no surcharge for unCon <=100
sur2 = 5 / 100  # units consumed
sur3 = 10 / 100  # of units consumed

lateFee = 10
discount = 20

unCon = int(input('\nhow many units consumed?\t'))
print(unCon)
dt = int(input('\nenter a date\t'))
if unCon <= 99 and dt > 10:
    ampayable = unCon * rate1 + unCon * sur1 + lateFee
    print('\n amount 1 to be paid', ampayable)
    print("------------------------------------")
    print('Bill for consumer')
    print('-------------------------------------')
    print('units consumed by user', unCon)
    print('rate applicable for that range:', rate1)
    print('surcharge payable', sur1)
    print('late fee payable', lateFee)
    print('Total amount payable', unCon * rate1 + unCon * sur1 + lateFee)

if unCon <= 99 and dt < 10:
    ampayable = unCon * rate1 + unCon * sur1 - discount
    print('\namount 2 to be paid', ampayable)
    print("------------------------------------")
    print('Bill for consumer')
    print('-------------------------------------')
    print('units consumed by user', unCon)
    print('rate applicable for that range:', rate1)
    print('surcharge payable', sur1)
    print('discount available', discount)
    print('Total amount payable', unCon * rate1 + unCon * sur1 - discount)

if 100 <= unCon <= 199 and dt < 10:
    ampayable = unCon * rate2 + unCon * sur2 - discount
    print('\namount 3 to be paid', ampayable)
    print("------------------------------------")
    print('Bill for consumer')
    print('-------------------------------------')
    print('units consumed by user', unCon)
    print('rate applicable for that range:', rate2)
    print('surcharge payable', sur2)
    print('discount available', discount)
    print('Total amount payable', unCon * rate2 + unCon * sur2 - discount)

if 100 <= unCon  <= 199 and dt > 10:
   ampayable = unCon * rate2 + unCon * sur2 + lateFee
   print('\namount 4 to be paid', ampayable)
   print('------------------------------------------')
   print("Bill For Consumer")
   print('------------------------------------------')
   print('units consumed by user', unCon)
   print('rate applicable for that range:', rate2)
   print('surcharge payable', sur2)
   print('late fee payable', lateFee)
   print('Total amount payable', unCon * rate2 + unCon * sur2 + lateFee)

if 200 <= unCon <= 399 and dt < 10:
   ampayable = unCon * rate3 + unCon * sur3 - discount
   print('\namount 5 to be paid:', ampayable)
   print('Total amount payable', unCon * rate3 + unCon * sur3 -discount)
   print("------------------------------------")
   print('Bill for consumer')
   print('-------------------------------------')
   print('units consumed by user', unCon)
   print('rate applicable for that range:', rate3)
   print('surcharge payable', sur3)
   print('discount  payable', discount)
   print('Total amount payable', unCon * rate3 + unCon * sur3 - discount)

if  200 <= unCon <= 399 and dt > 10:
   ampayable = unCon * rate3 + unCon * sur3 + lateFee
   print('\namount 5 to be paid:', ampayable)
   print('Total amount payable', unCon * rate3 + unCon * sur3 +lateFee)
   print("------------------------------------")
   print('Bill for consumer')
   print('-------------------------------------')
   print('units consumed by user', unCon)
   print('rate applicable for that range:', rate3)
   print('surcharge payable', sur3)
   print('latefee payable', lateFee)
   print('Total amount payable', unCon * rate3 + unCon * sur3 +lateFee)

if unCon >= 400:
 print ("amt payable is", unCon * rate4)
print ('have a nice day')