# ['orangeade', 'lemonade', 'applejuice','grapejuice', 'gin', 'vodka', 'whisky']

soft = ['orangeade', 'lemonade', 'applejuice','grapejuice']
hard = ['gin', 'vodka', 'whisky']
count = 0
def toast(type ,count, x):
    for i in type:
        if type == soft and i==x:
            print("I love ", x)
            if count >3 and type == soft:
                print('enjoy your ', x)
    for  i in type:
        if type == hard and i == x:
            print(" drink" +" " + x + " only when you have to ")
    if count > 2 and type == hard:
        print('be careful- you may get drunk')
    return
toast(hard, 4, 'gin')