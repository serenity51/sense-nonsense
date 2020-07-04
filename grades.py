print('*'*30)
marks = int(input('enter marks\t'))
if marks >=70:
    print('you made it-you passed')
    if marks >=90:
        if marks == 100:
          print("distinction")
        elif marks >=98 or marks ==99:
          print('A++')
        elif marks >=95 <=97:
          print('print A-')
        elif marks >=91 <=94:
          print('A--')
        elif marks >=90:
          print('A grade')
    if marks >80 <=89:
        if marks >=86 <=89:
          print('good,step it up')
        elif marks >80 <=85:
          print('there is scope for improvemnt')
        elif marks ==80:
          print('try harder')
else:
    print('sorry- u failed')
    print( 'dont be disheartened-failureis the stepping stone to success')

