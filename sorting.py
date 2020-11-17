data= [(2, 5, 7), (1, 2,5), (4, 4,8), (2, 2,6), (2, 1,3)]
s=[]
def first(s):
   return s[0]
x= sorted(data, key=first)
print(x)

output is

[(1, 2, 5), (2, 5, 7), (2, 2, 6), (2, 1, 3), (4, 4, 8)]

Question-this is in ascending order i presume. Sorting is done on the basis of s[0]
I don't' understand why  (2,5,7) comes before (2,2,6) and why (2.2.6 ) comes before (2.1,3)
please clarify