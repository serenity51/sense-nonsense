
#Given the 3 sides of a triangle – x, y and z –
# determine whether the triangle is equilateral, isosceles or obtuse.
x=3
y=4
a=5
if x==y==a:
    print("this is an equilateral triangle")
if x==y or x==a or y==a:
    print('it is an isosceles triangle')
else:
    print('this is an obtuse triangle')


#calculate electricity bill

unCon = 0
rate = 0
sur = 0
date = 0
ampayable = 0
rate1 = 5  # rate for <=100 unCon
rate2 = 8  # rate for > 100 < =200
rate3 = 10  # rate for > 200 <=300
rate4 = 20  # flat rate for > 400

sur1 = 0  # no surcharge for unCon <=100
sur2 = 2 / 100  # units consumed
sur3 = 5 / 100  # of units consumed
lateFee = 10

discount = 20
unCon = int(input('\nhow many units consumed?\t'))
print(unCon)
dt = int(input('\nenter a date\t'))
print(dt)
if unCon <= 100 and dt > 10:
    ampayable = unCon * rate1 + unCon * sur1 + lateFee
    print('\n amount 1 to be paid', ampayable)

elif unCon <= 100 and dt > 0 <= 10:
    ampayable = unCon * rate1 + unCon * sur1 - discount
    print('\namount 2 to be paid', ampayable)

if (unCon > 100) and (unCon <= 200) and dt > 10:
    ampayable = unCon * rate2 + unCon * sur2 + lateFee
    print('\namount 3 to be paid', ampayable)

elif (unCon > 100) and (unCon <= 200) and 0 < dt <= 10:
    ampayable = unCon * rate2 + unCon * sur2 - discount
    print('\namount 4 to be paid', ampayable)

if  (unCon > 200) and (unCon < 400) and dt > 10:
    ampayable = unCon * rate3 + unCon * sur3 + lateFee
    print('\namount 5 to be paid:', ampayable)

elif (unCon >200) and (unCon < 400) and 0 < dt <= 10:
    ampayable = unCon * rate3 + unCon * sur3 - discount
    print('\namount 6 to be paid', ampayable)

if  unCon >= 400 and date == 0:
    ampayable = unCon * rate4
    print('\namount 7 to be paid', ampayable)
print('have a nice day')

#Write a Python program to determine whether a given year is a leap year
y = int(input('enter a year'))
if y % 400 == 0 or y % 4 == 0 and y % 100 !=0:
  print('it is a leap year')
else:
  print("it is not a leap year")





