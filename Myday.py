import datetime
currentDate = datetime.date.today()
print(currentDate)
strDate =input('what is the date ')
print(strDate)
birthday = datetime.datetime.strptime(strDate,'%d %m %Y')
print(birthday)



