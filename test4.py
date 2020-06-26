
wdy= 0 #  mon-1, tue-2,wed-3 thur-4, fri-5,(sat-6 and sun- 7- holiday)
time = 0.00
wdy = int(input('enter dy no.'))
if wdy ==6 or wdy ==7:
    print('it is a holiday- so just relax')
if wdy <=5:
   print('remember it is a working day')
   time = float(input('enter a time'))
   if 8< time  < 8.59:
    print('rise and have bkfst')
   if 9.00 < time < 9.59:
     print('time to go to work ')
   if 10.00 < time < 12.59:
     print('time to work hard')
   if 13.00 < time < 13.29:
     print('it islunchtime')
   if 13.30 < time < 17.59:
      print('continue with yur work' )
   if 18.00 < time < 21.59:
      print('finish up and gt ready to go home')
   if 22.00 < time < 23.59:
       print('time for dinner and bedtime reading')
   if time == 24.00:
       print('it is midnight-time for bed')
   if 1.00 < time < 7.00:
      print('sleep well and wake up fresh')
   else:
    print('be it a holiday or working day-be gay')








