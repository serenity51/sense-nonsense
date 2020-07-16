item =['apples', 'pears', 'oranges']
taste= ['sweet', 'sour', 'tangy']

item = input('enter item\t')
qty = int(input('enter amount bought\t'))
price = int(input('enter price\t'))
taste =input('enter fruit taste\t')

def buy(qty, price, item, taste ):
 if price <= 15 and taste== 'sweet':
     print('go ahead and buy more', item)
 if price > 16 and taste == 'sweet':
     print('get a few at least', item)

 if price <= 15 and taste == 'sour':
     print('Do not buy too many', item)
 if price > 16 and taste == 'sour':
      print('not worth buying', item)

 if price <= 15 and taste == 'tangy':
     print('This is mybest choice-', item)
 if price >16 and taste == 'tangy':
       print('It is okay-indulge for once', item)
 return qty * price
Total = buy(20, 2, 'pears', 'sour')
print("Total payable", Total)


# # enter item pears
# enter amount bought20
# enter price10
# enter fruit tastetngy
# This is mybest choice- pears
# Total payable 200

# enter item	apples
# enter amount bought	20
# enter price	20
# enter fruit taste	sour
# not worth buying apples
# Total payable 400

