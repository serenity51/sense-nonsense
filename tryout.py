drinks =['orangeade', 'lemonade', 'applejuice','grapejuice', 'gin', 'vodka']
a = ['orangeade', 'lemonade', 'applejuice','grapejuice']
b = ['gin', 'vodka', 'whisky']

for drink in drinks:
 if drink == 'gin':
     break
 print('i do not like gin but like', drink)

for drink in drinks:
 if drink == 'orangeade': continue
 print(drink)

drink =input('enter type of drink\t')
for a in drink :
    if a:
     print('okay-enjoy your soft drink' )

drink =input('enter type of drink\t')
for b in drink:
    if b:
     print('be careful- you may get drunk')
