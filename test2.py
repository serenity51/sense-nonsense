# Given the 3 sides of a triangle – x, y and z –
# determine whether the triangle is equilateral, isosceles or obtuse.
# x=3
# y=4
# a=5
# if x==y==a:
#     print("this is an equilateral triangle")
# if x==y or x==a or y==a:
#     print('it is an isosceles triangle')
# else:
#     print('this is an scalene triangle')


    # determine what figure this
# Python program to take multiple inputs from the user
# a, b = input("Enter two of your lucky number: ").split()
# print("First lucky number is: ", a)
# print("Second lucky number is: ", b)

a, b = input("Enter length of two sides").split()
x, y = input('enter length of two sides').split()
x=3
y=4
a=4
b=3
if x==y==a==b:
 print('figure is a square')
if y==a and x==b:
 print('figure is a rectangle')
else:
 print('figure is a quadrilateral')

