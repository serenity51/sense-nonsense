unCon = [100, 115, 120, 125, 130, 135, 140, 145, 149]
rate = [5]
sur = [0]
dt =[0]
discount =50
latefee = 100
for x in unCon:
 for y in rate:
  for z in sur:
   print('ampayable is', x * y + x*z)

unCon =[150, 160, 170, 180, 190, 204]
rate =[10]
sur =[.5]
dt =[0]
for x in unCon:
 for y in rate:
  for z in sur:
   print('ampayable is', x * y + x* z)

unCon = [205, 230, 255, 280, 305, 330, 355, 380,405]
rate =[20]
sur = [.10]
for x in unCon:
 for y in rate:
  for z in sur:
   print('ampayable is', x * y + x * z)


# this is the out put for  the first list [100, 115, 120, 125, 130, 135, 140, 145, 149] rate=5, sur=0
# ampayable is 500
# ampayable is 575
# ampayable is 600
# ampayable is 625
# ampayable is 650
# ampayable is 675
# ampayable is 700
# ampayable is 725
# ampayable is 745


# this is the output for the 2nd list[150, 160, 170, 180, 190, 200]     rate =10 and sur=.5
# ampayable is 1575.0
# ampayable is 1680.0
# ampayable is 1785.0
# ampayable is 1890.0
# ampayable is 1995.0
# ampayable is 2142.0


# this is the output for the 3rd list [205, 230, 255, 280, 305, 330, 355, 380,405]  rate =[20]   sur = [.10]
# ampayable is 4120.5
# ampayable is 4623.0
# ampayable is 5125.5
# ampayable is 5628.0
# ampayable is 6130.5
# ampayable is 6633.0
# ampayable is 7135.5
# ampayable is 7638.0
# ampayable is 8140.5