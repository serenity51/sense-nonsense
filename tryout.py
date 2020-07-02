drinks =['orangeade', 'lemonade', 'applejuice','grapejuice', 'gin', 'vodka']
a = ['orangeade', 'lemonade', 'applejuice','grapejuice']
b = ['gin', 'vodka', 'whisky']

for drink in drinks:
 if drink == 'gin': break
 print('i do not like', 'gin')

for drink in drinks:
 if drink == 'orangeade': continue
 print(drink)

drink =input('enter type of drink\t')
if a: print('that is okay-carry on')
else: print('be careful-you may get drunk')

# Please look at the output--looks okay except for the last bit --else not working.
# let me know--no hurry--lv msg anytime you are free.
#output for the first for loop
# i do not like gin
# i do not like gin
# i do not like gin
# i do not like gin

# output for the 2nd for loop
# lemonade
# applejuice
# grapejuice
# gin
# vodka

#output after entering drink
# enter type of drink a
# that is okay-carry on   #  this is the correct output

# enter type of drink  b
# that is okay-carry on     # this is the wrong output -getting same output for a and b


