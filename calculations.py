#calculating the area of a room in sq feet
width   = 10
height  = 12
area = width * height
print (area)

#calculate volume of a cylinder pir2 h
# pi = 3.14
# radius   = 2
# height  =14
#
# volume = (pi * radius **2 * height)
# volume=str(round(volume,1))
# print (volume)

# calculate volume of a sphere
pi = 3.14
rad = 7
sphere_area = pi * rad **2
print(sphere_area)
sphere_area = str(round(sphere_area, 2))
circumference = 2* pi * rad
print (circumference)
print('area of the circle is:153.86')
print ('circumference of the circle is : 43.96')
#
# # calculate volume of pyramid
# #volume of pyramid is = 1/3 b*h
# b=4
# h=8
# volume = (1/3*b*h)
# volume=str(round(volume, 3))
# print (volume)
#
# #calculate volume of a con
# #cone===1/3 pir2
# pi=3.14
# r= 4
# h=13
# volume =(1/3*pi*r**2*h)
# volume = str(round(volume, 4))
# print (volume)
#
# #Calculate volume of a cube
# #cube -l*b*h or l3
# l=5
# b=5
# h=5
# volume =(l*b*h)
# volume=str(round(volume, 2))
# print (volume)
#
# #Calculate the volume of a sphere
# ##sphre = 4/3 pi r3
# pi= 3.14
# r= 4
# volume = (4/3*pi*r**3)
# volume= str(round(volume, 3))
# print (volume)


# calculate distance in miles and meters based on distance in kilometers d/t=s
# calculate time in seconds based on time in hours
# calculate speed in kms per hour, speed in miles per hour and meters per second
#distance/time= speed
#convert kms to mile divide kms /1.6
#convert kms to metres multiply kms by 1000
#convert hrs to seconds multipy by 3600
# initializing variables
dist_kms = 150
dist_mtrs =150 * 1000
dist_mls = 150/1.6
timehrs  = 2
timesec  = 2 * 3600
speed = dist_kms/timehrs
speedkms_hr = 150/2
print(speedkms_hr)
speedmls_hr = dist_mls/timehrs
print(speedmls_hr)
dist_mtrs_sec = dist_mtrs/timesec
print(dist_mtrs_sec)


distance = timehrs * speed


# # import math
# # print(type(math.pi), math.pi)
# # #getting decimal number from binary number
# # var1 = 0b1111
# # #getting decimal no. from hexadecimal no.
# # var = 0xa
# # print(var)
# # print(var1)
# # #modulo finds remainder after division
# # va = 13 // 2   # floor division --6
# # print(va)
# # v= 13/2
# # print(v)       #classic div gives 6.5
# # Vm = 5 % 2      # use of modulo gives remainder
# # print (Vm)
# # e= 2 ** 3 **2
# # print(e)
# # d = 2**9
# # print(d)