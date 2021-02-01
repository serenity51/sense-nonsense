emplist= ["emp1 ", "emp2  ","emp3 ", "emp4"]
sallist=["Netsalary="]
pay =0
allowances =0
deductions = 0
def calsal(pay):
 for x in emplist:
    for y in sallist:
      n= [x + y for x in emplist for y in sallist]
      Netsalary = (pay + 1 * pay - .2 * pay)
      print(x+y, Netsalary)
print(calsal(9000))
# output
# emp1 Netsalary= 16200.0
# emp2  Netsalary= 16200.0
# emp3 Netsalary= 16200.0
# emp4Netsalary= 16200.0